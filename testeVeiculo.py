# Testando a classe veículo
from veiculo import Veiculo

# Criação e instância do objeto da classe veículo
minhaCaranga = Veiculo('147', 'Fiat', 'Amarelo', 0)

# Acelerar a minha caranga
for cont in range(1, 151):
    minhaCaranga.acelerar()

# Exibir a minha caranga
print(minhaCaranga)