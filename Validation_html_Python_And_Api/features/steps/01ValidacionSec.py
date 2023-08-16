from behave import given, when, then
from Validation_html_Python_And_Api.Configuration import dataSet
from Validation_html_Python_And_Api.Funtions.ConsultPage import WebPage


url=dataSet.url
# Crear una instancia de la página web
web_page = None


@given(u'"{TestCase}" Se envia la peticion web al servicio')
def step_given_enviar_peticion_web(context, TestCase):
    global web_page
    url = dataSet.url  # Obtiene la URL del módulo dataSet
    web_page = WebPage(url)
    web_page.send_request()

@when(u'Validacion de response Code parseo de HTML')
def step_when_validacion_response_code(context):
    global web_page
    web_page.get_html_content()

@then(u'Se validan los link obtenidos.')
def step_then_validar_links_obtenidos(context):
    global web_page
    web_page.parse_src_attributes()
    failing_links = web_page.validate_src_links()

    if failing_links:
        print("Enlaces fallidos:")
        for link in failing_links:
            print(link)
    else:
        print("Todos los enlaces son funcionales.")