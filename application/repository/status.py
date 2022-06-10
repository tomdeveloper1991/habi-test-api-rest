from application.repository import connector


def get_last_status_id_by_property_id(property_id: int) -> int:

    result_id: int = 0

    adapter = connector.MsqlAdapter()

    query = f"SELECT max(status_id), property_id FROM status_history WHERE property_id={property_id} GROUP BY property_id;"

    cursor = adapter.connection.cursor()
    cursor.execute(query)

    records = cursor.fetchall()

    for record in records:
        result_id = record[0]

    return result_id
