from fastapi import APIRouter
import app.modules.hydrodeck as hydrodeck

router = APIRouter(
    prefix="/control",
    tags=["control"],
)


@router.get('/')
def get_status():
    return {"hydrodeck": hydrodeck.get_status()}
