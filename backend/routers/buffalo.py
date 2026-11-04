
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status

from schemas.buffalo import BuffaloCreate, BuffaloResponse

router = APIRouter(
    prefix="/buffaloes",
    tags=["Buffaloes"]
)

buffaloes: list[BuffaloResponse] = []

@router.post(
    "/",
    response_model=BuffaloResponse,
    status_code=status.HTTP_201_CREATED
)
def create_buffalo(buffalo: BuffaloCreate):

    for existing in buffaloes:
        if existing.tag_number == buffalo.tag_number:
            raise HTTPException(
                status_code=409,
                detail="A buffalo with this tag number already exists"
            )

    new_buffalo = BuffaloResponse(
        id=str(uuid4()),
        **buffalo.model_dump()
    )

    buffaloes.append(new_buffalo)

    return new_buffalo


@router.get("/", response_model=list[BuffaloResponse])
def get_buffaloes():
    return buffaloes
