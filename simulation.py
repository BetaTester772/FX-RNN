import pandas as pd

import tensorflow as tf
from tensorflow import keras
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

import datetime

model = keras.models.load_model("./FX-gru(0.9999091173873708).h5")

df = pd.read_csv('FX_New.csv')
df['매매기준율'] = df['매매기준율'].str.replace(',', '').astype(float)
data = df['매매기준율'].values

scaler = MinMaxScaler(feature_range=(0, 1))
baseRate = scaler.fit_transform(data.reshape(-1, 1))

sequence_length = 50

sequences = []
for i in range(sequence_length, len(baseRate)):
    sequences.append(baseRate[i - sequence_length:i + 1])

sequences = np.array(sequences)

X = sequences[:, :-1]
y = sequences[:, -1]

predictions = model.predict(X)

predictions = scaler.inverse_transform(predictions)[:-1]
y = scaler.inverse_transform(y.reshape(-1, 1))[1:]

# print(predictions[0]) TODO: check index
# print(y[0])
# print(predictions[-1])
# print(y[-1])
#
# input()

# 누적 평가 손익 계산
cumulative_profit = 0
cumulative_profits = []

results = []
file = open(f"result{datetime.datetime.now().strftime('%Y%m%d %H%M%S')}", "w")

for i in range(1, len(predictions)):
    prediction = round(predictions[i][0], 1)
    last_actual = round(y[i - 1][0], 1)
    actual = round(y[i][0], 1)
    if prediction > last_actual:
        result = actual - last_actual
        cumulative_profit += result
        results.append(result)
        print("매입:", result)
        file.write(f"매입: {result}" + "\n")
    elif prediction < last_actual:
        result = last_actual - actual
        cumulative_profit += result
        results.append(result)
        print("매도:", result)
        file.write(f"매도: {result}" + "\n")
    else:
        results.append(0)
        print("보류")
        file.write("보류" + "\n")

    cumulative_profits.append(cumulative_profit)

print("총 수익:", cumulative_profit)
file.write(f"총 수익: {cumulative_profit}" + "\n")
file.close()

print(len(results))

import matplotlib.pyplot as plt

plt.rc('font', family='NanumGothic')
print(plt.rcParams['font.family'])

# 평가 손익 시각화
# plt.figure(figsize=(10, 6))
plt.bar(range(len(results)), results, label='평가 손익', color='orange')
plt.xlabel('거래 번호')
plt.ylabel('평가 손익')
plt.title('평가 손익 시각화')
plt.legend()
plt.show()

# 누적 평가 손익 시각화
# plt.figure(figsize=(20, 6))
plt.plot(cumulative_profits, label='누적 평가 손익', linestyle='-', color='purple')
plt.xlabel('거래 번호')
plt.ylabel('누적 평가 손익')
plt.title('누적 평가 손익 시각화')
plt.legend()
plt.show()
