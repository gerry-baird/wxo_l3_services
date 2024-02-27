from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.routing import APIRoute
from model.models import LLM_Request, LLM_Response, Message
from responses.response_util import build_data
from deep_compare import CompareVariables

app = FastAPI()
security = HTTPBasic()


# this is our datastore
preset_responses = build_data()

@app.get("/ping")
async def ping(credentials: HTTPBasicCredentials = Depends(security)) -> Message:
    return {"message": "WxO L3 services are alive"}


@app.post("/v1/generate")
async def generate(llm_request: LLM_Request) -> LLM_Response:

    if "John" in llm_request.prompt:
        response = LLM_Response(
            message=preset_responses['John']
        )
        return response

    if "Sam" in llm_request.prompt:
        response = LLM_Response(
            message=preset_responses['Sam']
        )
        return response

    if "Oliver" in llm_request.prompt:
        response = LLM_Response(
            message=preset_responses['Oliver']
        )
        return response

    if "Janet" in llm_request.prompt:
        response = LLM_Response(
            message=preset_responses['Janet']
        )
        return response

    if "Mary" in llm_request.prompt:
        response = LLM_Response(
            message=preset_responses['Mary']
        )
        return response

    # Default response will be for extreme sports
    response = LLM_Response(
        message=preset_responses['extreme']
    )
    return response




def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, operation ID will be 'greeting'


use_route_names_as_operation_ids(app)