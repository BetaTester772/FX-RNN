import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import datetime
import matplotlib.pyplot as plt

# 모델 및 데이터 로드
model = keras.models.load_model("./FX-gru(0.9999091173873708).h5")
df = pd.read_csv('./FX_New.csv')
df['매매기준율'] = df['매매기준율'].str.replace(',', '').astype(float)

# 데이터 전처리
data = df['매매기준율'].values
scaler = MinMaxScaler(feature_range=(0, 1))
baseRate = scaler.fit_transform(data.reshape(-1, 1))

sequence_length = 50

# 누적 평가 손익 계산
cumulative_profit = 0
cumulative_profits = []
results = []

file = open(f"result{datetime.datetime.now().strftime('%Y%m%d %H%M%S')}", "w")

for i in range(sequence_length, len(baseRate) - 2):
    # 현재 시퀀스 데이터
    current_sequence = baseRate[i - sequence_length:i]
    current_sequence = current_sequence.reshape((1, current_sequence.shape[0], current_sequence.shape[1]))

    # 모델을 사용한 예측
    prediction = model.predict(current_sequence)
    prediction = scaler.inverse_transform(prediction).squeeze()

    # 실제 값과 비교
    last_actual = scaler.inverse_transform(baseRate[i - 1].reshape(-1, 1)).squeeze()
    actual = scaler.inverse_transform(baseRate[i].reshape(-1, 1)).squeeze()

    print(f"예측: {prediction}, 실제: {actual}, 이전: {last_actual}")

    if prediction > last_actual:
        result = actual - last_actual
        action = "매입"
    elif prediction < last_actual:
        result = last_actual - actual
        action = "매도"
    else:
        result = 0
        action = "보류"

    # 결과 기록
    cumulative_profit += result
    cumulative_profits.append(cumulative_profit)
    results.append(result)
    print(f"{action}: {result}")
    file.write(f"{action}: {result}\n")

print(len(results))

file.write(f"총 수익: {cumulative_profit}\n")
print(f"총 수익: {cumulative_profit}")
file.close()

# 평가 손익 시각화
plt.rc('font', family='NanumGothic')
plt.bar(range(len(results)), results, label='평가 손익', color='orange')
plt.xlabel('거래 번호')
plt.ylabel('평가 손익')
plt.title('평가 손익 시각화')
plt.legend()
plt.show()

# 누적 평가 손익 시각화
plt.plot(cumulative_profits, label='누적 평가 손익', linestyle='-', color='purple')
plt.xlabel('거래 번호')
plt.ylabel('누적 평가 손익')
plt.title('누적 평가 손익 시각화')
plt.legend()
plt.show()
