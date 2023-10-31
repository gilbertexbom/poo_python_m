class Veiculo(object):
    def __init__(self, marca, modelo, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setCor(self, cor):
        self.cor = cor

    def getCor(self):
        return self.cor

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade

    def getVelocidade(self):
        return self.velocidade

    def __str__(self):
        return "\n Marca: " + self.marca + "\nModelo: " +self.modelo+ "\nCor: " +self.cor+ "\nVelocidade: " +str(self.velocidade)+ "km/h\n"

    def acelerar(self):
        if self.velocidade < 120:
            self.velocidade = self.getVelocidade() + 1



