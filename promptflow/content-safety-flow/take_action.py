from promptflow import tool

@tool
def take_action(input:dict)->bool:
    suggested_action = input['suggested_action']
    if (suggested_action == "Accept"):
        return True
    else:
        return False