class Laptop:
    def __init__(self, cpu, ram = 4096, price = 2000, gpu = "AMD"):
        self.setCpu(cpu)
        self.setRam(ram)
        self.price = price
        self.gpu = gpu


    def setCpu(self, cpu):
        if cpu.lower() == "amd" or cpu.lower() == "intel" or cpu.lower() == "arm":
            self.cpu = cpu
        else:
            self.cpu = "unknown"


    def setRam(self, ram):
        if type(ram) == int and ram >= 2048:
            self.ram = ram
        else:
            self.ram = 2048

    def printData(self):
        print(self.cpu, self.ram, self.gpu, self.price)

laptop1 = Laptop("Intel", 2048)
laptop1.printData()