from pydantic import BaseModel

class DoctorCreate(BaseModel):

    nombre:str
    especialidad:str|None=None
    telefono:str|None=None