import streamlit as st
import duckdb

st.title("DuckDB SQL Query Workbench")

def validate_query(sql_text) -> bool | str:
    """
    @param sql_text: The SQL query to validate.
    @return: True if the query is valid
    @throws: InvalidQueryError if the query is invalid.
    """
    return True

def run_query(sql_text: str):
    """
    @param sql_text: The SQL query to run.
    @return: The result of the query.
    """
    return None

def display_results(results):
    """
    @param results: The results of the query to display.
    """
    pass
