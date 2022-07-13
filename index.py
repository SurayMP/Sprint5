import json
if __name__=='__main__':
    # from clases.clientes import Cliente
    # Arrastrar y soltar archivo json
    ArchivoArrastrado=input('Arrastre El Archivo Json con la Informacion y Presione Enter \n : ')
    try:
        archivo = open(ArchivoArrastrado,'r')
        # La Variable Data tiene la info del archivo
        data=json.load(archivo)
        archivo.close()
    except Exception as error:
        print("Un Error A Ocurrido con el Archivo Proporcionado")
        # print(error)
