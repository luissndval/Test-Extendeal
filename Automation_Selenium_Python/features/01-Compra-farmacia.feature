Feature: Reservar un articulo en la Pagina Web "<Web>"

  Scenario Outline: Como usuario deseo realizar una Reserva en la pagina Web: "<Web>"
    Given  Iniciando Navegador en la Web : "<Web>"
    When Como usuario me dirijo a la opcion "iniciar Sesion".
    And Completo los datos necesarios para iniciar sesion.
    When Navego hasta la barra de Busqueda en Ingreso el articulo deseado : "<Articulo>" y realizo la busqueda.
    When Selecciono el "<Articulo>" y visualizo el Nombre, Detalles, Precio y metodos de envio.
    And Agrego la cantidad deseada al carrito de compras.
    When me dirijo hacia el carrito de compras para validar el articulo agregado, las cantidades agregadas, el precio unitario y el valor total.
    When Procedo a confirmar la reserva y completar los datos necesarios.
    Then se visualiza el numero de orden y confirmacion de la reserva.

    Examples:
      | Web                                   | Articulo   |
      | https://www.farmaciasdrahorro.com.ar/ | Alikal     |
#      | https://www.farmaciasdrahorro.com.ar/ | Ibupirac   |
#      | https://www.farmaciasdrahorro.com.ar/ | Vitamina C |

