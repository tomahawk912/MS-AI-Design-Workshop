from promptflow import tool
import pandas as pd

@tool
def my_python_tool(code_block_to_run: str) -> str:
    # Replace this with your SAS URL
    sas_url = "<SAS URl>"

    # Read the CSV file into a DataFrame
    df = pd.read_csv(sas_url)

    # Create a dictionary for the local variables
    local_scope = {'df': df}

    # Run code block within the local scope
    exec(code_block_to_run, {}, local_scope)

    # Retrieve the 'answer' variable from the local scope
    answer = local_scope.get("answer")

    return answer