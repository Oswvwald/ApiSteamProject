from datetime import datetime
from conect.conexion_app import get_connection, put_connection

def convertir_a_dict(cursor, rows):
    columnas = [col[0] for col in cursor.description]
    resultado = []
    for row in rows:
        row_dict = {}
        for col, val in zip(columnas, row):
            row_dict[col] = val.isoformat() if isinstance(val, datetime) else val
        resultado.append(row_dict)
    return resultado

def obtener_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        return convertir_a_dict(cursor, rows)
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        return []
    finally:
        cursor.close()
        put_connection(conn)

def obtener_usuario_por_id(usuario_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
        row = cursor.fetchone()
        if row:
            return convertir_a_dict(cursor, [row])[0]
        else:
            return None
    except Exception as e:
        print(f"Error al obtener usuario por ID: {e}")
        return None
    finally:
        cursor.close()
        put_connection(conn)

def crear_usuario(nombre, apellido, email, contrasena, rol):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre_usuario, apellido_usuario, email_usuario, contrasena_usuario, rol_id) VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (nombre, apellido, email, contrasena, rol)
        )
        usuario_id = cursor.fetchone()[0]
        conn.commit()
        return usuario_id
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        conn.rollback()
        return None
    finally:
        cursor.close()
        put_connection(conn)
        
def actualizar_usuario(usuario_id, nombre, apellido, email, contrasena, rol):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE usuarios SET nombre_usuario = %s, apellido_usuario = %s, email_usuario = %s, contrasena_usuario = %s, rol_id = %s WHERE id_usuarios = %s",
            (nombre, apellido, email, contrasena, rol, usuario_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        put_connection(conn)
        
def eliminar_usuario(usuario_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM usuarios WHERE id_usuarios = %s", (usuario_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        put_connection(conn)
        
def obtener_roles():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM roles")
        rows = cursor.fetchall()
        return convertir_a_dict(cursor, rows)
    except Exception as e:
        print(f"Error al obtener roles: {e}")
        return []
    finally:
        cursor.close()
        put_connection(conn)

def obtener_rol_por_id(rol_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM roles WHERE id_rol = %s", (rol_id,))
        row = cursor.fetchone()
        if row:
            return convertir_a_dict(cursor, [row])[0]
        else:
            return None
    except Exception as e:
        print(f"Error al obtener rol por ID: {e}")
        return None
    finally:
        cursor.close()
        put_connection(conn)

def crear_rol(nombre_rol):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO roles (nombre_rol) VALUES (%s) RETURNING id_rol",
            (nombre_rol,)
        )
        rol_id = cursor.fetchone()[0]
        conn.commit()
        return rol_id
    except Exception as e:
        print(f"Error al crear rol: {e}")
        conn.rollback()
        return None
    finally:
        cursor.close()
        put_connection(conn)
        
def actualizar_rol(rol_id, nombre_rol):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE roles SET nombre_rol = %s WHERE id_rol = %s",
            (nombre_rol, rol_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar rol: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        put_connection(conn)
        
def eliminar_rol(rol_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM roles WHERE id_rol = %s", (rol_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar rol: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        put_connection(conn)
        
def obtener_usuarios_por_rol(rol_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios WHERE rol_id = %s", (rol_id,))
        rows = cursor.fetchall()
        return convertir_a_dict(cursor, rows)
    except Exception as e:
        print(f"Error al obtener usuarios por rol: {e}")
        return []
    finally:
        cursor.close()
        put_connection(conn)

def login_usuario(email, contrasena):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM usuarios WHERE email_usuario = %s AND contrasena_usuario = %s",
            (email, contrasena)
        )
        row = cursor.fetchone()
        if row:
            return convertir_a_dict(cursor, [row])[0]
        else:
            return None
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return None
    finally:
        cursor.close()
        put_connection(conn)