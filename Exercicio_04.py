def porcentagem (valor_total, valor_estado):
    valor_estado = (valor_estado/valor_total)*100
    return valor_estado

faturamento = {
"sp": 67836.43,
"rj": 36678.66,
"mg": 29229.88,
"es": 27165.48,
"outros": 19849.53
}

estado = ""
valor_total = sum(faturamento.values())

for estado in faturamento:
    print(f'{estado} {porcentagem(valor_total, faturamento[estado]):.0f}')