import json
from clases.clientes import ClienteClassic,ClienteBlack,ClienteGold
Tipos={
    "BLACK":ClienteBlack,
    "GOLD":ClienteGold,
    "CLASSIC":ClienteClassic,
}


def createClient(data,client):
    # data es un diccionario con la info del cliente
    return client(data)

# def processClient():



if __name__=='__main__':
    ArchivoArrastrado=input('Arrastre El Archivo Json con la Informacion y Presione Enter \n : ')
    try:
        archivo = open(ArchivoArrastrado,'r')
        # La Variable Data tiene la info del archivo
        data=json.load(archivo)
        archivo.close()
        print(data)
        createClient(data,Tipos.get(data.get('tipo')))
        
    except Exception as error:
        print("Un Error A Ocurrido con el Archivo Proporcionado")

