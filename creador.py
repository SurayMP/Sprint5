import string
import webbrowser
def creador(datos):
    archivo= open('index.html','w')
    
    datosCliente='<div class="cliente">'
    for i,infoClient in enumerate(datos.get('cliente')):
        if(i==3):
            datosCliente+=f"<p>Numero: {infoClient}</p>"
        elif i==2:
            datosCliente+=f"<p>Dni: {infoClient}</p>"
        elif i==1:
            datosCliente+=f"<p>Apellido: {infoClient}</p>"
        elif i==0:
            datosCliente+=f"<p>Nombre: {infoClient}</p>"
    datosCliente+='</div>'

    datosDireccion ='<div class="direccion">'
    for infoDireccion in datos.get('direccion'):
        datosDireccion +=f"<p>{infoDireccion} </p>"
    datosDireccion +='</div>'


    datosRazones ='<div class="razones">'
    for infoRazones in datos.get('razones'):
        fecha ='<p class="medium"> FECHA: '+ str(infoRazones.get('fecha')) +'</p>'
        monto = '<p class="medium"> MONTO:$'+ str(infoRazones.get('monto'))+'</p>'
        tipo = '<p class=""> TIPO: '+ str(infoRazones.get('tipo'))+'</p>'
        estado = ('<p class="aceptado">ACEPTADO' if infoRazones.get('estado') else '<p class="rechazado">RECHAZADO') + '</p>'
        razonText= estado + tipo + monto  + fecha 

        # print(infoRazones.get('razon'))
        for razon in infoRazones.get('razon'):
            razonText+=f"<p>{razon}</p>"


        datosRazones +=f"""<div class='razon'>{razonText}</div>"""
    datosRazones +='</div>'
    
    archivo.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
         <style>
              *{
                font-family: Arial, Helvetica, sans-serif;
                
                color: rgb(231, 231, 231);
            }
            body{
                background-color: rgb(26, 26, 26);
            }
            .cliente{
                font-size: 1.2rem;
                font-weight: 600;
            }
            .cliente p,
            .direccion p
            {
                margin: .5px;
            }
            .direccion{
                font-size: .8rem;
            }
            .razones{
                
                
            }
            .razon{
                color: rgb(223, 223, 223);
                background-color: rgb(41, 41, 41);
                margin: 5px;
                border-radius: 5px;
            }
            .razon .aceptado{
                color: green;
            }
            .razon .rechazado{
                color: red;
            }
            .razon p{
                margin: 4px;
            }
            .medium{
                font-size: .8rem;
            }
        </style>
    </head>
    """ + f"""
    <body>
    {datosCliente}{datosDireccion}
    {datosRazones}
    </body>
    </html>
    """
    )

    webbrowser.open('index.html')
    archivo.close()