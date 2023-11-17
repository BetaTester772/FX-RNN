# Overview

2023 하나고등학교 교내 학술제


  <a class="github-button" target="_blank" href="https://github.com/BetaTester772/FX-RNN" style="display: inline-block; background-color: #ffffff; color: #24292e; padding: 10px 20px; border-radius: 5px; text-decoration: none; transition: background-color 0.3s;">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png?hl=ko" alt="GitHub 아이콘"  /> GitHub에서 소스 보기
  </a>

[구두 47] 퀀터스: 합성곱 신경망(CNN)기반 실시간 퀀트 트레이딩 기법 제안

| 권동한 |            안호성            | 이정윤 | 이민규 |
|:---:|:-------------------------:|:---:|:---:|
|  @  | hoseong8115.dev@gmail.com |  @  |  @  |

## What is concept

RNN 예측 기반 환율 예측 모델을 통해 퀀트 트레이딩을 진행

## Data of EX rate

[KB 통화별 환율 조회: USD - KRW](https://obank.kbstar.com/quics?page=C101422)

[FX_Rate.csv](https://github.com/BetaTester772/FX-RNN/blob/master/FX_Rate.csv) - 2016.12.30 ~ 2023.11.03

[FX_New.csv](https://github.com/BetaTester772/FX-RNN/blob/master/FX_New.csv) - 2023.11.08 ~ 2023.11.15

| Index | Date     | 회차 | 등록시간     | 매매기준율    | 이전대비  | 송금보내실 때  | 송금받으실 때  | 현찰사실 때   | 현찰파실 때   | USD환산율 |
|-------|----------|----|----------|----------|-------|----------|----------|----------|----------|--------|
| 0     | 20161230 | 1  | 08:37:50 | 1,208.50 | -     | 1,219.90 | 1,197.10 | 1,229.64 | 1,187.36 | 1.0    |
| 1     | 20161230 | 2  | 08:40:58 | 1,208.50 | -     | 1,219.90 | 1,197.10 | 1,229.64 | 1,187.36 | 1.0    |
| 2     | 20161230 | 3  | 08:43:31 | 1,208.50 | -     | 1,219.90 | 1,197.10 | 1,229.64 | 1,187.36 | 1.0    |
| 3     | 20161230 | 4  | 08:52:44 | 1,208.50 | -     | 1,219.90 | 1,197.10 | 1,229.64 | 1,187.36 | 1.0    |
| 4     | 20161230 | 5  | 08:58:11 | 1,208.00 | ▼0.50 | 1,219.40 | 1,196.60 | 1,229.14 | 1,186.86 | 1.0    |

## Model evaluation

* SimpleRNN: `0.9993719301069783`
* LSTM: `0.9998571595732255`
* GRU: `0.9999091173873708`

> Metrics:  `R^2 score`
>
>Best possible score is 1.0, and it can be negative (because the model can be arbitrarily worse). In the general case
> when the true y is non-constant, a constant model that always predicts the average y disregarding the input features
> would get a R^2 score of 0.0.
