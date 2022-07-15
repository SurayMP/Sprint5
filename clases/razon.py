class Razon:


    type: str

    def __init__(self):
        self.type = ''

    def resolver(cliente, evento):
        return ''

class RazonAltaChequera(Razon):

    def __init__(self):
        self.type = 'ALTA_CHEQUERA'

    '''
        implementar resolver segun los casos de negocio
    '''

class RazonAltaTarjetaCredito(Razon):

    def __init__(self):
        self.type = 'ALTA_TARJETA_CREDITO'

    '''
        implementar resolver segun los casos de negocio
    '''

class RazonCompraDolar(Razon):

    def __init__(self):
        self.type = 'COMPRAR_DOLAR'

    '''
        implementar resolver segun los casos de negocio
    '''

class RazonRetiroEfectivo(Razon):

    def __init__(self):
        self.type = 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO'

    '''
        implementar resolver segun los casos de negocio
    '''

class RazonTransferenciaEnviada(Razon):

    def __init__(self):
        self.type = 'TRANSFERENCIA_ENVIADA'

    '''
        implementar resolver segun los casos de negocio
    '''

class RazonTransferenciaRecibida(Razon):

    def __init__(self):
        self.type = 'TRANSFERENCIA_RECIBIDA'

    '''
        implementar resolver segun los casos de negocio
    '''


