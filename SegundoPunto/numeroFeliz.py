class NumeroFeliz:
    """
    Clase que contiene la lógica para determinar si un número es feliz o no.
    """

    def esFeliz(self, numero: int) -> bool:
        """
        Determina si un número dado es feliz. Un número es feliz si al reemplazarlo
        repetidamente con la suma de los cuadrados de sus dígitos eventualmente llega
        a 1. Si entra en un ciclo que no incluye el 1, no es feliz.
        
        Args:
            numero (int): El número entero positivo a verificar.
        
        Retunrs:
            bool: True si el número es feliz, False en caso contrario.
        """
        numeros_vistos = set()  # Usamos un conjunto para detectar ciclos

        while numero != 1 and numero not in numeros_vistos:
            numeros_vistos.add(numero)
            numero = self._sumaCuadradosDigitos(numero)

        return numero == 1

    def _sumaCuadradosDigitos(self, numero: int) -> int:
        """
        Calcula la suma de los cuadrados de los dígitos de un número dado.

        Args:
            numero (int): El número entero cuyos dígitos se sumarán al cuadrado.

        Returns:
            int: La suma de los cuadrados de los dígitos del número.
        """
        return sum(int(digito) ** 2 for digito in str(numero))


class TestNumeroFeliz:
    """
    Clase que contiene los casos de prueba para verificar si la lógica de 'NumeroFeliz' funciona correctamente.
    """

    def __init__(self):
        self.numero_feliz = NumeroFeliz()  

    def numeroFelizTest(self):
        """
        Ejecuta los casos de prueba para validar si el programa funciona correctamente.
        """
        casos_de_prueba = [19, 4, 7, 28, 100]  # Lista de números a probar
        resultados_esperados = [True, False, True, True, True]  # Resultados esperados para cada caso

        print("Ejecutando pruebas...")
        for i, caso in enumerate(casos_de_prueba):
            resultado = self.numero_feliz.esFeliz(caso)
            assert resultado == resultados_esperados[i], f"Prueba fallida para {caso}: se esperaba {resultados_esperados[i]}, pero se obtuvo {resultado}"
        
        print("¡Todas las pruebas pasaron correctamente!")


if __name__ == "__main__":
    # Instanciar y ejecutar las pruebas
    tester = TestNumeroFeliz()
    tester.numeroFelizTest()

    # Solicitar número al usuario y verificar si es feliz
    numero_usuario = int(input("Introduce un número entero positivo: "))
    checker = NumeroFeliz()
    esFeliz = checker.esFeliz(numero_usuario)
    
    if esFeliz:
        print(f"El número {numero_usuario} es un número feliz.")
    else:
        print(f"El número {numero_usuario} no es un número feliz.")
