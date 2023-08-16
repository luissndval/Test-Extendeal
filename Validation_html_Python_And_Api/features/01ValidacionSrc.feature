Feature: Se desea validar que todos los src de la pagina web se encuentren funcionales.

  Scenario Outline: Solicitud Servicio
    Given "<TestCase>" Se envia la peticion web al servicio
    When Validacion de response Code parseo de HTML
    Then Se validan los link obtenidos.

    Examples:
      | TestCase |
      | TS-1-SRC |

