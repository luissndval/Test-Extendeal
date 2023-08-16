import json
import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Apis:

    def get_request(url, headers=None, params=None):
        """
        Realiza una solicitud GET a la URL proporcionada.

        :param url: La URL de la API a la cual realizar la solicitud.
        :param headers: (opcional) Un diccionario con las cabeceras de la solicitud.
        :param params: (opcional) Un diccionario con los parámetros de la solicitud.
        :return: La respuesta de la solicitud (objeto Response de requests).
        """
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Lanza una excepción en caso de que la respuesta sea un error (código de estado >= 400)
            return response
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud GET:", e)
            return None

    def post_request(url, data=None, headers=None, json=None):
        """
        Realiza una solicitud POST a la URL proporcionada.

        :param url: La URL de la API a la cual realizar la solicitud.
        :param data: (opcional) Un diccionario con los datos para la solicitud (se enviará como form-urlencoded).
        :param headers: (opcional) Un diccionario con las cabeceras de la solicitud.
        :param json: (opcional) Un diccionario con los datos para la solicitud (se enviará en formato JSON).
        :return: La respuesta de la solicitud (objeto Response de requests).
        """
        try:
            response = requests.post(url, data=data, headers=headers, json=json)
            response.raise_for_status()  # Lanza una excepción en caso de que la respuesta sea un error (código de estado >= 400)
            return response
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud POST:", e)
            return None

    def put_request(url, data=None, headers=None, json=None):
        """
        Realiza una solicitud PUT a la URL proporcionada.

        :param url: La URL de la API a la cual realizar la solicitud.
        :param data: (opcional) Un diccionario con los datos para la solicitud (se enviará como form-urlencoded).
        :param headers: (opcional) Un diccionario con las cabeceras de la solicitud.
        :param json: (opcional) Un diccionario con los datos para la solicitud (se enviará en formato JSON).
        :return: La respuesta de la solicitud (objeto Response de requests).
        """
        try:
            response = requests.put(url, data=data, headers=headers, json=json)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud PUT:", e)
            return None

    def delete_request(url, headers=None):
        """
        Realiza una solicitud DELETE a la URL proporcionada.

        :param url: La URL de la API a la cual realizar la solicitud.
        :param headers: (opcional) Un diccionario con las cabeceras de la solicitud.
        :return: La respuesta de la solicitud (objeto Response de requests).
        """
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud DELETE:", e)
            return None

    def head_request(url, headers=None):
        """
        Realiza una solicitud HEAD a la URL proporcionada.

        :param url: La URL de la API a la cual realizar la solicitud.
        :param headers: (opcional) Un diccionario con las cabeceras de la solicitud.
        :return: La respuesta de la solicitud (objeto Response de requests).
        """
        try:
            response = requests.head(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud HEAD:", e)
            return None

    def get_request_with_auth(url, auth, headers=None, params=None):
        """
        Realiza una solicitud GET a la URL proporcionada con autenticación básica.

        :param url: La URL de la API a la cual realizar la solicitud.
        :param auth: Una tupla (username, password) para la autenticación básica.
        :param headers: (opcional) Un diccionario con las cabeceras de la solicitud.
        :param params: (opcional) Un diccionario con los parámetros de la solicitud.
        :return: La respuesta de la solicitud (objeto Response de requests).
        """
        try:
            response = requests.get(url, headers=headers, params=params, auth=auth)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud GET con autenticación:", e)
            return None

    def post_request_with_cookies(url, data=None, headers=None, json=None, cookies=None):
        """
        Realiza una solicitud POST a la URL proporcionada con cookies.

        :param url: La URL de la API a la cual realizar la solicitud.
        :param data: (opcional) Un diccionario con los datos para la solicitud (se enviará como form-urlencoded).
        :param headers: (opcional) Un diccionario con las cabeceras de la solicitud.
        :param json: (opcional) Un diccionario con los datos para la solicitud (se enviará en formato JSON).
        :param cookies: (opcional) Un diccionario con las cookies para la solicitud.
        :return: La respuesta de la solicitud (objeto Response de requests).
        """
        try:
            response = requests.post(url, data=data, headers=headers, json=json, cookies=cookies)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud POST con cookies:", e)
            return None

    def get_field_value_from_json(response_json, field_name):
        """
        Extrae el valor de un campo específico de un diccionario JSON.

        :param response_json: El diccionario JSON de la respuesta.
        :param field_name: El nombre del campo cuyo valor queremos obtener.
        :return: El valor del campo o None si el campo no está presente en el JSON.
        """
        try:
            return response_json[field_name]
        except KeyError:
            print(f"El campo '{field_name}' no está presente en la respuesta JSON.")
            return None

    def get_field_value_from_json(response_content, field_name, default_value=None):
        """
        Extrae el valor de un campo específico de un diccionario JSON.

        :param response_content: El contenido de la respuesta (texto o bytes).
        :param field_name: El nombre del campo cuyo valor queremos obtener.
        :param default_value: (opcional) El valor predeterminado a devolver si el campo no está presente o hay un error.
        :return: El valor del campo o el valor predeterminado si el campo no está presente o hay un error.
        """
        try:
            response_json = json.loads(response_content)
            return response_json[field_name]
        except (json.JSONDecodeError, KeyError):
            print(f"El campo '{field_name}' no está presente o la respuesta no es un JSON válido.")
            return default_value

    """##############################################################################
       ########################## CONSULTA WEB SERVICE Y HTML########################
       ##############################################################################"""

