from app.repositories import paciente_repository

def listar_pacientes():
    return paciente_repository.get_pacientes()


def obtener_paciente(id_paciente):
    return paciente_repository.get_paciente(id_paciente)


def crear_paciente(data):
    return paciente_repository.create_paciente(data)


def actualizar_paciente(id_paciente, data):
    return paciente_repository.update_paciente(id_paciente, data)


def eliminar_paciente(id_paciente):
    return paciente_repository.delete_paciente(id_paciente)