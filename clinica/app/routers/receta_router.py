from fastapi import APIRouter
from app.schemas.receta_schema import RecetaCreate
from app.services import receta_service

router=APIRouter(prefix="/recetas",tags=["Recetas"])

@router.get("/")
def listar():

    return receta_service.listar_recetas()


@router.post("/")
def crear(data:RecetaCreate):

    return receta_service.crear_receta(data)