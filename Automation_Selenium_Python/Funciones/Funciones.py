import csv
import logging
import os
import time

import allure
from allure_commons.types import AttachmentType
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class funciones_2_0:
    def __init__(self, driver):
        self.driver = driver



    ############################################################################################
    ################################## Navegador ###############################################
    ############################################################################################


    def driver_Firefox(self):
        logger.info("################################################################")
        logger.info("########🅸🅽🅸🅲🅸🅰🅽🅳🅾 🆃🅴🅽🆂🆃🅸🅽🅶 🅰🆄🆃🅾🅼🅰🆃🅸🆉🅰🅳🅾########")
        logger.info("################################################################")
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def driver_Chrome(self):
        """
        Inicializa el navegador Chrome y lo asigna al atributo self.driver.
        """

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome("\\..\\drivers\\chromedriver.exe")
        logger.info("Chrome Inicializado")

    def driver_chrome_headless(self):
        """
        Inicializa el navegador Chrome en modo headless y lo asigna al atributo self.driver.
        """
        logger.info("################")
        logger.info("Inicializando el navegador Chrome...")
        logger.info("################")
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        display = Display(visible=0, size=(800, 600))
        display.start()
        logger.info("Chrome-headless Inicializado")

        return self.driver

    def driver_mobile(self):
        """
        Inicializa el navegador Chrome con la emulación de dispositivo iPhone X y lo asigna al atributo self.driver.
        """
        mobile_emulation = {"deviceName": "iPhone X"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    ############################################################################################
    ################################## element_to_be_clickable##################################
    ############################################################################################

    def browser(self, link):
        """
        Abre una página web con la URL proporcionada y maximiza la ventana del navegador.

        :param link: URL de la página web a abrir.
        """
        try:
            self.driver.get(link)
            self.driver.maximize_window()
            logger.info("Página abierta: " + str(link))
        except Exception as ex:
            print(f"Error al inicializar y maximizar la ventana del navegador: {ex}")
            raise

    def input_Texto(self, tipo, selector, texto):
        """
        Encuentra el elemento por su selector y escribe el texto proporcionado.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        :param texto: Texto a escribir en el elemento.
        """
        try:
            WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((tipo, selector))).send_keys(texto)
            logger.info("\nEscribir en el campo {} el texto -> {}".format(selector, texto))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except ElementNotInteractableException as ex:
            logger.info(f"Error: No se puede interactuar con el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al escribir en el campo {selector}. Detalles: {ex}")
            raise

    def click_Field(self, tipo, selector):
        """
        Encuentra el elemento por su selector y realiza clic en él.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        """
        try:
            WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((tipo, selector))).click()
            time.sleep(2)
            logger.info("\nClick sobre el elemento -> {}".format(selector))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except ElementNotInteractableException as ex:
            logger.info(f"Error: No se puede interactuar con el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al hacer clic en el elemento {selector}. Detalles: {ex}")
            raise

    def clear_Field(self, tipo, selector):
        """
        Encuentra el elemento por su selector y elimina el texto presente en él.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        """
        try:
            WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((tipo, selector))).clear()
            logger.info("\nTexto eliminado -> {}".format(selector))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except ElementNotInteractableException as ex:
            logger.info(f"Error: No se puede interactuar con el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al eliminar el texto del campo {selector}. Detalles: {ex}")
            raise

    def validates(self, tipo, selector):
        """
        Encuentra el elemento por su selector y muestra el texto presente en él.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        """
        try:
            element = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((tipo, selector))).text
            logger.info(element)
            logger.info("\nElemento Validado -> {}".format(selector))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al validar el elemento {selector}. Detalles: {ex}")
            raise

    def subirArchivo(self, tipo, selector, ruta):
        """
        Encuentra el elemento por su selector y carga el archivo desde la ruta especificada.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        :param ruta: Ruta absoluta del archivo a cargar.
        """
        try:
            val = self.driver.find_element(tipo, selector)
            val.send_keys(ruta)
            logger.info("\nElemento Cargado -> {}".format(selector))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al cargar el archivo en el elemento {selector}. Detalles: {ex}")
            raise

    def scrollToElement(self, tipo, elemento):
        """
        Desplaza la vista del navegador hacia el elemento especificado.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param elemento: Selector del elemento al que se desea desplazar.
        """
        try:
            val = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((tipo, elemento)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            logger.info("\nDesplazando al elemento -> {}".format(elemento))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{elemento}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{elemento}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al desplazar al elemento {elemento}. Detalles: {ex}")
            raise

    ###################################################################################

    ########################## Allure-Report ##########################################
    ###################################################################################

    def screenShot(self, nombre):
        """
        Captura una captura de pantalla del navegador y la adjunta al reporte de Allure.

        :param nombre: Nombre del archivo de la captura de pantalla.
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type=AttachmentType.PNG)

    ###################################################################################

    ########################## ACTION CHAINS ##########################################
    ###################################################################################

    def input_Texto_ActionChains(self, tipo, selector, texto):
        """
        Encuentra el elemento por su selector, hace clic en él y escribe el texto proporcionado usando ActionChains.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        :param texto: Texto a escribir en el elemento.
        """
        action = ActionChains(self.driver)
        try:
            val = self.driver.find_element(tipo, selector, texto)
            action.click(val).perform()
            action.send_keys(texto).perform()
            time.sleep(1)
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except ElementNotInteractableException as ex:
            logger.info(f"Error: No se puede interactuar con el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al completar el campo {selector}. Detalles: {ex}")
            raise

    def clickAction(self, tipo, selector):
        """
        Encuentra el elemento por su selector y realiza clic en él usando ActionChains.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        """
        action = ActionChains(self.driver)
        try:
            val = self.driver.find_element(tipo, selector)
            action.click(val).perform()
            time.sleep(1)
            logger.info(f"\nSe hizo clic en el elemento -> {selector}")
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except ElementNotInteractableException as ex:
            logger.info(f"Error: No se puede interactuar con el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al hacer clic en el elemento {selector}. Detalles: {ex}")
            raise

    def key_Up_Key_Down(self, tecla):
        """
        Simula la pulsación y liberación de una tecla específica usando ActionChains.

        :param tecla: Tecla a simular.
        """
        action = ActionChains(self.driver)
        try:
            action.key_down(tecla).perform()
            action.key_up(tecla).perform()
            time.sleep(1)
        except Exception as ex:
            logger.info(ex)
            raise

    ############################################################################################
    ############################ visibility_of_element_located #################################
    ############################################################################################

    def input_Texto_visibility(self, tipo, selector, texto):
        """
        Encuentra el elemento por su selector y escribe el texto proporcionado después de que sea visible.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        :param texto: Texto a escribir en el elemento.
        """
        try:
            WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((tipo, selector))).send_keys(
                texto)
            time.sleep(1)
            logger.info("\nEscribir en el campo {} el texto -> {}".format(selector, texto))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except ElementNotInteractableException as ex:
            logger.info(f"Error: No se puede interactuar con el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al escribir en el campo {selector}. Detalles: {ex}")
            raise

    def click_Field_visibility(self, tipo, selector):
        """
        Encuentra el elemento por su selector y realiza clic en él después de que sea visible.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        """
        try:
            WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((tipo, selector))).click()
            time.sleep(2)
            logger.info("\nClick sobre el elemento -> {}".format(selector))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except ElementNotInteractableException as ex:
            logger.info(f"Error: No se puede interactuar con el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al hacer clic en el elemento {selector}. Detalles: {ex}")
            raise

    def clear_Field_visibility(self, tipo, selector):
        """
        Encuentra el elemento por su selector y elimina el texto presente en él después de que sea visible.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        """
        try:
            WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((tipo, selector))).clear()
            logger.info("\nTexto eliminado -> {}".format(selector))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except ElementNotInteractableException as ex:
            logger.info(f"Error: No se puede interactuar con el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al limpiar el campo {selector}. Detalles: {ex}")
            raise

    def validates_visibility(self, tipo, selector):
        """
        Encuentra el elemento por su selector, muestra el texto presente en él después de que sea visible.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        """
        try:
            element = WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((tipo, selector))).text
            logger.info(element)
            logger.info("\nElemento Validado -> {}".format(selector))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al validar el elemento {selector}. Detalles: {ex}")
            raise

    def subirArchivo_visibility(self, tipo, selector, ruta):
        """
        Encuentra el elemento por su selector y carga el archivo desde la ruta especificada después de que sea visible.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        :param ruta: Ruta absoluta del archivo a cargar.
        """
        try:
            val = self.driver.find_element(tipo, selector)
            val.send_keys(ruta)
            logger.info("\nElemento Cargado -> {}".format(selector))
            raise
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al cargar el archivo en el elemento {selector}. Detalles: {ex}")
            raise

    def scrollToElement_visibility(self, tipo, elemento):
        """
        Desplaza la vista del navegador hacia el elemento especificado después de que sea visible.

        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param elemento: Selector del elemento al que se desea desplazar.
        """
        try:
            val = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((tipo, elemento)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            logger.info("\nDesplazando al elemento -> {}".format(elemento))
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{elemento}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except TimeoutException as ex:
            logger.info(f"Error: Tiempo de espera excedido para encontrar el elemento '{elemento}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al desplazar al elemento {elemento}. Detalles: {ex}")
            raise

    def Iframe(self, tipo, selector):
        """
        Cambia al iframe especificado.

        :param tipo: Tipo de localización del iframe (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del iframe.
        """
        try:
            element = self.driver.find_element(tipo, selector)
            self.driver.switch_to.frame(element)
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al cambiar al iframe {selector}. Detalles: {ex}")
            raise

    def CrearDocumento(self, nombre_doc, nombre_columna, tipo, selector):
        """
        Crea un documento CSV y escribe el contenido de un elemento en él. Si el documento ya existe, agrega una nueva fila.

        :param nombre_doc: Nombre del documento CSV a crear o modificar.
        :param nombre_columna: Nombre de la columna donde se almacenará el valor del elemento.
        :param tipo: Tipo de localización del elemento (e.g., By.ID, By.XPATH, By.NAME, etc.).
        :param selector: Selector del elemento.
        """
        try:
            ruta_actual = os.path.abspath(__file__)
            ruta_padre = os.path.dirname(os.path.dirname(ruta_actual))
            ruta_txt = os.path.join(ruta_padre, 'txt')
            ruta_csv = os.path.join(ruta_txt, '{}.csv'.format(nombre_doc))

            elemento = WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located((tipo, selector))).text
            valor = elemento

            logger.info(valor)

            if not os.path.exists(ruta_csv):
                with open(ruta_csv, 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = [nombre_columna]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()

                    elemento = WebDriverWait(self.driver, timeout=5).until(
                        EC.visibility_of_element_located((tipo, selector))).text
                    valor = elemento
                    valor_repleace = valor.replace('"', '').replace('\n', '')
                    writer.writerow({nombre_columna: valor_repleace})
            else:
                with open(ruta_csv, 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = [nombre_columna]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    elemento = WebDriverWait(self.driver, timeout=5).until(
                        EC.visibility_of_element_located((tipo, selector))).text
                    valor = elemento
                    valor_repleace = valor.replace('"', '').replace('\n', '')
                    writer.writerow({nombre_columna: valor_repleace})
        except NoSuchElementException as ex:
            logger.info(f"Error: No se encontró el elemento con el selector '{selector}' de tipo: '{tipo}'. Detalles: {ex}")
            raise
        except Exception as ex:
            logger.info(f"Error desconocido al crear o escribir en el documento. Detalles: {ex}")
            raise

    def Change_Ventana(self):
        """
        Cambia al identificador de ventana de la nueva ventana abierta recientemente.
        """
        try:
            ventanas = self.driver.window_handles
            self.driver.switch_to.window(ventanas[1])
        except Exception as ex:
            logger.info(f"Error desconocido al cambiar a la nueva ventana. Detalles: {ex}")
            raise

    def new_window(self):
        """
        Abre una nueva ventana en blanco en el navegador y cambia al identificador de ventana de esa nueva ventana.
        """
        try:
            self.driver.execute_script("window.open('about:blank','_blank');")
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[2])
            self.driver.get()
        except Exception as ex:
            logger.info(f"Error desconocido al abrir una nueva ventana. Detalles: {ex}")
            raise