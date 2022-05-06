distância = float(input("Qual é a distância da sua Viagem? "))
print("Você está prestes a começar uma viagem de {}km" .format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print("O preço da sua passagem será de {:.2f}" .format(preço))