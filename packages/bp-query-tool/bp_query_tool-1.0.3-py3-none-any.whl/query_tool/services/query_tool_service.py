class QueryTool:
    def __init__(self, entities_cls, filters_cls, dimesion_cls):
        self.__entities_cls = entities_cls
        self.__filters_cls = filters_cls
        self.__dimesion_cls = dimesion_cls

    def generate_query(self, query_json):
        (
            entities_columns,
            entities_tables_with_aliases,
            relations,
            table_aliases,
        ) = self.__entities_cls.get_entities(query_json.get("entity_data"))
        filters = self.__filters_cls.get_filter_query(
            query_json.get("filter_data"), table_aliases
        )
        dimensions, measures, measure_columns = self.__dimesion_cls.get_dimension_query(
            query_json.get("dimension_data"), table_aliases
        )
        return self.__get_query(
            entities_columns,
            relations,
            filters,
            dimensions,
            measures,
            entities_tables_with_aliases,
            measure_columns,
            query_json
        )

    def __get_query(
        self,
        entities_columns,
        relations,
        filters,
        dimensions,
        measures,
        entities_tables_with_aliases,
        measure_columns,
        query_json
    ) -> str:
        sql_array = ["SELECT"]
        select_query = ""

        if len(entities_columns) > 0:
            # Check select columns are in group by clause or in aggregate columns list
            if len(dimensions) > 0:
                select_columns = [select_column for select_column in entities_columns if select_column in dimensions]
                select_query += ", ".join(select_columns)
            else: 
                select_query += ", ".join(entities_columns)

        if len(measures) > 0:
            select_query = f"{select_query}, " if select_query else select_query
            select_query += ", ".join(measures)

        sql_array.append(select_query)

        if len(entities_tables_with_aliases) > 0:
            sql_array.append("FROM")
            sql_array.append(", ".join(entities_tables_with_aliases))

        if len(relations) > 0:
            sql_array.append(" ".join(relations))

        if len(filters) > 0:
            sql_array.append("WHERE")
            sql_array.append(" ".join(filters))

        if len(dimensions) > 0:
            sql_array.append("GROUP BY")
            sql_array.append(", ".join(dimensions))

        options = query_json.get("options", {})
        limit_records = options.get("limit", None)
        if limit_records is not None and limit_records != -1:
            sql_array.append("LIMIT " + str(limit_records))
        return " ".join(sql_array)
