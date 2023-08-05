# flake8: noqa

import openai


def generate_response(prompt) -> list:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that suggests improvements to dbt models in a concise manner but following the rules outlined below. \
             Avoid suggestions related to the following: \
                - Do not provide suggestions regarding capturing metadata in a yml file, because this information \
            is being provided as part of a separate check in this application \
                - No suggestions regarding code comments \
                - Do NOT suggest using LIMIT if the model is already selecting a small number of records (e.g. under 1000) \
                - Do NOT suggest using JOIN to filter records if the model is already selecting a small number of records (e.g. under 1000) \
                    \
            For the suggestions for each model you provide, simply start it with 'Suggestions for model <model name>' \
            followed by a new line. Do NOT forget the new line! Surround the model name with ` so it is rendered like code and that underscores in the name dont get rendered. \
            Keep your suggestions fairly concise and easy to read. Order your suggestions in a logical order. \
            Follow these formatting rules for every models' suggestions: \
            Add a new line in between list entries in your suggestions to help the application render it in html more nicely. Make sure \
            this is done for all the model suggestions. Favor using new lines for every point - do not randomize the formatting. \
                The formatting for the suggestions for each model must be exactly the same i.e. in markdown bullet points",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=400,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message["content"].strip()
