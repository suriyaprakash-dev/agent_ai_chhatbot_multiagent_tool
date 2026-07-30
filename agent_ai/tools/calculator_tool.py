from langchain.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Perform mathematical calculations.
    """

    try:
        return str(eval(expression))

    except Exception as e:
        return str(e)