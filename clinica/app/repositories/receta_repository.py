from app.database import connect_to_database

def get_recetas():

    conn=connect_to_database()
    cursor=conn.cursor()

    sql="""
    SELECT

    r.id_receta,
    p.nombre paciente,
    d.nombre doctor,
    r.medicamento,
    r.dosis,
    r.duracion_tratamiento

    FROM recetas r

    JOIN citas c ON c.id_cita=r.id_cita
    JOIN pacientes p ON p.id_paciente=c.id_paciente
    JOIN doctores d ON d.id_doctor=c.id_doctor
    """

    cursor.execute(sql)

    result=cursor.fetchall()

    conn.close()

    return result


def create_receta(data):

    conn=connect_to_database()
    cursor=conn.cursor()

    sql="""
    INSERT INTO recetas(id_cita,medicamento,dosis,duracion_tratamiento,indicaciones)
    VALUES(%s,%s,%s,%s,%s)
    """

    cursor.execute(sql,(data.id_cita,data.medicamento,data.dosis,data.duracion_tratamiento,data.indicaciones))

    conn.commit()
    conn.close()

    return {"mensaje":"receta creada"}


def recetas_por_cita(id_cita):

    conn=connect_to_database()
    cursor=conn.cursor()

    sql="""
    SELECT
    medicamento,
    dosis,
    duracion_tratamiento
    FROM recetas
    WHERE id_cita=%s
    """

    cursor.execute(sql,(id_cita))

    result=cursor.fetchall()

    conn.close()

    return result