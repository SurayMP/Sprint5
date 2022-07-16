from clases.cuenta import Cuenta
from clases.direccion import Direccion
from clases.razon import RealizarOperacion


class Cliente:
    """
    """
    def __init__(self,diccionarioInfoCliente) -> None:
        self.transacciones = diccionarioInfoCliente.get('transacciones')
        self.numero= diccionarioInfoCliente.get('numero')
        self.nombre= diccionarioInfoCliente.get('nombre')
        self.apellido= diccionarioInfoCliente.get('apellido')
        self.dni= diccionarioInfoCliente.get('DNI')
        self.tarjetaCredito=False
        self.tarjetaDebito = False
        self.chequera = False
        self.dolares = False
        self.cuenta=None
        self.razones=[]
        
        # self.razones=[ Razon(x) for x in self.transacciones ]
    def __str__(self) -> str:
        return f"""\n
        {self.numero}\n
        {self.nombre}\n
        {self.apellido}\n
        {self.dni}\n
        {self.cuentas}\n
        {self.razones}"""

    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_credito(self) -> bool:
        return False
        
    def puede_comprar_dolar(self) -> bool:
        return False
    def datos_para_html(self):
        pass

class ClienteClassic(Cliente):
    def __init__(self,diccionarioInfoCliente) -> None:
        Cliente.__init__(self,diccionarioInfoCliente)
        self.tarjetaDebito = 1
        self.cuenta=Cuenta({
            "_limite_extraccion_diario":10000,
            "_limite_transferencia_recibida":150000,
            "_costo_transferencias":1,
            "_saldo_descubierto_disponible":0
        })
        self.razones=[ RealizarOperacion(self,cadaTransacc) for cadaTransacc in self.transacciones ]


    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_credito(self) -> bool:
        return False
        
    def puede_comprar_dolar(self) -> bool:
        return False
    def datos_para_html (self):
        print(self.razones)
        return self.razones
        # self.razones=[ Razon(x,self) for x in self.transacciones ]
    # def __str__(self):
    #     return self.cuentas.get("AHORRO_PESOS").__str__()


class ClienteGold(Cliente):
   def __init__(self,diccionarioInfoCliente) -> None:
        Cliente.__init__(self,diccionarioInfoCliente)


class ClienteBlack(Cliente):
    def __init__(self,diccionarioInfoCliente) -> None:
        Cliente.__init__(self,diccionarioInfoCliente)
        self.tarjetaCredito = 5
        self.tarjetaDebito = True
        self.chequera = 2 
        self.cuenta = Cuenta({
            "_limite_extraccion_diario":100000,
            "_limite_transferencia_recibida":0,
            "_costo_transferencias":0,
            "_saldo_descubierto_disponible":-10000
        })
        self.razones=[ RealizarOperacion(self,cadaTransacc) for cadaTransacc in self.transacciones ]
    def puede_crear_chequera(self) -> bool:
        return True

    def puede_crear_tarjeta_credito(self)-> bool:
        return True
    
    def puede_comprar_dolar(self)-> bool:
        return True

    def datos_para_html (self):
        print(self.razones)
        return self.razones
