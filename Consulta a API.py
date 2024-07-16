# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:33:30 2024

@author: Rolando Gonzàlez
"""

import requests
import json

# Consumir el recurso
URL = "https://api.lambdatest.com/automation/api/v1/platforms"

# Definir el encabezado de autenticación
headers = {
    'Authorization': 'Bearer TU_TOKEN_AQUI'  # Reemplaza TU_TOKEN_AQUI con tu token real de API
}

# Realizar la solicitud GET a la API con autenticación 
respuesta = requests.get(URL, headers=headers)

# Verificar el estado de la solicitud
if respuesta.status_code == 200:
    print('La Solicitud fue exitosa')
    print('Datos Extraidos: ', respuesta.json())
else:
    print('Error al realizar la solicitud del recurso. Detalles: \n', respuesta.text)