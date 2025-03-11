import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

class VistaCuentaTkinter:
    def __init__(self, controlador):
        self.controlador = controlador  # Pasamos el controlador
        self.ventana = tk.Tk()
        self.ventana.title("Cuenta Bancaria")

        # Crear etiqueta para mostrar el saldo
        self.label_saldo = tk.Label(self.ventana, text="Saldo: $0", font=("Arial", 14))
        self.label_saldo.pack(pady=10)

        # Botón para depositar dinero
        self.boton_depositar = tk.Button(self.ventana, text="Depositar", width=20, command=self.depositar)
        self.boton_depositar.pack(pady=5)

        # Botón para retirar dinero
        self.boton_retirar = tk.Button(self.ventana, text="Retirar", width=20, command=self.retirar)
        self.boton_retirar.pack(pady=5)

        # Botón para consultar el saldo
        self.boton_consultar_saldo = tk.Button(self.ventana, text="Consultar Saldo", width=20, command=self.consultar_saldo)
        self.boton_consultar_saldo.pack(pady=5)

        # Botón para salir
        self.boton_salir = tk.Button(self.ventana, text="Salir", width=20, command=self.salir)
        self.boton_salir.pack(pady=5)

    def depositar(self):
        self._solicitar_cantidad("depositar")

    def retirar(self):
        self._solicitar_cantidad("retirar")

    def _solicitar_cantidad(self, accion):
        cantidad = self._obtener_cantidad()
        if cantidad is not None and cantidad > 0:
            mensaje = self.controlador.procesar_transaccion(accion, cantidad)
            messagebox.showinfo("Resultado", mensaje)
            self.consultar_saldo()  # Actualizar el saldo en la GUI
        else:
            messagebox.showerror("Error", "Cantidad inválida. Inténtalo de nuevo.")

    def consultar_saldo(self):
        saldo = self.controlador.obtener_saldo()
        self.label_saldo.config(text=f"Saldo: ${saldo}")

    def salir(self):
        self.ventana.quit()

    def _obtener_cantidad(self):
        # Pedimos al usuario la cantidad mediante un cuadro de entrada
        entrada = simpledialog.askstring("Cantidad", "Ingresa la cantidad:")
        try:
            return float(entrada) if entrada else None
        except ValueError:
            return None

    def ejecutar(self):
        self.ventana.mainloop()  # Inicia el bucle de la ventana
