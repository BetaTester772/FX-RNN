# Training

모델 요약 및 fit 관련 정보

> 모델과 옵티마이저는 [연구 결과](RNN-model-research.md)를 바탕으로 선정함

## SimpleRNN Model

Summary
:
```
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 simple_rnn_4 (SimpleRNN)    (None, 50, 50)            2600      
 simple_rnn_5 (SimpleRNN)    (None, 50)                5050      
 dense_2 (Dense)             (None, 1)                 51        
=================================================================
Total params: 7701 (30.08 KB)
Trainable params: 7701 (30.08 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
```

Training setting
:
* Callbacks: EarlyStopping(monitor='val_loss', patience=3)
* Loss: Mean_Squared_Error
* Optimizer: Adam

History
:
![RNN history](RNNhistory.png)
```
Epoch 1/50
349/349 [==============================] - 26s 57ms/step - loss: 0.0027 - val_loss: 2.4990e-05
Epoch 2/50
349/349 [==============================] - 20s 57ms/step - loss: 2.0591e-05 - val_loss: 1.6920e-05
Epoch 3/50
349/349 [==============================] - 19s 56ms/step - loss: 1.5860e-05 - val_loss: 1.3386e-05
Epoch 4/50
349/349 [==============================] - 19s 55ms/step - loss: 1.3670e-05 - val_loss: 1.1369e-05
Epoch 5/50
349/349 [==============================] - 20s 56ms/step - loss: 1.2269e-05 - val_loss: 1.2177e-05
Epoch 6/50
349/349 [==============================] - 19s 54ms/step - loss: 2.0865e-05 - val_loss: 8.2757e-05
Epoch 7/50
349/349 [==============================] - 20s 56ms/step - loss: 2.6854e-05 - val_loss: 3.3354e-05
```

## LSTM Model

Summary
:
```
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 lstm_2 (LSTM)               (None, 100)               40800                                                   
 dense_2 (Dense)             (None, 1)                 101                                                      
=================================================================
Total params: 40901 (159.77 KB)
Trainable params: 40901 (159.77 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
```

Training setting
:
* Callbacks: EarlyStopping(monitor='val_loss', patience=3)
* Loss: Mean_Squared_Error
* Optimizer: Adam

History
:
![LSTM history](LSTMhistory.png)
```
Epoch 1/50
349/349 [==============================] - 10s 8ms/step - loss: 0.0015 - val_loss: 1.1754e-05
Epoch 2/50
349/349 [==============================] - 2s 7ms/step - loss: 1.1712e-05 - val_loss: 1.1424e-05
Epoch 3/50
349/349 [==============================] - 2s 7ms/step - loss: 1.1356e-05 - val_loss: 1.1008e-05
Epoch 4/50
349/349 [==============================] - 2s 7ms/step - loss: 1.1004e-05 - val_loss: 1.0868e-05
Epoch 5/50
349/349 [==============================] - 2s 7ms/step - loss: 1.0609e-05 - val_loss: 1.0144e-05
Epoch 6/50
349/349 [==============================] - 2s 7ms/step - loss: 1.0311e-05 - val_loss: 9.7962e-06
Epoch 7/50
349/349 [==============================] - 2s 7ms/step - loss: 9.7611e-06 - val_loss: 9.3512e-06
Epoch 8/50
349/349 [==============================] - 2s 7ms/step - loss: 9.7010e-06 - val_loss: 9.0441e-06
Epoch 9/50
349/349 [==============================] - 2s 7ms/step - loss: 9.4313e-06 - val_loss: 9.2712e-06
Epoch 10/50
349/349 [==============================] - 2s 7ms/step - loss: 9.2417e-06 - val_loss: 9.3758e-06
Epoch 11/50
349/349 [==============================] - 2s 7ms/step - loss: 9.3990e-06 - val_loss: 8.1832e-06
Epoch 12/50
349/349 [==============================] - 2s 7ms/step - loss: 9.2997e-06 - val_loss: 7.8138e-06
Epoch 13/50
349/349 [==============================] - 2s 7ms/step - loss: 9.2090e-06 - val_loss: 8.5546e-06
Epoch 14/50
349/349 [==============================] - 2s 7ms/step - loss: 8.7962e-06 - val_loss: 7.3502e-06
Epoch 15/50
349/349 [==============================] - 2s 7ms/step - loss: 8.6043e-06 - val_loss: 7.5583e-06
Epoch 16/50
349/349 [==============================] - 2s 7ms/step - loss: 9.2771e-06 - val_loss: 6.8191e-06
Epoch 17/50
349/349 [==============================] - 2s 7ms/step - loss: 7.9040e-06 - val_loss: 1.4065e-05
Epoch 18/50
349/349 [==============================] - 2s 7ms/step - loss: 8.4011e-06 - val_loss: 7.1161e-06
Epoch 19/50
349/349 [==============================] - 2s 7ms/step - loss: 8.1817e-06 - val_loss: 7.5856e-06
```


## GRU Model

Summary
:
```
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 gru_2 (GRU)                 (None, 50, 50)            7950                       
 gru_3 (GRU)                 (None, 50)                15300                   
 dense_1 (Dense)             (None, 1)                 51                      
=================================================================
Total params: 23301 (91.02 KB)
Trainable params: 23301 (91.02 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
```

Training setting
:
* Callbacks: EarlyStopping(monitor='val_loss', patience=3)
* Loss: Mean_Squared_Error
* Optimizer: Adam

History
:
![GRU history.png](GRUhistory.png)
```
Epoch 1/50
349/349 [==============================] - 12s 10ms/step - loss: 0.0025 - val_loss: 7.5941e-06
Epoch 2/50
349/349 [==============================] - 3s 8ms/step - loss: 7.0093e-06 - val_loss: 6.1103e-06
Epoch 3/50
349/349 [==============================] - 3s 8ms/step - loss: 5.8589e-06 - val_loss: 5.3030e-06
Epoch 4/50
349/349 [==============================] - 3s 8ms/step - loss: 5.2649e-06 - val_loss: 4.8958e-06
Epoch 5/50
349/349 [==============================] - 3s 8ms/step - loss: 4.9381e-06 - val_loss: 4.6823e-06
Epoch 6/50
349/349 [==============================] - 3s 8ms/step - loss: 4.7218e-06 - val_loss: 4.4238e-06
Epoch 7/50
349/349 [==============================] - 3s 8ms/step - loss: 4.5645e-06 - val_loss: 4.3088e-06
Epoch 8/50
349/349 [==============================] - 3s 8ms/step - loss: 4.4203e-06 - val_loss: 4.1245e-06
Epoch 9/50
349/349 [==============================] - 3s 8ms/step - loss: 4.3127e-06 - val_loss: 4.0519e-06
Epoch 10/50
349/349 [==============================] - 3s 8ms/step - loss: 4.3005e-06 - val_loss: 4.5148e-06
Epoch 11/50
349/349 [==============================] - 3s 8ms/step - loss: 4.2540e-06 - val_loss: 3.9034e-06
Epoch 12/50
349/349 [==============================] - 3s 8ms/step - loss: 4.2584e-06 - val_loss: 3.7366e-06
Epoch 13/50
349/349 [==============================] - 3s 8ms/step - loss: 4.3550e-06 - val_loss: 3.9741e-06
Epoch 14/50
349/349 [==============================] - 3s 8ms/step - loss: 5.3136e-06 - val_loss: 1.1133e-05
Epoch 15/50
349/349 [==============================] - 3s 8ms/step - loss: 5.3412e-06 - val_loss: 4.8264e-06
```
