"""
Menú interactivo para CRUD de:
Autor, Libro, Ejemplar, Prestamo, Usuario
"""

import sys
from uuid import UUID
from typing import Optional

sys.path.insert(0, ".")

from src.database.config import create_tables

from src.crud import Autor as crud_autor
from src.crud import Libro as crud_libro
from src.crud import Ejemplar as crud_ejemplar
from src.crud import Prestamo as crud_prestamo
from src.crud import Usuario as crud_usuario
from src.crud import Empleado as crud_empleado
from src.crud import Reserva as crud_reserva
from src.crud import Categoria as crud_categoria
from src.crud import Editorial as crud_editorial
from src.entities.Empleado import Empleado


create_tables()
# ----------------------------
# Lectura segura
# ----------------------------


def leer_str(msg, default=""):
    val = input(msg).strip()
    return val if val else default


def leer_int(msg, default=0):
    try:
        return int(input(msg).strip() or default)
    except:
        return default


def leer_uuid(msg) -> Optional[UUID]:
    val = input(msg).strip()
    try:
        return UUID(val) if val else None
    except:
        return None


# ----------------------------
# MENÚ AUTOR
# ----------------------------


def menu_autor():
    while True:
        print("\n--- AUTOR ---")
        print("1. Crear autor")
        print("2. Listar autores")
        print("3. Buscar autor")
        print("4. Actualizar autor")
        print("5. Eliminar autor")
        print("0. Volver")

        op = leer_int("Opción: ")

        if op == 1:
            nombre = leer_str("Nombre: ")
            apellido = leer_str("Apellido: ")
            nacionalidad = leer_str("Nacionalidad: ")
            id_usuario = leer_uuid("ID usuario crea: ")

            autor = crud_autor.crear_autor(nombre, apellido, nacionalidad, id_usuario)
            print("Autor creado:", autor.id_autor)

        elif op == 2:
            autores = crud_autor.obtener_autores()
            for a in autores:
                print(a.id_autor, a.nombre, a.apellido)

        elif op == 3:
            id_autor = leer_uuid("ID: ")
            autor = crud_autor.obtener_autor_por_id(id_autor)
            print(autor)

        elif op == 4:
            id_autor = leer_uuid("ID: ")
            nombre = leer_str("Nuevo nombre: ")
            crud_autor.actualizar_autor(id_autor, None, nombre=nombre)
            print("Actualizado")

        elif op == 5:
            id_autor = leer_uuid("ID: ")
            crud_autor.eliminar_autor(id_autor)
            print("Eliminado")

        elif op == 0:
            break


def menu_libro():
    while True:
        print("\n--- LIBRO ---")
        print("1. Crear libro")
        print("2. Listar libros")
        print("3. Eliminar libro")
        print("0. Volver")

        op = leer_int("Opción: ")

        if op == 1:
            titulo = leer_str("Titulo: ")
            isbn = leer_str("ISBN: ")
            anio = leer_int("Año: ")
            editorial = leer_int("ID editorial: ")
            categoria = leer_int("ID categoria: ")
            user = leer_uuid("ID usuario: ")

            libro = crud_libro.crear_libro(
                titulo, isbn, anio, editorial, categoria, user
            )
            print("Libro creado:", libro.id_libro)

        elif op == 2:
            libros = crud_libro.obtener_libros()
            for l in libros:
                print(l.id_libro, l.titulo)

        elif op == 3:
            id_libro = leer_uuid("ID: ")
            crud_libro.eliminar_libro(id_libro)
            print("Eliminado")

        elif op == 0:
            break


def menu_ejemplar():
    while True:
        print("\n--- EJEMPLAR ---")
        print("1. Crear")
        print("2. Listar")
        print("0. Volver")

        op = leer_int("Opción: ")

        if op == 1:
            id_libro = leer_uuid("ID libro: ")
            codigo = leer_str("Codigo: ")
            estado = leer_str("Estado: ")
            ubicacion = leer_str("Ubicacion: ")
            user = leer_uuid("ID usuario: ")

            e = crud_ejemplar.crear(id_libro, codigo, estado, ubicacion, user)
            print("Creado:", e.id_ejemplar)

        elif op == 2:
            for e in crud_ejemplar.obtener_todos():
                print(e.id_ejemplar, e.estado)

        elif op == 0:
            break


