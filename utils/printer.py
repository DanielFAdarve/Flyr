from datetime import datetime, timedelta
from colorama import Fore, Back, init

# region - Library or class imports

class Printer:
    """
        Impresor
        ========
        Esta clase se encargará de imprimir mensajes en consola
        para el seguimiento del aplicativo, en la etapa de desarrollo.
        ### `Usos:`
        - Depurar a través de print el código
        - Imprimir variables necesarias para el desarrollo
    """
    
    def __init__(self):
        """
            Constructor de la clase `Impresor`, donde se inicializan
            las variables de la clase.
        """
        init()  # Se inicializa el modulo de Colorama.
        self.__currentTime = ""
    
    def getCurrentTime(self):
        return self.__currentTime
    
    def setCurrentTime(self, currentTime):
        self.__currentTime = currentTime
        
    # Region - Metodos en la clase
    
    def printStart(self, appName):
        """
            Metodo encargado de imprimir en consola el
            inicio de la ejecución del proyecto
        Args:
            nombreApp (str): Nombre del proyecto o de la aplicación
        """
        self.setCurrentTime((datetime.today() - timedelta(hours=0)).strftime('%Y-%m-%d %H:%M:%S'))
        data = "============================================================================================================================\n"
        data += "| INICIO DE APLICACION --> ["+ str(appName) +"] Hora de ejecucion: " + str(self.getCurrentTime()) + " |\n"
        data += "============================================================================================================================\n"
        print(data)
    
    def printProcess(self, process):
        """
            Metodo usado para imprimir la tarea o función
            que se esta ejecutando en el proceso.
        Args:
            proceso (str): Nombre de la función
        """
        self.setCurrentTime((datetime.today() - timedelta(hours=0)).strftime('%Y-%m-%d %H:%M:%S'))
        data = "============================================================================================================================\n"
        data += "| Ejecutando la tarea --> ["+ str(process) +"]\n"
        data += "| Hora de ejecucion: " + str(self.getCurrentTime()) + "\n"
        data += "============================================================================================================================\n"
        print(data)
    
    def printComment(self, process: str, comment: str):
        """
            Metodo usado para imprimir la tarea o función
            que se esta ejecutando en el proceso.
        `Args:`
            `proceso (str):` Nombre de la función del llamado
            `comentario (str):` Comentario que se desea imprimir
        """
        self.setCurrentTime((datetime.today()).strftime('%Y-%m-%d %H:%M:%S'))
        data = "|==========================================================================================================================|\n"
        data += f"| Tarea: [{process}] <==> {comment}|\n"
        data += f"| Hora de ejecución: ({self.getCurrentTime()}) |\n"
        data += "|==========================================================================================================================|\n"
        print(data)
    
    def printEnd(self):
        """
            Metodo usado para imprimir la hora
            en la que se termino de ejecutar el proceso
        """
        self.setCurrentTime((datetime.today() - timedelta(hours=0)).strftime('%Y-%m-%d %H:%M:%S'))
        data = "============================================================================================================================\n"
        data += "| FINALIZACION DE APLICACION | Hora de ejecucion: " + str(self.getCurrentTime()) + "\n"
        data += "============================================================================================================================\n"
        print(data)
    
    def printError(self, error):
        """
            Metodo para imprimir un posible error identificado
            durante la ejecución del proceso
        Args:
            error (str): Variable contenedora del error.
        """
        self.setCurrentTime((datetime.today() - timedelta(hours=0)).strftime('%Y-%m-%d %H:%M:%S'))
        data = "============================================================================================================================\n"
        data += "| Error en ejecución| Hora del error: " + str(self.getCurrentTime()) + "\n"
        data += "| ERROR: " + error + "\n"
        data += "============================================================================================================================\n"
        print(data)
        
    def printErrorColor(self, title: str, error: str) -> None:
        """
        Este metodo imprimira un mensaje de error en 
        consola, con una configuración de color RED
        de manera que sea visible dentro de los demás
        mensajes impresos en la consola.
        - `Args:`
           -  `titulo (str):` Titulo o nombre del metodo donde se generá el error.
           -  `error (str):` Mensaje del error, descriptivo, más variable del error.
        - `Usos:`
            - Informar sobre un posible error critico en un proceso.
        """
        self.setCurrentTime((datetime.today() - timedelta(hours=0)).strftime('%Y-%m-%d %H:%M:%S'))
        message = Back.LIGHTRED_EX + Fore.LIGHTRED_EX + "============================================================================================================================\n" + Back.RESET + Fore.RESET
        message += Fore.RED + f"| [{title}] - [{self.getCurrentTime()}] | \n" + Fore.RESET
        message += Fore.WHITE + f"| {error} | \n" + Fore.RESET
        message += Back.LIGHTRED_EX + Fore.LIGHTRED_EX + "============================================================================================================================\n" + Back.RESET + Fore.RESET
        print(message)
    
    def printInfoColor(self, title: str, data: str) -> None:
        """
        Este metodo podrá ser usado para multiples propositos
        por ejemplo, para imprimir en consola, el inicio del tratado
        de un proceso especifico, o para validar la información de
        un metodo que se este ejecutando. Se imprimirá en Azul.
        - `Args:`
           -  `titulo (str):` Titulo del mensaje a mostrar -> [Titulo - Fecha (Y-m-d H-M-S)].
           -  `data (str):` Mensaje que se desea mostrar en consola, siendo descriptivo.
        - `Usos:`
            - Para indicar la finalización del tratado de un proceso.
            - Para informar sobre el inicio de una función.
        """
        self.setCurrentTime((datetime.today() - timedelta(hours=0)).strftime('%Y-%m-%d %H:%M:%S'))
        message = f"{Back.LIGHTBLUE_EX}{Fore.LIGHTBLUE_EX}============================================================================================================================\n{Back.RESET}{Fore.RESET}"
        message += f"{Fore.BLUE}| [{title}] - [{self.getCurrentTime()}] | { Fore.RESET}\n"
        message += f"{Fore.WHITE}| {data} | {Fore.RESET}\n"
        message += f"{Back.LIGHTBLUE_EX}{Fore.LIGHTBLUE_EX}============================================================================================================================\n{Back.RESET}{Fore.RESET}"
        print(message)
    
    def printWarnColor(self, title: str, data: str) -> None:
        """
        Con este metodo, imprimiremos en consola aquellos
        mensajes de advertencia de lo que sucede en el proceso
        de manera que podremos identificar aquel falla no
        critica en el mismo. Se imprimira en Amarillo
        - `Args:` 
           -  `titulo (str):` Titulo del mensaje a mostrar -> [Titulo - Fecha (Y-m-d H-M-S)].
           -  `data (str):` Mensaje que se desea mostrar en consola, siendo descriptivo.
        - `Usos:`
            - Advertir de un posible error, que no afectaría del todo la ejecución del proceso.      
        """
        self.setCurrentTime((datetime.today() - timedelta(hours=0)).strftime('%Y-%m-%d %H:%M:%S'))
        message = f"{Back.LIGHTYELLOW_EX}{Fore.LIGHTYELLOW_EX}============================================================================================================================\n{Back.RESET}{Fore.RESET}"
        message += f"{Fore.YELLOW}| [{title}] - [{self.getCurrentTime()}] | { Fore.RESET}\n"
        message += f"{Fore.WHITE}| {data} | {Fore.RESET}\n"
        message += f"{Back.LIGHTYELLOW_EX}{Fore.LIGHTYELLOW_EX}============================================================================================================================\n{Back.RESET}{Fore.RESET}"
        print(message)
