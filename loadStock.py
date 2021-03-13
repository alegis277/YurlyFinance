import pandas as pd
import numpy as np

stock = {"CONCONCRET": [2175, 484], "PFAVAL": [648, 1172], "PFDAVVNDA": [16, 31360], 
		"PFBCOLOM": [33, 30630], "CEMARGOS": [183, 5470], "CNEC": [73, 10400]}

XLS_FILE = "https://www.bvc.com.co/mercados/DescargaXlsServlet?archivo=acciones&resultados=100"

df = pd.read_excel(XLS_FILE, header = 1)
df['Nemotecnico'] = df['Nemotecnico'].apply(lambda x: x.strip())




print("\nVARIATION IN EACH SHARE FROM BUY PRICE\n")
totalPortfolioOriginal = 0
totalPortfolioCurrent = 0
for key, value in stock.items():
	stringToPrint = key + ": "
	stringToPrint += str(float(value[1])) + " -> " + str(float(df.loc[df["Nemotecnico"] == key, "Ultimo Precio"]))

	diffPrice = float(df.loc[df["Nemotecnico"] == key, "Ultimo Precio"]) - float(value[1])
	stringToPrint += "  (" + ("+" if diffPrice>=0 else "-") + str(np.abs(diffPrice)) + ")"

	totalPortfolioOriginal += float(value[1] * value[0])
	totalPortfolioCurrent += float(df.loc[df["Nemotecnico"] == key, "Ultimo Precio"] * value[0])

	print(stringToPrint)

print("\nVARIATION IN PORTFOLIO\n")

stringToPrint = f'{totalPortfolioOriginal:,}' + " -> " + f'{totalPortfolioCurrent:,}'
diffPrice = totalPortfolioCurrent - totalPortfolioOriginal
stringToPrint += "  (" + ("+" if diffPrice>=0 else "-") + f'{float(np.abs(diffPrice)):,}' + ")"

print(stringToPrint + "\n")

