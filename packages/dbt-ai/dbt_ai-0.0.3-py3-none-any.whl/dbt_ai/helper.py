import glob
import os
import html


def find_yaml_files(dbt_project_path):
    yaml_files = glob.glob(os.path.join(dbt_project_path, "**/*.yml"), recursive=True)
    yaml_files.extend(glob.glob(os.path.join(dbt_project_path, "**/*.yaml"), recursive=True))
    return yaml_files


def format_suggestion(suggestion):
    html_suggestion = ""

    escaped_suggestion = html.escape(suggestion)
    formatted_suggestion = escaped_suggestion.replace("\n", "<br>")
    html_suggestion = formatted_suggestion

    return html_suggestion