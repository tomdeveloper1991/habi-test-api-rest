from typing import Type
from unittest import TestCase
import pytest
from pydantic import ValidationError
from application.api import property as property_service
from application.repository import property as property_repository
from application.dto import property_dto


class TestPropertyModule(TestCase):
    def test_when_state_is_not_in_allowed_states(self):

        with pytest.raises(ValidationError):
            property_service._validate_query_params(
                request_query_params={"state": "pre_ventas"})

    def test_when_state_is_in_allowed_states(self):
        query_params = property_service._validate_query_params(
            request_query_params={"state": "pre_venta"})

        assert query_params.state in property_dto.PropertyStateFilter.PRE_SALE.value
        assert not(query_params.city)
        assert not(query_params.year)

    def test_when_request_have_more_than_1_query_param(self):
        query_params = property_service._validate_query_params(
            request_query_params={"state": "pre_venta", "city": "bogota"})

        assert query_params.state in property_dto.PropertyStateFilter.PRE_SALE.value
        assert query_params.city
        assert not(query_params.year)


