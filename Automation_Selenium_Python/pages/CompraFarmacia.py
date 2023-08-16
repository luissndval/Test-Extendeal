import time
from Automation_Selenium_Python.Data import DataSet
from Automation_Selenium_Python.Funciones.Funciones import funciones_2_0
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Automation_Selenium_Python.elements import ElementosHTML
t2 = 5
t3 = 10


class Compra(funciones_2_0):
    global Articulo
    def __init__(self, driver):
        super().__init__(driver)

    def OpenBrowser(self, Web):
        funciones_2_0.driver_Firefox(self)
        # funciones_2_0.driver_Firefox(self)
        # funciones_2_0.driver_mobile(self)
        funciones_2_0.browser(self, Web)
        funciones_2_0.screenShot(self, "Navegador-Iniciado")
        time.sleep(t2)

    def InicioSesion(self):
        funciones_2_0.validates(self,By.XPATH,ElementosHTML.iniciarSesiN)
        funciones_2_0.click_Field(self,By.XPATH,ElementosHTML.iniciarSesiN)
        funciones_2_0.screenShot(self, "InicioSesion")

    def DatosInicioSesion(self):
        funciones_2_0.validates(self,By.XPATH,ElementosHTML.userName)
        funciones_2_0.input_Texto(self,By.XPATH,ElementosHTML.userName,DataSet.User)
        funciones_2_0.input_Texto(self, By.XPATH, ElementosHTML.password0, DataSet.Pass)
        funciones_2_0.click_Field(self,By.XPATH, ElementosHTML.BotonLogin)
        funciones_2_0.screenShot(self, "InicioSesion")


    def SearchBar(self,Articulo):

        funciones_2_0.input_Texto(self,By.XPATH,ElementosHTML.Busqueda,Articulo)
        time.sleep(3)
        funciones_2_0.key_Up_Key_Down(self,Keys.ENTER)
        time.sleep(3)
        funciones_2_0.screenShot(self, "SearchBar")

    def ArticuloSelect(self,Articulo):
        funciones_2_0.click_Field(self,By.XPATH,f"(//a[contains(.,'{Articulo}')])[1]")
        funciones_2_0.validates(self,By.XPATH,ElementosHTML.TituloValidate)
        funciones_2_0.screenShot(self, "ArticuloSelect")

    def AddToCart(self):
        funciones_2_0.click_Field(self,By.XPATH,ElementosHTML.agregarAlCarrito)
        time.sleep(2)
        funciones_2_0.screenShot(self, "AddToCart")



    def GotoCart(self):
        funciones_2_0.click_Field(self,By.XPATH,ElementosHTML.carrito)
        Comparation = self.driver.find_element(By.XPATH,"//td[contains(@class,'product-price')]").text
        funciones_2_0.screenShot(self, "GotoCart")

    def ConfirmarReserva(self):
        funciones_2_0.click_Field(self,By.XPATH,ElementosHTML.confirmarReserva)
        funciones_2_0.click_Field(self,By.XPATH,ElementosHTML.finalizarLaReserva)
        funciones_2_0.screenShot(self, "ConfirmarReserva")

    def ValidarOrden(self):
        funciones_2_0.validates(self,By.XPATH,ElementosHTML.nMeroDelPedido)
        funciones_2_0.CrearDocumento(self,"OrdersFarmacia","Ordenes",By.XPATH,ElementosHTML.nMeroDelPedido)
        funciones_2_0.screenShot(self, "ConfirmarReserva")




