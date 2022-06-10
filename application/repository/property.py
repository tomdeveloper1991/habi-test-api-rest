from typing import List, Optional
from application.dto.property_dto import RequestPropertyDto
from application.repository import connector
from application.model.property import Property
from application.repository import status as status_repository


def get_all() -> List[Property]:

    try:

        result: List[Property] = []

        adapter = connector.MsqlAdapter()

        query = "SELECT * FROM property;"

        cursor = adapter.connection.cursor()
        cursor.execute(query)

        records = cursor.fetchall()

        for record in records:
            result.append(Property(
                id=record[0],
                address=record[1],
                city=record[2],
                price=record[3],
                description=record[4] or None,
                year=record[5] or None
            ))

        adapter.close_connection()

        return result

    except Exception as e:
        raise


def get_filtered_by_state_city_year(query_params: RequestPropertyDto) -> List[Property]:

    result: List[Property] = []

    adapter = connector.MsqlAdapter()

    city_filter: str = ""
    year_filter: str = ""

    if query_params.city:
        city_filter = f" AND P.city=\"{query_params.city}\""

    if query_params.year:
        year_filter = f" AND P.year={query_params.year}"

    query = f"SELECT P.*, S.name FROM property P JOIN (SELECT max(status_id) as status_id_max, property_id FROM status_history GROUP BY property_id) SH ON P.id=SH.property_id JOIN status S ON S.id=SH.status_id_max WHERE S.name=\"{query_params.state}\"{city_filter}{year_filter};"

    cursor = adapter.connection.cursor()
    cursor.execute(query)

    records = cursor.fetchall()

    for record in records:
        result.append(Property(
            id=record[0],
            address=record[1],
            city=record[2],
            price=record[3],
            description=record[4] or None,
            year=record[5] or None,
            status_name=record[6] or None
        ))

    adapter.close_connection()

    return result
