from agents.pdf_agent import pdf_agent
from agents.sql_agent import sql_agent
from agents.report_agent import report_agent


def collaborate(question, config):

    print("Step 1 : PDF Agent")

    pdf_response = pdf_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        },
        config=config
    )

    pdf_answer = pdf_response["messages"][-1].content

    print(pdf_answer)

    print("Step 2 : SQL Agent")

    sql_response = sql_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content":
                    f"""
                    PDF Information

                    {pdf_answer}

                    Use this information to query the database.
                    """
                }
            ]
        },
        config=config
    )

    sql_answer = sql_response["messages"][-1].content

    print(sql_answer)

    print("Step 3 : Report Agent")

    report_response = report_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content":
                    f"""
                    PDF Result

                    {pdf_answer}

                    SQL Result

                    {sql_answer}

                    Generate one final report.
                    """
                }
            ]
        },
        config=config
    )

    return report_response