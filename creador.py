import webbrowser
def creador(datos):
    archivo= open('index.html','w')
    
    datosCliente='<div class="cliente">'
    for infoClient in datos.get('cliente'):
        datosCliente+=f"<p>{infoClient}</p>"
    datosCliente+='</div>'

    datosDireccion ='<div class="direccion">'
    for infoDireccion in datos.get('direccion'):
        datosDireccion +=f"<p>{infoDireccion} </p>"
    datosDireccion +='</div>'
    
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
            
        </style>
    </head>
    """ + f"""
    <body>
    {datosCliente}{datosDireccion}
    {datos}
    </body>
    </html>
    """
    )

    webbrowser.open('index.html')
    archivo.close()