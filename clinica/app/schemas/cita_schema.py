from pydantic import BaseModel

class CitaCreate(BaseModel):

    id_paciente:int
    id_doctor:int
    fecha_cita:str
    motivo:str|None=None
    proxima_cita:str|None=None