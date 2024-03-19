import os
import sqlite3
from flask import Flask, request, jsonify

app = Flask('main')
banco_dados = sqlite3.connect('banco_dados.db')
cursor = banco_dados.cursor()

comando_sql1 = """
CREATE TABLE IF NOT EXISTS CUSTOMER (
    ID INTEGER PRIMARY KEY NOT NULL,
    NAME VARCHAR(50) NOT NULL,
    CARD_ID VARCHAR(10)
)
"""
comando_sql2 = """
CREATE TABLE IF NOT EXISTS VEHICLE (
    ID INTEGER PRIMARY KEY NOT NULL,
    PLATE VARCHAR(10) NOT NULL,
    MODEL VARCHAR(30),
    DESCRIPTION VARCHAR(50),
    CUSTOMER_ID INTEGER,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(ID)
)
"""
comando_sql3 = """
CREATE TABLE IF NOT EXISTS PLAN (
    ID INTEGER PRIMARY KEY NOT NULL,
    DESCRIPTION VARCHAR(50) NOT NULL,
    VALUE FLOAT NOT NULL
)
"""

comando_sql4 = """
CREATE TABLE IF NOT EXISTS CUSTOMER_PLAN (
    ID INTEGER PRIMARY KEY NOT NULL,
    CUSTOMER_ID INTEGER NOT NULL,
    PLAN_ID INTEGER NOT NULL,
    DUE_DATE DATETIME NULL,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(ID),
    FOREIGN KEY (PLAN_ID) REFERENCES PLAN(ID)
    
)
"""
comando_sql5 = """
CREATE TABLE IF NOT EXISTS CONTRACT (
    ID INTEGER PRIMARY KEY NOT NULL,
    DESCRIPTION VARCHAR(50) NOT NULL,
    MAX_VALUE FLOAT NULL
)
"""
comando_sql6 = """
CREATE TABLE IF NOT EXISTS CONTRACT_RULE (
    ID INTEGER PRIMARY KEY NOT NULL,
    CONTRACT_ID INTEGER NOT NULL,
    UNTIL INTEGER NOT NULL,
    VALUE FLOAR NOR NULL,
    FOREIGN KEY (CONTRACT_ID) REFERENCES CONTRACT(ID)
)
"""
comando_sql7 = """
CREATE TABLE IF NOT EXISTS PARKMOVEMENT (
    ID INTEGER PRIMARY KEY NOT NULL,
    ENTRY_DATE DATETIME NOT NULL,
    EXIT_DATE DATETIME NULL,
    VEHICLE_ID INTEGER,
    VALUE FLOAT NULL,
    FOREIGN KEY (VEHICLE_ID) REFERENCES VEHICLE(ID)
)
"""

cursor.execute(comando_sql1)
cursor.execute(comando_sql2)
cursor.execute(comando_sql3)
cursor.execute(comando_sql4)
cursor.execute(comando_sql5)
cursor.execute(comando_sql6)
cursor.execute(comando_sql7)

banco_dados.commit()

@app.route('/api/v1/customer', methods=['POST'])
def cadastrar_cliente():
    data = request.json
    return jsonify({'message': 'Cliente cadastrado com sucesso'}), 201

@app.route('/api/v1/plan', methods=['POST'])
def cadastrar_plano():
    data = request.json
    return jsonify({'message': 'Plano cadastrado com sucesso'}), 201

@app.route('/api/v1/vehicle', methods=['POST'])
def cadastrar_veiculo():
    data = request.json
    return jsonify({'message': 'Veículo cadastrado com sucesso'}), 201

@app.route('/api/v1/contract', methods=['POST'])
def cadastrar_contrato():
    data = request.json
    return jsonify({'message': 'Contrato cadastrado com sucesso'}), 201

@app.route('/api/v1/customer/<int:id>', methods=['GET'])
def buscar_cliente(id):
    cursor.execute("SELECT * FROM CUSTOMER WHERE ID=?", (id,))
    cliente = cursor.fetchone()
    if cliente:
        return jsonify({'cliente': cliente}), 200
    else:
        return jsonify({'message': 'Cliente não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)


        
        