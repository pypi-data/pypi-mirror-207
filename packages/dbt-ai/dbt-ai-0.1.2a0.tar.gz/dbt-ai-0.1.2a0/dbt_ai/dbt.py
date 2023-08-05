import glob
import os
import re
import yaml
import uuid
import networkx as nx
from pyvis.network import Network
import plotly.graph_objects as go

from dbt_ai.ai import generate_response, generate_dalle_image, generate_models
from dbt_ai.helper import find_yaml_files


class DbtModelProcessor:
    """Class containing functions to process and analyse a DBT project"""

    def __init__(self, dbt_project_path) -> None:
        self.dbt_project_path = dbt_project_path
        self.yaml_files = find_yaml_files(dbt_project_path)
        self.api_key_available = bool(os.getenv("OPENAI_API_KEY"))
        self.sources_yml_content = self.read_sources_yml(dbt_project_path)
        if not self.api_key_available:
            print("Warning: OPENAI_API_KEY is not set. Suggestion features will be unavailable.")

    def read_sources_yml(self, dbt_project_path: str):
        sources_yml_path = os.path.join(dbt_project_path, "models", "sources.yml")
        try:
            with open(sources_yml_path, "r") as f:
                sources_yml_content = f.read()
        except FileNotFoundError:
            print("sources.yml not found. Proceeding with an empty sources file.")
            sources_yml_content = None
        return sources_yml_content


    def get_model_refs(self, model_file_path: str) -> list:
        with open(model_file_path, "r") as f:
            content = f.read()

        refs = re.findall(r"ref\(['\"]([\w\.]+)['\"]\)", content)

        return refs

    def suggest_dbt_model_improvements(self, file_path: str, model_name: str) -> list:
        with open(file_path, "r") as f:
            content = f.read()
        prompt = f"Given the following dbt model {model_name}:\n\n{content}\n\nPlease provide suggestions on how to improve this model in terms of syntax, code structure and dbt best practices such as using ref instead of hardcoding table names:"
        response = generate_response(prompt)
        return response

    def model_has_metadata(self, model_name: str) -> bool:
        for yaml_file in self.yaml_files:
            with open(yaml_file, "r") as f:
                try:
                    yaml_content = yaml.safe_load(f)

                    if yaml_content:
                        for item in yaml_content.get("models", []):
                            if isinstance(item, dict) and item.get("name") == model_name:
                                return True
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML file {yaml_file}: {e}")

        return False

    def process_model(self, model_file: str) -> dict:
        model_name = os.path.basename(model_file).replace(".sql", "")

        has_metadata = self.model_has_metadata(model_name)
        if self.api_key_available:
            raw_suggestion = self.suggest_dbt_model_improvements(model_file, model_name)
        else:
            raw_suggestion = ""

        refs = self.get_model_refs(model_file)

        return {
            "model_name": model_name,
            "metadata_exists": has_metadata,
            "suggestions": raw_suggestion,
            "refs": refs,
        }

    def process_dbt_models(self):  # flake8: noqa
        model_files = glob.glob(os.path.join(self.dbt_project_path, "models/**/*.sql"), recursive=True)
        models = [self.process_model(model_file) for model_file in model_files]
        missing_metadata = []

        # Check for models without metadata
        for model in models:
            if not model["metadata_exists"]:
                missing_metadata.append(model["model_name"])

        return models, missing_metadata

    def generate_lineage_graph(self, models):
        # Create a directed graph
        G = nx.DiGraph()

        # Add nodes for each model
        for model in models:
            G.add_node(model["model_name"], metadata_exists=model["metadata_exists"])

        # Add edges based on ref() calls
        for model in models:
            refs = model["refs"]
            for ref in refs:
                G.add_edge(ref, model["model_name"])

        return G

    def generate_lineage_description(self, G: nx.DiGraph) -> str:
        nodes = list(nx.topological_sort(G))

        description = ""  # "The following DBT models are used:\n\n"
        for node in nodes:
            parents = list(G.predecessors(node))
            if parents:
                parent_names = ", ".join(parents)
                description += f"{node} depends on {parent_names}\n"
            else:
                description += f"{node} is a root node\n"

        return description

    def generate_lineage(self, dbt_models: list[dict]):
        G = self.generate_lineage_graph(dbt_models)
        description = self.generate_lineage_description(G)
        return description, G

    def generate_image(self, description: str) -> None:
        image_binary = generate_dalle_image(description)
        image_path = f"{self.dbt_project_path}/lineage.png"
        print(f"Saving generated lineage image in {image_path}")
        # Write image to file
        with open(image_path, "wb") as f:
            f.write(image_binary)

    def plot_directed_graph(self, G: nx.DiGraph):
        pos = nx.spring_layout(G, seed=42)

        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            mode="markers+text",
            textposition="top center",
            hoverinfo="text",
            marker=dict(color="rgb(71, 122, 193)", size=10, line=dict(width=2, color="rgb(0, 0, 0)")),
            name="Nodes",
        )

        missing_metadata_color = "rgb(255, 0, 0)"

        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=dict(width=2, color="#888"),
            hoverinfo="none",
            mode="lines",
            name="Edges",
        )

        for node in G.nodes():
            x, y = pos[node]
            node_trace["x"] += tuple([x])
            node_trace["y"] += tuple([y])
            node_trace["text"] += tuple([node])

            # set marker color and/or text label based on whether the model has metadata or not
            if "metadata_exists" in G.nodes[node] and not G.nodes[node]["metadata_exists"]:
                node_trace["marker"]["color"] = missing_metadata_color
                node_trace["text"] += tuple(["MISSING METADATA"])
            else:
                node_trace["marker"]["color"] = "rgb(71, 122, 193)"

        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_trace["x"] += tuple([x0, x1, None])
            edge_trace["y"] += tuple([y0, y1, None])

        fig = go.Figure(data=[edge_trace, node_trace])
        fig.update_layout(
            title="Directed Graph of DBT Models",
            title_x=0.5,
            title_font_size=24,
            showlegend=False,
            hovermode="closest",
            margin=dict(b=20, l=5, r=5, t=40),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.2, 1.2]),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.2, 1.2]),
        )

        fig.show()

    def create_dbt_models(self, prompt: str) -> None:
        print(f"Attempting to create dbt models based on prompt")
        sources_yml = self.sources_yml_content if self.sources_yml_content else ""
        response = generate_models(prompt, self.sources_yml_content)

        model_delimiter = "===\n\n"
        response_lines = response[0].split(model_delimiter)

        for i, model_str in enumerate(response_lines):
            if not model_str.strip():
                continue

            model_lines = model_str.strip().split("\n")
            model_name = model_lines[0].split(":")[-1].strip()
            model_content = "\n".join(model_lines[1:])
            model_content = model_content.replace("===", "")

            model_path = os.path.join(self.dbt_project_path, "models", f"{model_name}.sql")
            with open(model_path, "w") as f:
                f.write(model_content.strip())
            print(f"Created model file: {model_path}")
