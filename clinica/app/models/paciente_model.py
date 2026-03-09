class Paciente:
    
    def __init__(self, id_paciente, nombre, telefono=None, fecha_nacimiento=None, direccion=None):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion

    def to_dict(self):
        return {
            "id_paciente": self.id_paciente,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "fecha_nacimiento": self.fecha_nacimiento,
            "direccion": self.direccion
        }