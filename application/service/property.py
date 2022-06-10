from typing import List
from application.dto.property_dto import RequestPropertyDto
from application.model.property import Property
from application.repository import property as property_repository


def get_filtered_by_state_city_year(query_params: RequestPropertyDto) -> List[Property]:

    result: List[Property] = property_repository.get_filtered_by_state_city_year(
        query_params=query_params)

    return result
