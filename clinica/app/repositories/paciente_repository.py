from app.database import connect_to_database

def get_pacientes():

    conn=connect_to_database()
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM pacientes")

    result=cursor.fetchall()

    conn.close()

    return result


def create_paciente(data):

    conn=connect_to_database()
    cursor=conn.cursor()

    sql="""
    INSERT INTO pacientes(nombre,telefono,fecha_nacimiento,direccion)
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(sql,(data.nombre,data.telefono,data.fecha_nacimiento,data.direccion))

    conn.commit()
    conn.close()

    return {"mensaje":"paciente creado"}


def historial_paciente(id_paciente):

    conn=connect_to_database()
    cursor=conn.cursor()

    sql="""
    SELECT
    c.id_cita,
    c.fecha_cita,
    d.nombre AS doctor,
    r.medicamento,
    r.dosis,
    r.duracion_tratamiento

    FROM citas c

    JOIN doctores d ON d.id_doctor=c.id_doctor
    LEFT JOIN recetas r ON r.id_cita=c.id_cita

    WHERE c.id_paciente=%s
    """

    cursor.execute(sql,(id_paciente))

    result=cursor.fetchall()

    conn.close()

    return result