class FooBarChecker:
    """
    Clase que contiene la lógica para verificar si un número es divisible
    por 3, 5 o ambos, y devuelve el resultado correspondiente.
    """
    
    def checkNumber(self, number: int) -> str:
        """
        -Devuelve "Foo" si es divisible por 3\n 
        -Devuelve "Bar" si es divisible por 5\n
        -Devuelve "FooBar" si es divisible por ambos\n
        -Devuelve el numero mismo si no es divisible por ninguno,
        
        Args:
            number (int): El número a verificar.
        
        Returns:
            str: El resultado de la verificación.
        """
        if number % 3 == 0 and number % 5 == 0:
            return "FooBar"
        elif number % 3 == 0:
            return "Foo"
        elif number % 5 == 0:
            return "Bar"
        else:
            return str(number)

class FooBarTest:
    """
    Clase que contiene los casos de prueba para la lógica de FooBarChecker.
    """

    def runTest(self):
        """
        Ejecuta los casos de prueba para verificar que el comportamiento del
        programa sea el esperado.
        """
        checker = FooBarChecker()

        #Casos de Prueba para realizar el test de la funcion:

        #Argumentos brindados 
        testCases = [1, 3, 5, 15, 23, 30, 45] 
        #Resutlados esperados
        expectedResults = ["1", "Foo", "Bar", "FooBar", "23", "FooBar", "FooBar"]


        #Se ejecuta la funcion para cada caso de prueba, y se valida si el resultado es el que se espera
        print("Ejecutando pruebas...")
        for i, test_case in enumerate(testCases):
            result = checker.checkNumber(test_case)
            assert result == expectedResults[i], f"Caso fallido para el registro {test_case}: estaba esperando el valor {expectedResults[i]}, la funcion dio como retorno {result}"
        print("Todos los test Pasaron")


if __name__ == "__main__":

    # Ejecutar los casos de prueba para validar el funcionamiento del programa
    tester = FooBarTest()
    tester.runTest()

    # Solicitar un número al usuario
    n = int(input("Introduce un número entero positivo: "))
    
    # Crear una instancia de FooBarChecker y mostrar el resultado
    checker = FooBarChecker()
    print(checker.checkNumber(n))
