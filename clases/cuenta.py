
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

    def comprarDolares(self,data):
        saldo = data.get("saldoEnCuenta")
        monto = data.get("monto")

        # Cambiar la tupla por Diccionario??
        if saldo >= monto:
            return {
                'estado': True,
                'razon': (
                    f"La Operacion De Compra Fue Exitosa",
                    f"Compra por un monto de ${monto}",
                )
            }
        else: 
            return {
                'estado':False,
                'razon': ( 
                    f"La Operacion De Compra Fue Rechazada",
                    f"Compra por un monto de ${monto}",
                    f"Se Recibio una Cantidad de $USD{0}",
                    f"Fondos insuficientes para llevar a cabo la operacion"
                )
            }

    def extraerEfectivo(self, data):
        cupoDiarioRestante = data.get("cupoDiarioRestante")
        monto = data.get("monto")

        if monto < cupoDiarioRestante:
            return {
                'estado': True,
                'razon': ('La extracción fue realizada con éxito'),
            }
        else: 
            return {
                'estado': False,
                'razon': ('Fondos insuficientes para llevar a cabo la extracción'),
            }

    def tranferenciaRecibida(self, data):
        monto = data.get("monto")
        limiteTransferenciaRecibida = self._limite_transferencia_recibida

        if monto <  limiteTransferenciaRecibida:
            return {
                'estado': True,
                'razon': ('La transferencia fue reacibida con éxito'),
            }
        else:
            return {
                'estado': False,
                'razon': (
                    'La transferencia no fue recibida',
                    'El monto excede el límite de su cuenta',
                    'Debe solicitar autorización al banco para recibir la transferencia'
                ),
            }
    
    def transferenciaEnviada(self, data):
        monto = data.get("monto")
        cupoDiarioRestante = data.get("cupoDiarioRestante")
        costoTransferencias = self._costo_transferencias

        if monto < (cupoDiarioRestante + costoTransferencias):
            return {
                'estado': True,
                'razon': ('La transferencia fue enviada con éxito'),
            }
        else: 
            return {
                'estado': False,
                'razon': (
                    'La transferencia no fue enviada',
                    'El monto excede el saldo de su cuenta',
                ),
            }

    def altaTarjeta(cliente, evento):
        tarjetasActuales = evento.get('totalTarjetasDeCreditoActualmente')
        maxTarjetasPosibles = cliente.getTarjetaCredito()
        if cliente.puede_crear_tarjeta_credito():
            if tarjetasActuales < maxTarjetasPosibles:
                return {
                    'estado': True, 
                    'razon': ('La tarjeta de credito fue creada exitosamente') 
                }                 
            else:
                return {
                    'estado': False, 
                    'razon': (f'Ya tienes {maxTarjetasPosibles} tarjetas de credito', 'No puedes crear otra')
                }
        else: 
            return { 
                'estado': True, 
                'razon': ('No puedes crear tarjeta de credito')
            }

    def razonAltaChequera(cliente, evento):
        chequerasActuales = evento.get('totalChequerasActualmente')
        maxChequerasPosibles = cliente.getChequeras()
        if cliente.puede_crear_chequeras():
            if chequerasActuales < maxChequerasPosibles:
                return {
                    'estado': True,
                    'razon': ('La chequera fue creada exitosamente')
                }
            else:
                return {
                    'estado': False, 
                    'razon': (f'Ya tienes {maxChequerasPosibles} chequeras', 'No puedes crear otra')
                }
                 
        else:
            return { 
                'estado': False, 
                'razon': ('No puedes crear chequeras')
            }
