from direccion import Direccion

class Cliente:
    """
    ## Ayuda 
    - markdown?  
    yes
    """
    # direccion completa un diccionario con los campos
    # o hacemos primero el objeto direccion y despues lo asignamos al cliente?
    def __init__(self,nombre,apellido,numero,dni,direccionCompleta,cuentas={}) -> None:
        self.nombre= nombre
        self.apellido= apellido
        self.numero= numero
        self.dni= dni
        self.cuentas = cuentas
        self.direccion = Direccion(direccionCompleta)

    def __str__(self) -> str:
        return f"{self.apellido} {self.nombre}"

    def puede_crear_chequera() -> bool:
        return True

    def puede_crear_tarjeta_credito() -> bool:
        return True
        
    def puede_comprar_dolar() -> bool:
        return True


class ClienteClassic(Cliente):
    def __init__(self,nombre,apellido,numero,dni) -> None:
        Cliente.__init__(nombre,apellido,numero,dni)
        pass
class ClienteGold(Cliente):
    def __init__(self,nombre,apellido,numero,dni) -> None:
        Cliente.__init__(nombre,apellido,numero,dni)
        pass
class ClienteBlack(Cliente):
    def __init__(self,nombre,apellido,numero,dni) -> None:
        Cliente.__init__(nombre,apellido,numero,dni)
        pass