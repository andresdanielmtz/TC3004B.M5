from factory.ComputerFactoryClass import ComputerFactory


class Client:

    @staticmethod
    def client_code(LaptopFactory: ComputerFactory):

        # Will do an advertisement if it has the function for it. Currently only ASUS does.
        if hasattr(LaptopFactory, "advertisement"):
            LaptopFactory.advertisement()

        # Will show a number from 5o to 120 of how many countries does it operate in. CUrrently only HP has this specific function.
        if hasattr(LaptopFactory, "getData"):
            LaptopFactory.getData()

        laptop = LaptopFactory.create_laptop()
        desktop = LaptopFactory.create_desktop()
        handheld = LaptopFactory.create_handheld()

        laptop.boot()
        laptop.show_battery()
        desktop.boot()
        handheld.boot()
        handheld.show_battery()
