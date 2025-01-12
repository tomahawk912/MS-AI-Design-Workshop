from promptflow.core import tool

@tool
def default_result(question: str) -> str:
    return f"질문하신 내용은 적절한 내용이 아닙니다 : {question}."