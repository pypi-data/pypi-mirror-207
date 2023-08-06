from typing import List, Any, Union, Optional, Dict

from pydantic import BaseModel, Field


class Type(BaseModel):
    name: str

    class Config:
        extra = "allow"


class Evaluation(BaseModel):
    question: str
    name: str

    class Config:
        extra = "allow"


class Query(BaseModel):
    name: str
    value: Any
    type: Union[Type, str]


class Response(BaseModel):
    name: str
    value: Any
    type: Union[Type, str]
    evaluation: List[Evaluation]


class Context(BaseModel):
    name: str
    value: Any
    type: Union[Type, str]


class Submitter(BaseModel):
    name: str
    version: str


class CommonCaseFormat(BaseModel):
    case_id: str = Field(
        None,
        description="Case id given by the user used for identifying specific cases.",
    )
    version: int = Field(1, description="Version of the Common Case Format.")
    submitter: Submitter = Field(..., description="Who is the submitter of the case")
    query: List[Query] = Field(
        ...,
        description="List of query objects that describes what was the input for the case",
    )
    response: List[Response] = Field(
        ..., description="List of response objects that describes what was the response"
    )
    context: Optional[List[Context]] = Field(
        None, description="Context that was available for model"
    )
    metadata: Dict[str, Any] = Field(
        ..., description="Additional metadata that will be saved with the case"
    )


class OpenCase(CommonCaseFormat):
    id: str
    created_at: str
    is_archived: Optional[bool] = None
    is_open: Optional[bool] = None
