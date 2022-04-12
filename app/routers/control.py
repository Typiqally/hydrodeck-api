from fastapi import APIRouter, HTTPException
from starlette import status

import app.modules.hydrodeck as hydrodeck

router = APIRouter(
    prefix="/control",
    tags=["control"],
)


@router.get('/')
def get_status():
    return {"hydrodeck": hydrodeck.get_status()}


@router.post('/')
def execute_action(action: int):
    result = hydrodeck.execute_action(action)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unable to execute action '{action}'",
        )

    return {"message": f"Action '{action}' executed successfully"}
