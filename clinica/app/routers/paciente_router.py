from fastapi import APIRouter
from app.schemas.paciente_schema import PacienteCreate, PacienteUpdate
from app.services import paciente_service

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])


@router.get("/")
def get_pacientes():
    return paciente_service.listar_pacientes()


@router.get("/{id_paciente}")
def get_paciente(id_paciente: int):
    return paciente_service.obtener_paciente(id_paciente)


@router.post("/")
def create_paciente(paciente: PacienteCreate):
    return paciente_service.crear_paciente(paciente)


@router.put("/{id_paciente}")
def update_paciente(id_paciente: int, paciente: PacienteUpdate):
    return paciente_service.actualizar_paciente(id_paciente, paciente)


@router.delete("/{id_paciente}")
def delete_paciente(id_paciente: int):
    return paciente_service.eliminar_paciente(id_paciente)