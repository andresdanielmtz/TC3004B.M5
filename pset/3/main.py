from client import Client
from factory.ASUSFactoryClass import ASUSFactory
from factory.HPFactoryClass import HPFactory


def main():
    clientInstance = Client()

    print("\n Client (ASUS): \n")
    clientInstance.client_code(ASUSFactory())
    

    print("\n Client (HP): \n")
    clientInstance.client_code(HPFactory())


if __name__ == "__main__":
    main()
