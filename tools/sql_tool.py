import sqlite3
import pandas as pd

def run_sql(query):

    if not query.lower().startswith("select"):
        raise ValueError("Invalid SQL generated")

    conn = sqlite3.connect("database/sales.db")

    df = pd.read_sql(query, conn)

    conn.close()

    return df