class Direccion:
    def __init__(self, data) -> None:
        self.calle = data.get('calle')
        self.numero= data.get('numero')
        self.ciudad= data.get('ciudad')
        self.provincia= data.get('provincia')
        self.pais= data.get('pais')

    def __str__(self) -> str:
        return f"""\n
        {self.numero}{self.calle}\n
        {self.ciudad}\n
        {self.provincia}\n
        {self.pais}\n"""
    def getDireccion(self):
        return (
        f"{self.numero} {self.calle}",
        f"{self.ciudad}",
        f"{self.provincia} {self.pais}")