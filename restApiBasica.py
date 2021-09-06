#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      LENOVO
#
# Created:     05/01/2021
# Copyright:   (c) LENOVO 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import Flask,request
import wikipedia
from flask_mysqldb import MySQL

aplicacion=Flask(__name__)
aplicacion.config['MYSQL_HOST']='localhost'
aplicacion.config['MYSQL_USER']='root'
aplicacion.config['MYSQL_PASSWORD']=''
aplicacion.config['MYSQL_DB']='conceptos'
mysql=MySQL(aplicacion)


@aplicacion.route('/')
def saludar():
    return 'hola'

@aplicacion.route('/Martes')
def concepToMartes():
    return 'es el 2do dia de la semana'

@aplicacion.route('/python')
def conceptoPython():
    return 'es un lenguaje de programacion'

@aplicacion.route('/definicion')
def definiciones():
    #ip:puerto/definicion?c=byte
    concepto=request.args.get('c')
    respuesta=''
    if concepto=='byte':
        respuesta='8 bits'
    elif concepto=='bit':
        respuesta='unidad minima de info puede tener valores 0 o 1'
    else:
        respuesta='concepto no encontrado'
    return respuesta

@aplicacion.route('/consulta')
def funcionCOnsulta():
    #ip:puerto/consulta?concepto=byte&v2=djhhjs
    Elconcepto=request.args.get('concepto')
    respuesta=''
    Elconcepto=chr(34)+Elconcepto+chr(34)
    consulta=f'select definicion from definicion where concepto={Elconcepto}'
    elCursor=mysql.connection.cursor()
    elCursor.execute(consulta)
    lineas=elCursor.fetchall()
    for linea in lineas:
        respuesta=respuesta+linea[0]+'<br>----<br>'
    return respuesta

@aplicacion.route('/insertar')
def funcionInsercion():
    #ip:puerto/insertar?concepto=byte&descripcion=8 bits
    #esto va en la url
    Elconcepto=request.args.get('concepto')
    Ladefinicion=request.args.get('descripcion')
    respuesta=''
    Elconcepto=chr(34)+Elconcepto+chr(34)
    Ladefinicion=chr(34)+Ladefinicion+chr(34)
    consulta=('insert into definicion (concepto,definicion) '+
    f'values ({Elconcepto},{Ladefinicion})')
    elCursor=mysql.connection.cursor()
    elCursor.execute(consulta)
    mysql.connection.commit()
    return 'registro agregado correctamente'

@aplicacion.route('/borrar')
def funcionBorrado():
    #ip:puerto/insertar?concepto=byte&descripcion=8 bits
    #esto va en la url
    Elconcepto=request.args.get('concepto')
    Elconcepto=chr(34)+Elconcepto+chr(34)
    consulta=('delete from definicion where '+
    f'concepto={Elconcepto}')
    elCursor=mysql.connection.cursor()
    elCursor.execute(consulta)
    mysql.connection.commit()
    return 'registro borrado correctamente'

@aplicacion.route('/actualizar')
def funcionActualizar():
    #ip:puerto/insertar?concepto=byte&descripcion=8 bits
    #esto va en la url
    Elconcepto=request.args.get('concepto')
    nuevaDefinicion=request.args.get('nuevaDescripcion')
    Elconcepto=chr(34)+Elconcepto+chr(34)
    nuevaDefinicion=chr(34)+nuevaDefinicion+chr(34)
    consulta=(f'update definicion set definicion={nuevaDefinicion} '+
    f'where concepto={Elconcepto}')
    elCursor=mysql.connection.cursor()
    elCursor.execute(consulta)
    mysql.connection.commit()
    return 'registro actualizado correctamente'



@aplicacion.route('/wiki')
def definiciones2():
    #ip:puerto/definicion?c=byte
    wikipedia.set_lang('es')
    concepto=request.args.get('w')
    respuesta=''
    try:
        resultado=wikipedia.page(concepto)
        respuesta=resultado.summary
    except:
        respuesta='termino no encontrado'
    return respuesta



if __name__=='__main__':
    aplicacion.run(host='192.168.1.104',port=8020)
