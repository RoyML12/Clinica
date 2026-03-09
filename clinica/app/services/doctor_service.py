from app.repositories import doctor_repository

def listar_doctores():

    return doctor_repository.get_doctores()


def crear_doctor(data):

    return doctor_repository.create_doctor(data)