from datetime import date


def menu_prestamo():
    while True:
        print("\n--- PRESTAMO ---")
        print("1. Crear")
        print("2. Listar")
        print("0. Volver")

        op = leer_int("Opción: ")

        if op == 1:
            usuario = leer_uuid("ID usuario: ")
            empleado = leer_uuid("ID empleado: ")
            user = leer_uuid("ID usuario crea: ")

            p = crud_prestamo.crear_prestamo(
                usuario,
                empleado,
                date.today(),
                date.today(),
                "ACTIVO",
                user,
            )
            print("Prestamo:", p.id_prestamo)

        elif op == 2:
            for p in crud_prestamo.obtener_prestamos():
                print(p.id_prestamo, p.estado)

        elif op == 0:
            break


def menu_usuario():
    while True:
        print("\n--- USUARIO ---")
        print("1. Crear")
        print("2. Listar")
        print("0. Volver")

        op = leer_int("Opción: ")

        if op == 1:
            nombre = leer_str("Nombre: ")
            rol = leer_str("Rol: ")
            contrasena = leer_str("Contraseña: ")

            u = crud_usuario.crear_usuario(nombre, rol, contrasena)
            print("Usuario:", u.id_usuario)

        elif op == 2:
            for u in crud_usuario.obtener_usuarios():
                print(u.id_usuario, u.nombre_usuario)

        elif op == 0:
            break


