from typing import Any, Dict
from flask import Blueprint, Response, request
import json

from pydantic import ValidationError

from application.dto.property_dto import RequestPropertyDto, ResponsePropertyDto
from application.service import property as property_service

property = Blueprint("property", __name__)

property.url_prefix = "/property"

APPLICATION_JSON = "application/json"


@property.route("/", methods=["GET"])
def get_by_state():
    try:
        query_params = _validate_query_params(
            request_query_params=request.args.to_dict())
        properties = property_service.get_filtered_by_state_city_year(
            query_params=query_params)

        response_dto = ResponsePropertyDto(
            property_result=properties
        )

        return Response(json.dumps({"payload": response_dto.dict()}), mimetype=APPLICATION_JSON, status=200)
    except ValidationError as e:
        return Response(json.dumps({"errors": json.loads(e.json())}), mimetype=APPLICATION_JSON, status=400)
    except Exception as e:
        raise


def _validate_query_params(request_query_params: Dict[str, Any]) -> RequestPropertyDto:

    return RequestPropertyDto.parse_obj(request_query_params)
