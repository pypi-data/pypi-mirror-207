import os
from typing import List
import streamlit.components.v1 as components
import streamlit as st
from query_tool.services.query_tool_factory import get_query_tool
from query_tool.services.register import (
    init,
    register_callback,
    get_component_rerender_count,
    set_component_rerender_count,
)

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
init()

if _RELEASE:
    # __query_tool_component_function = components.declare_component(
    #     "query_tool", url="https://querytoolreact.z13.web.core.windows.net/"
    # )
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    __query_tool_component_function = components.declare_component(
        "query_tool", path=build_dir
    )
else:
    __query_tool_component_function = components.declare_component(
        "query_tool", url="http://localhost:4000"
    )


def __query_builder(
    query=None,
    title: str = "",
    database_list=None,
    table_list=None,
    column_list=None,
    error="",
    show_execute=False,
    on_click=None,
    key="b-query-builder",
    args: tuple = (),
):
    register_callback(key, on_click, *args)
    render_count = get_component_rerender_count(key)
    query_builder_value = __query_tool_component_function(
        key=key,
        query=query,
        title=title,
        database_list=database_list,
        table_list=table_list,
        column_list=column_list,
        error=error,
        show_execute=show_execute,
        render_count=render_count,
    )
    set_component_rerender_count(key)
    return query_builder_value


def handle_query_tool_actions(
    widget_key,
    on_database_change=None,
    on_table_change=None,
    on_generate_query=None,
    on_copy_query=None,
    on_execute_query=None
):
    response = st.session_state.get(widget_key)
    if response["action"] == "database_change" and on_database_change is not None:
        on_database_change(response.get("database"))
    if response["action"] == "table_change" and on_table_change is not None:
        on_table_change(response.get("database"), response.get("table"))
    if response["action"] == "preview_query" and on_generate_query is not None:
        query_tool = get_query_tool()
        query = query_tool.generate_query(response)
        on_generate_query(response, query)
    if response["action"] == "copy_to_clipboard" and on_copy_query is not None:
        on_copy_query(response.get("query"))
    if response["action"] == "execute_query" and on_execute_query is not None:
        on_execute_query(response.get("query"))


def query_tool(
    key: str = "query-tool",
    query: str = "",
    title: str = "",
    databases: List[str] = [],
    tables: List[dict] = [],
    columns: List[dict] = [],
    error="",
    show_execute=False,
    on_database_change=None,
    on_table_change=None,
    on_generate_query=None,
    on_copy_query=None,
    on_execute_query=None,
):
    return __query_builder(
        query=query,
        title=title,
        database_list=databases,
        table_list=tables,
        column_list=columns,
        error=error,
        show_execute=show_execute,
        key=key,
        on_click=handle_query_tool_actions,
        args=(
            key,
            on_database_change,
            on_table_change,
            on_generate_query,
            on_copy_query,
            on_execute_query,
        ),
    )
