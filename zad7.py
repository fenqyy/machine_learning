import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

df = pd.DataFrame()
df['X'] = [1, 2, 3, 4, 5]
df['Y'] = [4, 6, 9, 11, 18]
print(df)
plt.scatter(df['X'], df['Y'], label='Wartości Niezależne')
plt.xlabel('Wartości X')
plt.ylabel('Wartości Y')
plt.legend()
plt.show()


def srednia(a):
    return sum(a) / len(a)


Mean_x = srednia(df['X'])
Mean_y = srednia(df['Y'])


def odchylenie(a):
    std = 0
    for i in a:
        std += ((i - srednia(a)) ** 2) / (len(a) - 1)
    return sqrt(std)


Sx = odchylenie(df['X'])
Sy = odchylenie(df['Y'])

n = len(df['X'])

pearson = pd.DataFrame(df[:])
pearson['y2'] = df['Y'] * df['Y']
pearson['xy'] = df['X'] * df['Y']
pearson['x2'] = df['X'] * df['X']
pearson['y2'] = df['Y'] * df['Y']
pearson.loc['sum'] = pearson.sum()

print("n = ", n)
print()
print(pearson)


def wsp_korelacji_pearsona(a):
    p = (((n * (pearson['xy'].loc['sum'])) - (pearson['X'].loc['sum'] * pearson['Y'].loc['sum'])) / (sqrt(
        (n * pearson['x2'].loc['sum'] - (pearson['X'].loc['sum'] ** 2)) * (
                    n * pearson['y2'].loc['sum'] - (pearson['Y'].loc['sum']) ** 2))))
    return p


pearson_result = wsp_korelacji_pearsona(pearson)
print()
print("Mean x: ", Mean_x)
print("Mean y: ", Mean_y)
print("Standard deviation x: ", Sx)
print("Standard deviation y: ", Sy)
print("r = ", pearson_result)

b = pearson_result * (Sy / Sx)
a = Mean_y - b * Mean_x
print("b = ", b)
print("a = ", a)


def linia_regresji(x):
    return (b * x) + a


x = np.linspace(0, 5, 1000)
plt.scatter(df['X'], df['Y'], label="Wartości Niezależne")
plt.plot(x, linia_regresji(x), 'r', label='Linia Regresji')
plt.xlabel('Wartości X')
plt.ylabel('Wartości Y')
plt.legend()
plt.show()

df_new_row = pd.DataFrame({ 'X': [6], 'Y': [np.nan] })
df = pd.concat([df, df_new_row])
df


def predict_y(x, b, a):
    return b * x + a


df.at[5, 'Y'] = predict_y(df['X'][5], b, a)
df
