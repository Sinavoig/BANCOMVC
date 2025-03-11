class VistaCuenta:
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

    @staticmethod
    def mostrar_menu():
        print("\n--- Menú ---")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("4. Salir")

    @staticmethod
    def obtener_opcion():
        return input("Elige una opción: ")

    @staticmethod
    def obtener_cantidad():
        try:
            return float(input("Ingresa la cantidad: "))
        except ValueError:
            return None