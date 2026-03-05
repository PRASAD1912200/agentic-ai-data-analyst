from langchain_ollama import ChatOllama
import re

llm = ChatOllama(
    model="llama3",
    temperature=0
)

def extract_sql(text):
    """
    Extract SQL query from LLM response
    """

    # find SQL inside ```sql blocks
    match = re.search(r"```sql(.*?)```", text, re.DOTALL)

    if match:
        return match.group(1).strip()

    # fallback: first SELECT statement
    match = re.search(r"(SELECT .*?;)", text, re.IGNORECASE | re.DOTALL)

    if match:
        return match.group(1).strip()

    return text.strip()


def sql_agent(state):

    question = state["question"]

    prompt = f"""
You are a SQL expert.

Database table: sales

Columns:
id, product, city, amount

IMPORTANT RULES:
- Return ONLY SQL query
- No explanation
- No text
- No markdown
- Only SQL

Example:
SELECT * FROM sales;

Question:
{question}
"""

    response = llm.invoke(prompt)

    sql_query = extract_sql(response.content)

    print("Generated SQL:", sql_query)

    return {"sql_query": sql_query}