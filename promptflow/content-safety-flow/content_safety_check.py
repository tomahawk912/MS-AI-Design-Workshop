from promptflow.core import tool
import random


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def content_safety_check(text: str) -> str:
    return random.choice([True, False])