class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Has depositado ${cantidad}. Saldo actual: ${self.saldo}"
        return "Cantidad inválida. Inténtalo de nuevo."

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return "Fondos insuficientes."
        elif cantidad > 0:
            self.saldo -= cantidad
            return f"Has retirado ${cantidad}. Saldo actual: ${self.saldo}"
        return "Cantidad inválida. Inténtalo de nuevo."

    def consultar_saldo(self):
        return f"Tu saldo actual es: ${self.saldo}"