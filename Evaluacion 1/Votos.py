#clase que contiene listas vacias y una lista con contenido
class Votaciones:
    def __init__(self):  #Aqui el self sirve como nombre para el primer parametro de la clase. y el __init__ sirve para iniciar la clase que cree anterioramente
        self.votantesAdmitidos = [] #listas vacias 
        self.votantesRechazados = []
        self.candidatos = ["juanita", "daniel", "soraya", "voto en blanco"]
        self.contadorVotos = 0 #contadores
        self.contadorVotosR = 0

    def ingresoVotantes(self):
        continuarIngreso = True 
 #creamos un ciclo para validar que digiten el candidato que este en la lista
        while continuarIngreso:
            #Datos a pedir y guardar
            nombre = input("Ingresa su nombre: ")
            id = int(input("Ingrese su id: "))
            print(f"Lista de candidatos {self.candidatos}")
            voto = input("Ingrese  su voto (recuerde que hay ¡voto en blanco!): ").lower() #.lower() Para volver las letras en minuscula

            #verificamos que escriban el candidato correpto 
            if  voto and self.candidatos in self.candidatos:
                print("Gracias por Votar")
                self.votantesAdmitidos.append(f"Nombre Aprediz: {nombre}, id: {id}, Su voto a sido: {voto}")
                self.contadorVotos += 1
                #No cumplieron con lo requerrido
            else:
                print("Lo siento no puedes votar")
                motivoRechazo = "no existe el canditado en el sistema"
                self.votantesRechazados.append(f"Aprendiz {nombre}, de ID: {id}, a votado por: {voto}, Motivo anulacion del voto: {motivoRechazo}")
                self.contadorVotosR += 1
                #Esto sirve que al finalizar el ingreso mande un reporte de los aprendices no admitidos y de los que si fueron admitidos, y hace tipo texto describiendo el voto que no fue admitido
            respuesta = input("¿Desea votar otro aprendiz diferente?(recuerda que un aprendiz no puede votar 2 veces) (si/no): ")
            continuarIngreso = respuesta.lower() == 'si' #Si digitan si el ciclo se repite 
            #Si digitan no el ciclo se cierra
            

    #generamos los reportes de los votos admitidos y nulos
    def generarReporte(self):
        print(f"\nReporte de aprendices que han votado:")
        for votante in self.votantesAdmitidos:
            print(votante)
        print("\nReporte de Asistentes Rechazados:")
        for asistente in self.votantesRechazados:
            print(asistente)
        #Aqui estos prints sirven para traer tipo el contador de los qvotos fueron rechados y los que fueron admitidos
        print(f"\nTotal de votos contabilizados: {self.contadorVotos}")
        print(f"Reporte votos anullados: {self.contadorVotosR}")

#Y aqui serian los cierres del codigo

votos = Votaciones()
votos.ingresoVotantes()
votos.generarReporte()