from Combustivel import Combustivel
from Veiculo import Veiculo
from Abastecimento import Abastecimento

# ==========================================
# COMBUSTÍVEIS
# ==========================================
etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")

# ==========================================
# VEÍCULOS
# ==========================================
carro = Veiculo("Carro", "ABC-1234")
moto = Veiculo("Moto", "DEF-5678")
van = Veiculo("Van Escolar", "GHI-9012")
barco = Veiculo("barco", "ABC-1234")
caminhao = Veiculo("caminhão", "ABC-1234")
aviao = Veiculo("avião", "ABC-1234")
caminhonete = Veiculo("caminhonete", "ABC-1234")
triciclo = Veiculo("triciclo", "ABC-1234")

# ==========================================
# ABASTECIMENTOS
# ==========================================
abastecimento1 = Abastecimento(carro,etanol,50)
abastecimento2 = Abastecimento(moto,gasolina,25)
abastecimento3 = Abastecimento(van,diesel,200)
abastecimento4 = Abastecimento(barco,diesel,100)
abastecimento5 = Abastecimento(caminhao,diesel,200)
abastecimento6 = Abastecimento(aviao,gasolina,500)
abastecimento7 = Abastecimento(caminhonete,diesel,150)
abastecimento8 = Abastecimento(triciclo,etanol,50)


# ==========================================
# LISTA DE ABASTECIMENTOS
# ==========================================
abastecimentos = [abastecimento1, abastecimento2, abastecimento3,abastecimento4, abastecimento5, abastecimento6, abastecimento7, abastecimento8]

# ==========================================
# MOSTRANDO OS ABASTECIMENTOS
# ==========================================
print("========== ABASTECIMENTOS DO DIA ==========")

for abastecimento in abastecimentos:
    abastecimento.mostrar_abastecimento()

# ==========================================
# TOTAL DE VENDAS POR COMBUSTÍVEL
# ==========================================
total_etanol = 0
total_gasolina = 0
total_diesel = 0

for abastecimento in abastecimentos:
    if abastecimento.combustivel.nome == "Etanol":
        total_etanol += abastecimento.valor
    elif abastecimento.combustivel.nome == "Gasolina":
        total_gasolina += abastecimento.valor
    elif abastecimento.combustivel.nome == "Diesel":
        total_diesel += abastecimento.valor

# ==========================================
# TOTAL DO DIA
# ==========================================
total_dia = (total_etanol + total_gasolina + total_diesel)

print("=============================Aluno:===============================")


texto = ""
combustiveis_abastecidos = []

for i in abastecimentos:
    texto +=   (f"{i.veiculo.modelo} - {i.veiculo.placa}\n"
                f"Combustível: {i.combustivel}\n"
                f"Valor: R${i.valor}\n\n")

with open("abastecimentos.txt", "w",encoding="utf-8") as arquivo:
    arquivo.write("========== POSTO DE GASOLINA ==========\n")
    arquivo.write(texto)
    arquivo.write("========================================\n")
    arquivo.write(f"Etanol: R${total_etanol:.2f}\n"
                  f"Gasolina: R${total_gasolina:.2f}\n"
                  f"Diesel: R${total_diesel:.2f}\n"
                  f"TOTAL DO DIA:{total_dia:.2f}\n")


