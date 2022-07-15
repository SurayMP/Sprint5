from pickle import TRUE


class Cuenta:
    
    _monto: float
    _limite_extraccion_diario: float
    _limite_transferencia_recibida: float
    _costo_transferencias: float
    _saldo_descubierto_disponible: float

    def __init__(self,data) -> None:
        self._monto = 0
        self._limite_extraccion_diario = data.get('_limite_extraccion_diario')
        self._limite_transferencia_recibida = data.get('_limite_transferencia_recibida')
        self._costo_transferencias = data.get('_costo_transferencias')
        self._saldo_descubierto_disponible = data.get('_saldo_descubierto_disponible') or 0

    def __str__(self) -> str:
        return f"{self._limite_extraccion_diario}"



class CuentaDolares(Cuenta):
    def __init__(self, data) -> None:
        super().__init__(data)
    def comprar(self,data):
        saldo = data.get("saldoEnCuenta")
        valorDolar = data.get("valorDolar")
        cantidad = data.get("cantidad")
        monto = data.get("monto")

        # Cambiar la tupla por Diccionario??
        if saldo >= cantidad*valorDolar:
            return (TRUE,
            f"La Operacion De Compra Fue Exitosa",
            f"Compra por un costo de ${cantidad*valorDolar}",
            f"Se Recibio una Cantidad de $USD{cantidad}"
            )
        else: 
            return (False,
            f"La Operacion De Compra Fue Rechazada",
            f"Compra por un costo de ${cantidad*valorDolar}",
            f"Se Recibio una Cantidad de $USD{0}",
            )

class CuentaPesos(Cuenta):
    pass

class CuentaCorriente(Cuenta):
    pass