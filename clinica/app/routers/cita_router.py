from fastapi import APIRouter
from app.schemas.cita_schema import CitaCreate
from app.services import cita_service

router=APIRouter(prefix="/citas",tags=["Citas"])

@router.get("/")
def listar():

    return cita_service.listar_citas()


@router.post("/")
def crear(data:CitaCreate):

    return cita_service.crear_cita(data)