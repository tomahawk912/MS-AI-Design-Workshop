from promptflow.core import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def generate_result(llm_result="", default_result="") -> str:
    if llm_result:
        return llm_result
    else:
        return default_result