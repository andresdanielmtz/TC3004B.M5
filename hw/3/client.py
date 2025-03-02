from factory.ComputerFactoryClass import ComputerFactory


class Client():
    
    @staticmethod
    def client_code(LaptopFactory: ComputerFactory):
        laptop = LaptopFactory.create_laptop()
        desktop = LaptopFactory.create_desktop()
        handheld = LaptopFactory.create_handheld()

        laptop.boot()
        laptop.show_battery()
        desktop.boot()
        handheld.boot()
        handheld.show_battery()