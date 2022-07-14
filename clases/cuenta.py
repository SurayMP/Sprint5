# Varias clases con los tipos de cuentas o le asignamos un tipo a una variable?
class Cuenta:
    
    _limite_extraccion_diario: float
    _limite_transferencia_recibida: float
    _monto: float
    _costo_transferencias: float
    _saldo_descubierto_transferible: float

    def __init__(self) -> None:
        """ DireccionCompleta Diccionario? o Array? """
        self._limite_extraccion_diario = 0
        self._limite_transferencia_recibida = 0
        self._monto = 0
        self._costo_transferencias = 0
        self._saldo_descubierto_transferible = 0



