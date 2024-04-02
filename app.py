from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

clientes = []

class Cliente:
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardarCliente', methods=['POST'])
def guardar_cliente():
    nombre = request.form['nombre']
    correo = request.form['correo']
    nit = request.form['nit']

    #  NIT
    for cliente in clientes:
        if cliente.nit == nit:
            return jsonify({'error': 'El cliente ya existe'})

    nuevo_cliente = Cliente(nombre, correo, nit)
    clientes.append(nuevo_cliente)

    #registro de clientes 
    return redirect(url_for('index'))

@app.route('/getClientes')
def obtener_clientes():
    return render_template('clientes.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
