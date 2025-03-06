import json

with open("faturamento.json", "r") as file:
    dados = json.load(file)

fatu_diario = [dia["valor"] for dia in dados if dia["valor"] > 0]

if fatu_diario:
    menor = min(fatu_diario)
    maior = max(fatu_diario)
    media_m = sum(fatu_diario) / len(fatu_diario)

    dias_acima_da_media = sum(1 for valor in fatu_diario if valor > media_m)

    print(f"Menor faturamento diário: R$ {menor:.2f}")
    print(f"Maior faturamento diário: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
else:
    print("Não há dados válidos para calcular o faturamento.")