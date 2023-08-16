from Automation_Selenium_Python.Funciones.Funciones import funciones_2_0
from behave import *
from Automation_Selenium_Python.pages.CompraFarmacia import Compra

@given(u'Iniciando Navegador en la Web : "{Web}"')
def step_1(context,Web):
    try:
        Compra.OpenBrowser(context,Web)
    except:
        context.driver.close()
        print(f"Prueba fallo en: {step_1}")


@when(u'Como usuario me dirijo a la opcion "iniciar Sesion".')
def step_2(context):
    try:
        Compra.InicioSesion(context)
    except:
        context.driver.close()
        print(f"Prueba fallo en: {step_2}")

@when(u'Completo los datos necesarios para iniciar sesion.')
def step_3(context):
    try:
        Compra.DatosInicioSesion(context)
    except:
        context.driver.close()
        print(f"Prueba fallo en: {step_3}")

@when(u'Navego hasta la barra de Busqueda en Ingreso el articulo deseado : "{Articulo}" y realizo la busqueda.')
def step_4(context,Articulo):
    try:
        Compra.SearchBar(context,Articulo)
    except:
        context.driver.close()
        print(f"Prueba fallo en: {step_4}")


@when(u'Selecciono el "{Articulo}" y visualizo el Nombre, Detalles, Precio y metodos de envio.')
def step_5(context,Articulo):
    try:
        Compra.ArticuloSelect(context,Articulo)
    except:
        context.driver.close()
        print(f"Prueba fallo en: {step_5}")

@when(u'Agrego la cantidad deseada al carrito de compras.')
def step_6(context):
    try:
        Compra.AddToCart(context)
    except:
        context.driver.close()
        print(f"Prueba fallo en: {step_6}")


@when(u'me dirijo hacia el carrito de compras para validar el articulo agregado, las cantidades agregadas, el precio unitario y el valor total.')
def step_7(context):
    try:
        Compra.GotoCart(context)
    except:
        context.driver.close()
        print(f"Prueba fallo en: {step_7}")


@when(u'Procedo a confirmar la reserva y completar los datos necesarios.')
def step_8(context):
    try:
        Compra.ConfirmarReserva(context)
    except:
        context.driver.close()
        print(f"Prueba fallo en: {step_8}")



@then(u'se visualiza el numero de orden y confirmacion de la reserva.')
def step_9(context):
    try:
        Compra.ValidarOrden(context)
        context.driver.close()
    except:
        context.driver.close()
        print(f"Prueba fallo en: {step_9}")

