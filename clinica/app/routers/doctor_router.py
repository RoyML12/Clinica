from fastapi import APIRouter
from app.schemas.doctor_schema import DoctorCreate
from app.services import doctor_service

router=APIRouter(prefix="/doctores",tags=["Doctores"])

@router.get("/")
def listar():

    return doctor_service.listar_doctores()


@router.post("/")
def crear(data:DoctorCreate):

    return doctor_service.crear_doctor(data)