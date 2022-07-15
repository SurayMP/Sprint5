from clases.direccion import Direccion
from clases.razon import Razon
from clases.cuenta import Cuenta

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
        self.cuentas={
            "AHORRO_PESOS":False,
            "AHORRO_DOLARES":False,
            "CUENTA_CORRIENTE":False,
        }
        self.razones=[]
        
        # self.razones=[ Razon(x) for x in self.transacciones ]
    def __str__(self) -> str:
        return f"""{ self.transacciones,
        self.numero,
        self.nombre,
        self.apellido,
        self.dni,
        self.cuentas,
        self.razones}"""

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
        self.tarjetaDebito = True
        self.limiteDiario=10000
        # porcentaje
        self.comisionTransferencias=1
        # No puede recibir transferencias mayores a $150.000 sin previo aviso.
        self.transferenciasAClienteMax=150000
        self.cuentas={
            "AHORRO_PESOS":Cuenta("datos"),
            "AHORRO_DOLARES":False,
            "CUENTA_CORRIENTE":False,
        }
    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_credito(self) -> bool:
        return False
        
    def puede_comprar_dolar(self) -> bool:
        return False
    def datos_para_html(self):
        pass
        # self.razones=[ Razon(x,self) for x in self.transacciones ]


class ClienteGold(Cliente):
   def __init__(self,diccionarioInfoCliente) -> None:
        Cliente.__init__(self,diccionarioInfoCliente)


class ClienteBlack(Cliente):
    def __init__(self,diccionarioInfoCliente) -> None:
        Cliente.__init__(self,diccionarioInfoCliente)
        self.tarjetaCredito = 5
        self.tarjetaDebito = True
        self.limiteDiario = 100000
        self.comisionTransferencia = 0
        self.tranferenciaAClienteMax = "no Limits"
        self.chequera = 2 
        self.cuentaCorrienteNegativo = -10000 #armar funcion cuenta corriente negativo
        self.cuentas = {
            "AHORRO_PESOS":True,
            "AHORRO_DOLARES":True,
            "CUENTA_CORRIENTE":True,
        }
    def puede_crear_chequera(self) -> bool:
        return True

    def puede_crear_tarjeta_credito(self)-> bool:
        return True
    
    def puede_comprar_dolar(self)-> bool:
        return True

    def datos_para_html (self):
        pass
