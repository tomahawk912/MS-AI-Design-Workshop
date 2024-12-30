from promptflow.core import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def default_result(question: str) -> str:
    return f"질문하신 내용은 적절한 내용이 아닙니다 : {question}."