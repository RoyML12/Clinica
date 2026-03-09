from app.repositories import receta_repository

def listar_recetas():

    return receta_repository.get_recetas()


def crear_receta(data):

    return receta_repository.create_receta(data)