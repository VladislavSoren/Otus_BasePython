from fastapi import APIRouter

router = APIRouter(
    # prefix='/items',
    tags=['items'],
)


@router.get("/")
def get_items():
    return {
        "data": [
            {'id': 123, 'name': 'abc'},
            {'id': 234, 'name': 'qwe'},
        ]
    }


@router.get("/{item_id}/")
def get_items(item_id: str):  # типизация через pydantic строгая!
    return {
        "data": [
            {'id': item_id, 'name': f'abc-{item_id}'},
        ]
    }


@router.post("/")
def create_item(data: dict):  # dict берётся из тела запроса
    return {'data': data}


