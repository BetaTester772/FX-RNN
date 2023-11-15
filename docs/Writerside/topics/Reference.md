# Reference

## Data of EX rate

[KB 통화별 환율 조회: USD - KRW](https://obank.kbstar.com/quics?page=C101422)

[FX_Rate.csv](https://github.com/BetaTester772/FX-RNN/blob/master/FX_Rate.csv)

## Model evaluation

* SimpleRNN: `0.9993719301069783`
* LSTM: `0.9998571595732255`
* GRU: `0.9999091173873708`

> Metrics:  `R^2 score`
> 
>Best possible score is 1.0, and it can be negative (because the model can be arbitrarily worse). In the general case
> when the true y is non-constant, a constant model that always predicts the average y disregarding the input features
> would get a R^2 score of 0.0.
