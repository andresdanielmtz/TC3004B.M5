"""
Example of Builder Design Pattern.
Andrés Martínez - A00227463
"""


class Computer:
    def __init__(self, cpu, ram, storage, gpu):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    # We can check if any prop is not implemented.
    def displaySystem(self):
        print(f"cpu: {self.cpu} \nram: {self.ram} \nstorage: {self.storage}gb \ngpu: {self.gpu or "No GPU"}")
    
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer(None, None, None, None) # all values = null
    
    def setRam(self, ram):
        self.computer.ram = ram
        return self
    
    def setCPU(self, cpu):
        self.computer.cpu = cpu 
        return self
    
    def setGPU(self, gpu):
        self.computer.gpu = gpu
        return self
    
    def setStorage(self, storage):
        self.computer.storage = storage
        return self
    
    def build(self):
        return self.computer
    
def main():
    basicComputer = ComputerBuilder().setRam(2).setStorage(10).setCPU(200).setGPU("gtx 1050ti").build()
    basicComputer.displaySystem()

if __name__ == "__main__":
    main()