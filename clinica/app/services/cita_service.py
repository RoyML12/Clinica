from app.repositories import cita_repository

def listar_citas():

    return cita_repository.get_citas()


def crear_cita(data):

    return cita_repository.create_cita(data)