def menu_empleado():
    while True:
        print("\n--- EMPLEADO ---")
        print("1. Crear empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("0. Volver")

        op = leer_int("Opción: ")

        if op == 1:
            id_usuario = leer_uuid("ID usuario: ")
            cargo = leer_str("Cargo: ")
            salario = float(leer_str("Salario: ") or 0)
            fecha = date.today()
            tipo = leer_str("Tipo contrato: ")
            user = leer_uuid("ID usuario crea: ")

            e = crud_empleado.crear_empleado(
                id_usuario, cargo, fecha, tipo, user, salario
            )
            print("Empleado creado:", e.id_empleado)

        elif op == 2:
            empleados = crud_empleado.obtener_empleados()
            for e in empleados:
                print(e.id_empleado, e.cargo, e.estado)

        elif op == 3:
            id_emp = leer_uuid("ID: ")
            e = crud_empleado.obtener_empleado(id_emp)
            print(e)

        elif op == 4:
            id_emp = leer_uuid("ID: ")
            cargo = leer_str("Nuevo cargo: ")
            user = leer_uuid("ID usuario edita: ")

            crud_empleado.actualizar_empleado(id_emp, user, cargo=cargo)
            print("Actualizado")

        elif op == 5:
            id_emp = leer_uuid("ID: ")
            crud_empleado.eliminar_empleado(id_emp)
            print("Eliminado")

        elif op == 0:
            break


def menu_reserva():
    while True:
        print("\n--- RESERVA ---")
        print("1. Crear reserva")
        print("2. Listar reservas")
        print("3. Buscar reserva")
        print("4. Actualizar reserva")
        print("5. Eliminar reserva")
        print("0. Volver")

        op = leer_int("Opción: ")

        if op == 1:
            usuario = leer_uuid("ID usuario: ")
            libro = leer_uuid("ID libro: ")
            user = leer_uuid("ID usuario crea: ")

            r = crud_reserva.crear_reserva(usuario, libro, user)
            print("Reserva creada:", r.id_reserva)

        elif op == 2:
            reservas = crud_reserva.obtener_reservas()
            for r in reservas:
                print(r.id_reserva, r.estado)

        elif op == 3:
            id_res = leer_uuid("ID: ")
            r = crud_reserva.obtener_reserva(id_res)
            print(r)

        elif op == 4:
            id_res = leer_uuid("ID: ")
            estado = leer_str("Nuevo estado: ")
            user = leer_uuid("ID usuario edita: ")

            crud_reserva.actualizar_reserva(id_res, user, estado=estado)
            print("Actualizada")

        elif op == 5:
            id_res = leer_uuid("ID: ")
            crud_reserva.eliminar_reserva(id_res)
            print("Eliminada")

        elif op == 0:
            break

def menu_categoria():

    while True:

        print("\n--- CATEGORIA ---")

        print("1. Crear categoria")

        print("2. Listar categorias")

        print("3. Buscar categoria")

        print("4. Actualizar categoria")

        print("5. Eliminar categoria")

        print("0. Volver")
 
        op = leer_int("Opción: ")
 
        if op == 1:

            nombre = leer_str("Nombre: ")

            descripcion = leer_str("Descripcion: ")
 
            c = crud_categoria.crear_categoria(nombre, descripcion)

            print("Categoria creada:", c.id_categoria)
 
        elif op == 2:

            categorias = crud_categoria.obtener_categorias()

            for c in categorias:

                print(c.id_categoria, c.nombre)
 
        elif op == 3:

            nombre = leer_str("Buscar nombre: ")

            resultados = crud_categoria.buscar_categoria_por_nombre(nombre)

            for c in resultados:

                print(c.id_categoria, c.nombre)
 
        elif op == 4:

            id_categoria = leer_uuid("ID: ")

            nombre = leer_str("Nuevo nombre: ")

            descripcion = leer_str("Nueva descripcion: ")
 
            crud_categoria.actualizar_categoria(

                id_categoria,

                nombre=nombre,

                descripcion=descripcion,

            )

            print("Actualizado")
 
        elif op == 5:

            id_categoria = leer_uuid("ID: ")

            crud_categoria.eliminar_categoria(id_categoria)

            print("Eliminado")
 
        elif op == 0:

            break
 
def menu_editorial():

    while True:

        print("\n--- EDITORIAL ---")

        print("1. Crear editorial")

        print("2. Listar editoriales")

        print("3. Buscar editorial")

        print("4. Actualizar editorial")

        print("5. Eliminar editorial")

        print("0. Volver")
 
        op = leer_int("Opción: ")
 
        if op == 1:

            nombre = leer_str("Nombre: ")

            pais = leer_str("Pais: ")
 
            e = crud_editorial.crear_editorial(nombre, pais)

            print("Editorial creada:", e.id_editorial)
 
        elif op == 2:

            editoriales = crud_editorial.obtener_editoriales()

            for e in editoriales:

                print(e.id_editorial, e.nombre, e.pais)
 
        elif op == 3:

            nombre = leer_str("Buscar nombre: ")

            resultados = crud_editorial.buscar_editorial_por_nombre(nombre)

            for e in resultados:

                print(e.id_editorial, e.nombre)
 
        elif op == 4:

            id_editorial = leer_uuid("ID: ")

            nombre = leer_str("Nuevo nombre: ")

            pais = leer_str("Nuevo pais: ")
 
            crud_editorial.actualizar_editorial(

                id_editorial,

                nombre=nombre,

                pais=pais,

            )

            print("Actualizado")
 
        elif op == 5:

            id_editorial = leer_uuid("ID: ")

            crud_editorial.eliminar_editorial(id_editorial)

            print("Eliminado")
 
        elif op == 0:

            break
 

def main():
    while True:
        print("\n====== SISTEMA BIBLIOTECA ======")
        print("1. Autor")
        print("2. Libro")
        print("3. Ejemplar")
        print("4. Prestamo")
        print("5. Usuario")
        print("6. Empleado")
        print("7. Reserva")
        print("8. Categoria")
        print("9. Editorial")
        print("0. Salir")

        op = leer_int("Seleccione: ")

        if op == 1:
            menu_autor()
        elif op == 2:
            menu_libro()
        elif op == 3:
            menu_ejemplar()
        elif op == 4:
            menu_prestamo()
        elif op == 5:
            menu_usuario()
        elif op == 6:
            menu_empleado()
        elif op == 7:
            menu_reserva()
        elif op == 8:
            menu_categoria()
        elif op == 9:
            menu_editorial()
        elif op == 0:
            print("Saliendo...")
            break


if __name__ == "__main__":
    main()
