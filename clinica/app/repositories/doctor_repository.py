from app.database import connect_to_database

def get_doctores():

    conn=connect_to_database()
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM doctores")

    result=cursor.fetchall()

    conn.close()

    return result


def create_doctor(data):

    conn=connect_to_database()
    cursor=conn.cursor()

    sql="""
    INSERT INTO doctores(nombre,especialidad,telefono)
    VALUES(%s,%s,%s)
    """

    cursor.execute(sql,(data.nombre,data.especialidad,data.telefono))

    conn.commit()
    conn.close()

    return {"mensaje":"doctor creado"}