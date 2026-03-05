from langgraph.graph import StateGraph

from agents.supervisor_agent import supervisor_agent
from agents.sql_agent import sql_agent
from agents.report_agent import report_agent
from tools.sql_tool import run_sql

def run_query(state):

    query = state["sql_query"]

    result = run_sql(query)

    return {"result": result}


workflow = StateGraph(dict)

workflow.add_node("supervisor", supervisor_agent)
workflow.add_node("sql_agent", sql_agent)
workflow.add_node("run_query", run_query)
workflow.add_node("report_agent", report_agent)

workflow.set_entry_point("supervisor")

workflow.add_edge("supervisor", "sql_agent")
workflow.add_edge("sql_agent", "run_query")
workflow.add_edge("run_query", "report_agent")

graph = workflow.compile()