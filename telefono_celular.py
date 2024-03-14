class TelefonoCelular:


    def __init__(self, marca, modelo, numero_telefono):
        """
        Constructor de la clase TelefonoCelular.


        Parámetros:
            marca (str): La marca del teléfono celular.
            modelo (str): El modelo del teléfono celular.
            numero_telefono (str): El número de teléfono del celular.
        """
        self.marca = marca
        self.modelo = modelo
        self.numero_telefono = numero_telefono


    def llamar(self, numero_destino):
        """
        Realiza una llamada al número de teléfono especificado.


        Parámetros:
            numero_destino (str): El número de teléfono al que se desea llamar.
        """
        print(f"Llamando al número {numero_destino}...")


    def enviar_mensaje(self, numero_destino, mensaje):
        """
        Envía un mensaje de texto al número de teléfono especificado.


        Parámetros:
            numero_destino (str): El número de teléfono al que se desea enviar el mensaje.
            mensaje (str): El mensaje de texto que se desea enviar.
        """
        print(f"Enviando mensaje al número {numero_destino}: {mensaje}")


    def tomar_foto(self):
        """
        Toma una foto con la cámara del teléfono celular.
        """
        print("Tomando una foto...")


    def grabar_video(self):
        """
        Graba un video con la cámara del teléfono celular.
        """
        print("Grabando un video...")


    def acceder_internet(self):
        """
        Accede a internet mediante el navegador web del teléfono celular.
        """
        print("Accediendo a internet...")


    def instalar_aplicacion(self, nombre_aplicacion):
        """
        Instala una aplicación desde la tienda de aplicaciones del teléfono celular.


        Parámetros:
            nombre_aplicacion (str): El nombre de la aplicación que se desea instalar.
        """
        print(f"Instalando la aplicación {nombre_aplicacion}...")


# Creamos una instancia de la clase TelefonoCelular
telefono = TelefonoCelular("Samsung", "Galaxy S23", "+64 9 11 22334455")


# Imprimimos la información del teléfono
print(f"Marca: {telefono.marca}")
print(f"Modelo: {telefono.modelo}")
print(f"Número de teléfono: {telefono.numero_telefono}")


# Realizamos una llamada
telefono.llamar("+64 9 11 66778899")


# Enviamos un mensaje de texto
telefono.enviar_mensaje("+64 9 11 66778899", "Hola, ¿cómo estás?")


# Tomamos una foto
telefono.tomar_foto()


# Grabamos un video
telefono.grabar_video()


# Accedemos a internet
telefono.acceder_internet()


# Instalamos una aplicación
telefono.instalar_aplicacion("WhatsApp")
