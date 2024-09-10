import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://docs.google.com/spreadsheets/d/1IS8idBZgifxAaWG3s76ERy6agzsE-cat5YXz00h6XDw/export?format=csv'
df = pd.read_csv(url)

# a) Gráfico de densidade de gorjetas por sexo
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x='gorjeta', hue='sexo', fill=True)
plt.title('Densidade de Gorjetas por Sexo')
plt.xlabel('Valor da Gorjeta')
plt.ylabel('Densidade')
plt.show()

# b) Gráfico de densidade de gorjetas pela quantidade de pessoas na mesa
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x='gorjeta', hue='quantidade', fill=True, palette='viridis')
plt.title('Densidade de Gorjetas pela Quantidade de Pessoas na Mesa')
plt.xlabel('Valor da Gorjeta')
plt.ylabel('Densidade')
plt.show()

# c) Gráfico de densidade de gorjetas por dia da semana
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x='gorjeta', hue='dia', fill=True, palette='pastel')
plt.title('Densidade de Gorjetas por Dia da Semana')
plt.xlabel('Valor da Gorjeta')
plt.ylabel('Densidade')
plt.show()
