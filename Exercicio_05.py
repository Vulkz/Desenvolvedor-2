palavra = "Gabriel"
palavra_invertida = ""


for index in range(len(palavra), 0, -1):
    palavra_invertida += palavra[index-1]

print(palavra_invertida)