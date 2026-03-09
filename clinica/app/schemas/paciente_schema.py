from pydantic import BaseModel
from typing import Optional

class PacienteBase(BaseModel):
    nombre: str
    telefono: Optional[str]
    fecha_nacimiento: Optional[str]
    direccion: Optional[str]

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(PacienteBase):
    pass

class Paciente(PacienteBase):
    id_paciente: int

    class Config:
        orm_mode = True