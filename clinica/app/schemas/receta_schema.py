from pydantic import BaseModel

class RecetaCreate(BaseModel):

    id_cita:int
    medicamento:str
    dosis:str
    duracion_tratamiento:str
    indicaciones:str|None=None