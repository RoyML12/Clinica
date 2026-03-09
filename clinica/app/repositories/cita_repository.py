from app.database import connect_to_database

def get_citas():

    conn=connect_to_database()
    cursor=conn.cursor()

    sql="""
    SELECT

    c.id_cita,
    c.fecha_cita,
    p.nombre AS paciente,
    d.nombre AS doctor,
    c.motivo,
    c.proxima_cita

    FROM citas c

    JOIN pacientes p ON p.id_paciente=c.id_paciente
    JOIN doctores d ON d.id_doctor=c.id_doctor
    """

    cursor.execute(sql)

    result=cursor.fetchall()

    conn.close()

    return result


def create_cita(data):

    conn=connect_to_database()
    cursor=conn.cursor()

    sql="""
    INSERT INTO citas(id_paciente,id_doctor,fecha_cita,motivo,proxima_cita)
    VALUES(%s,%s,%s,%s,%s)
    """

    cursor.execute(sql,(data.id_paciente,data.id_doctor,data.fecha_cita,data.motivo,data.proxima_cita))

    conn.commit()
    conn.close()

    return {"mensaje":"cita creada"}


def citas_por_doctor(id_doctor):

    conn=connect_to_database()
    cursor=conn.cursor()

    sql="""
    SELECT
    c.id_cita,
    p.nombre paciente,
    c.fecha_cita,
    c.motivo

    FROM citas c

    JOIN pacientes p ON p.id_paciente=c.id_paciente

    WHERE c.id_doctor=%s
    """

    cursor.execute(sql,(id_doctor))

    result=cursor.fetchall()

    conn.close()

    return result