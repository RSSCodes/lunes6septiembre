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

from flask import Flask

aplicacion=Flask(__name__)
@aplicacion.route('/')
def saludar():
    return 'hola'

@aplicacion.route('/Martes')
def concepToMartes():
    return 'es el 2do dia de la semana'

@aplicacion.route('/python')
def conceptoPython():
    return 'es un lenguaje de programacion'



if __name__=='__main__':
    aplicacion.run(host='0.0.0.0',port=3500)
