from modelo import CuentaBancaria
from vista_tkinter import VistaCuentaTkinter  # Importa la nueva vista con Tkinter

class ControladorCuenta:
    def __init__(self):
        self.cuenta = CuentaBancaria()
        self.vista = VistaCuentaTkinter(self)  # Pasa el controlador a la vista gráfica

    def procesar_transaccion(self, accion, cantidad):
        # Procesar depósito o retiro
        if accion == "depositar":
            return self.cuenta.depositar(cantidad)
        elif accion == "retirar":
            return self.cuenta.retirar(cantidad)
        return "Acción no válida."

    def obtener_saldo(self):
        # Obtener el saldo actual
        return self.cuenta.saldo

    def ejecutar(self):
        # Ejecutar la aplicación
        self.vista.ejecutar()

if __name__ == "__main__":
    app = ControladorCuenta()
    app.ejecutar()
