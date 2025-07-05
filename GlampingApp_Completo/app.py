from flask import Flask, render_template, request, redirect, url_for
from glamping import Glamping, glampings
from alojamiento import Alojamiento, alojamientos
from huesped import Huesped, huespedes
from empleado import Empleado, empleados
from reserva import Reserva, reservas, calcular_precio
from servicios import servicios
from reportes import calcular_ingresos

app = Flask(__name__)

usuarios = []

@app.route('/')
@app.route('/usuarios')
def mostrar_usuarios():
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/glampings')
def mostrar_glampings():
    return render_template('glampings.html', glampings=glampings)

@app.route('/alojamientos')
def mostrar_alojamientos():
    return render_template('alojamientos.html', alojamientos=alojamientos)

@app.route('/huespedes')
def mostrar_huespedes():
    return render_template('huespedes.html', huespedes=huespedes)

@app.route('/empleados')
def mostrar_empleados():
    return render_template('empleados.html', empleados=empleados)

@app.route('/reservas')
def mostrar_reservas():
    return render_template('reservas.html', reservas=reservas)

@app.route('/servicios')
def mostrar_servicios():
    return render_template('servicios.html', servicios=servicios)

@app.route('/reportes')
def mostrar_reportes():
    ingresos = calcular_ingresos()
    return render_template('reportes.html', ingresos=ingresos)

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    email = request.form['email']
    usuarios.append({
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'email': email
    })
    return redirect(url_for('mostrar_usuarios'))

@app.route('/crear_glamping', methods=['POST'])
def crear_glamping():
    nombre = request.form['glamping_nombre']
    ubicacion = request.form['ubicacion']
    capacidad = request.form['capacidad']
    precio = request.form['precio']
    glampings.append(Glamping(nombre, ubicacion, capacidad, precio))
    return redirect(url_for('mostrar_glampings'))

@app.route('/crear_alojamiento', methods=['POST'])
def crear_alojamiento():
    tipo = request.form['tipo']
    capacidad = int(request.form['capacidad'])
    precio = float(request.form['precio'])
    alojamientos.append(Alojamiento(tipo, capacidad, precio))
    return redirect(url_for('mostrar_alojamientos'))

@app.route('/crear_huesped', methods=['POST'])
def crear_huesped():
    nombre = request.form['nombre']
    documento = request.form['documento']
    huespedes.append(Huesped(nombre, documento))
    return redirect(url_for('mostrar_huespedes'))

@app.route('/crear_empleado', methods=['POST'])
def crear_empleado():
    nombre = request.form['nombre']
    rol = request.form['rol']
    empleados.append(Empleado(nombre, rol))
    return redirect(url_for('mostrar_empleados'))

@app.route('/crear_reserva', methods=['POST'])
def crear_reserva():
    huesped = request.form['huesped']
    alojamiento = request.form['alojamiento']
    temporada = request.form['temporada']
    precio_total = calcular_precio(temporada)
    reservas.append(Reserva(huesped, alojamiento, temporada, precio_total))
    return redirect(url_for('mostrar_reservas'))

if __name__ == '__main__':
    app.run(debug=True)
