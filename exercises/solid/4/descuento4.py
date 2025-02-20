from abc import ABC, abstractmethod

# Aqui se puede observar la interfaz de descuento
class DescuentoStrategy(ABC):
    @abstractmethod
    def aplicar_descuento(self, am: float) -> float:
        pass

    @abstractmethod
    def obt_descuento_porcentaje(self) -> float:
        pass

# Implementaciones de descuentos
class NoDescuento(DescuentoStrategy):
    def aplicar_descuento(self, am: float) -> float:
        return am
    
    def obt_descuento_porcentaje(self) -> float:
        return 0.0

class VIPDescuento(DescuentoStrategy):
    def aplicar_descuento(self, am: float) -> float:
        return am * 0.9  # 10% de descuento
    
    def obt_descuento_porcentaje(self) -> float:
        return 10.0

class SeasonalDescuento(DescuentoStrategy):
    def aplicar_descuento(self, am: float) -> float:
        return am * 0.8  # 20% de descuento
    
    def obt_descuento_porcentaje(self) -> float:
        return 20.0

# Aqui procesamos el pago
class PagoProcessor:
    def __init__(self, descuento_strategy: DescuentoStrategy):
        self.descuento_strategy = descuento_strategy
    
    def process_pago(self, am: float) -> float:
        descuentoed_am = self.descuento_strategy.aplicar_descuento(am)
        descuento_porcentaje = self.descuento_strategy.obt_descuento_porcentaje()
        print(f"Descuento aplicado: {descuento_porcentaje}%")
        print(f"Monto con descuento: ${descuentoed_am:.2f}")
        return descuentoed_am

# ejemplo de uso
def main():
    am = 1000  # Monto de ejemplo
    
    print("\nPago sin descuento:")
    print(f"Monto original: ${am:.2f}")
    
    print("\nPago con descuento VIP:")
    vip_descuento_pago = PagoProcessor(VIPDescuento())
    vip_descuento_pago.process_pago(am)
    
    print("\nPago con descuento de temporada:")
    seasonal_descuento_pago = PagoProcessor(SeasonalDescuento())
    seasonal_descuento_pago.process_pago(am)

if __name__ == "__main__":
    main()

