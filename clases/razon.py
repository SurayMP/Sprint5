Estados = {
    'ACEPTADA':True,
    'RECHAZADA':False,
}


class Razon:
    type: str

    def __init__(self):
        self.type = ''

    def resolver(self,cliente, evento):
        self.cliente=cliente
        self.evento = evento
        self.razonDatos = {
            'fecha':evento.get('fecha'),
            'monto':evento.get('monto'),
            'tipo':evento.get('tipo')
        }

        return 'Analisis'

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
        self.type = 'COMPRA_DOLAR'
        
    def resolver(self,cliente,evento):
        super().resolver(cliente,evento)
        if self.cliente.puede_comprar_dolar():
            self.razonDatos.update(self.cliente.cuenta.comprarDolares(self.evento))
            return self.razonDatos
        else:
            self.razonDatos.update({'estado':False,'razon':("El Cliente No Puede Comprar Dolares")})
            return self.razonDatos


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


Razones={
    'RETIRO_EFECTIVO_CAJERO_AUTOMATICO': RazonRetiroEfectivo,
    'ALTA_TARJETA_CREDITO': RazonAltaTarjetaCredito,
    'ALTA_CHEQUERA': RazonAltaChequera,
    'COMPRA_DOLAR': RazonCompraDolar,
    'TRANSFERENCIA_ENVIADA': RazonTransferenciaEnviada,
    'TRANSFERENCIA_RECIBIDA': RazonTransferenciaRecibida,
}
def RealizarOperacion(cliente,operacion):
    evento = operacion.get('tipo')
    razon = Razones.get(evento)()
    return razon.resolver(cliente,operacion)
    # estado = operacion.get('estado')

