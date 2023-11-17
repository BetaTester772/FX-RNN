# RNN model search

> The following table shows the results of the RNN model losses at epoch 5.

## SimpleRNN

![RNN Loss](RNNloss.png)

| Rank | Model                         | Optimizer | Last Loss              |
|------|-------------------------------|-----------|------------------------|
| 0    | SimpleRNN-50-50-1             | Adam      | 7.1484460022475105e-06 |
| 1    | SimpleRNN-100-1               | Adam      | 8.823052667139564e-06  |
| 2    | SimpleRNN-50-1                | Adamax    | 1.0893405487877317e-05 |
| 3    | Bidirectional-SimpleRNN-100-1 | Adam      | 1.2944186892127618e-05 |
| 4    | SimpleRNN-50-1                | Adam      | 1.68453134392621e-05   |
| 5    | SimpleRNN-50-50-1             | Adamax    | 1.9008082745131105e-05 |
| 6    | Bidirectional-SimpleRNN-100-1 | Adamax    | 2.1004654627176933e-05 |
| 7    | SimpleRNN-50-1                | Nadam     | 2.120728458976373e-05  |
| 8    | SimpleRNN-100-100-1           | Adamax    | 2.4231214410974644e-05 |
| 9    | SimpleRNN-100-1               | Adamax    | 2.442320874251891e-05  |
| 10   | SimpleRNN-100-100-1           | SGD       | 3.388046388863586e-05  |
| 11   | SimpleRNN-100-1               | SGD       | 3.389002085896209e-05  |
| 12   | SimpleRNN-100-100-1           | Adagrad   | 3.476670099189505e-05  |
| 13   | SimpleRNN-100-1               | Nadam     | 3.7021618481958285e-05 |
| 14   | Bidirectional-SimpleRNN-50-1  | Adam      | 3.967313750763424e-05  |
| 15   | SimpleRNN-50-1                | SGD       | 3.971823753090575e-05  |
| 16   | Bidirectional-SimpleRNN-100-1 | SGD       | 4.183324199402705e-05  |
| 17   | Bidirectional-SimpleRNN-100-1 | Nadam     | 4.296704355510883e-05  |
| 18   | SimpleRNN-100-1               | Adagrad   | 4.6194210881367326e-05 |
| 19   | Bidirectional-SimpleRNN-50-1  | Nadam     | 4.66597884951625e-05   |
| 20   | Bidirectional-SimpleRNN-50-1  | Adamax    | 5.6208711612271145e-05 |
| 21   | SimpleRNN-50-50-1             | SGD       | 5.6846984080038965e-05 |
| 22   | SimpleRNN-100-100-1           | Adam      | 6.122249033069238e-05  |
| 23   | SimpleRNN-50-1                | RMSprop   | 6.467275670729578e-05  |
| 24   | SimpleRNN-50-50-1             | Nadam     | 6.788319296902046e-05  |
| 25   | Bidirectional-SimpleRNN-50-1  | SGD       | 7.195172656793147e-05  |
| 26   | Bidirectional-SimpleRNN-100-1 | Adagrad   | 7.867234671721235e-05  |
| 27   | SimpleRNN-50-1                | Adafactor | 8.302795322379097e-05  |
| 28   | SimpleRNN-100-1               | RMSprop   | 8.682197949383408e-05  |
| 29   | SimpleRNN-100-1               | Adafactor | 9.388985927216709e-05  |
| 30   | SimpleRNN-50-1                | Adagrad   | 0.00010135362390428782 |
| 31   | Bidirectional-SimpleRNN-50-1  | Adagrad   | 0.00010191676847171038 |
| 32   | Bidirectional-SimpleRNN-100-1 | RMSprop   | 0.00010570752783678472 |
| 33   | SimpleRNN-50-50-1             | Adagrad   | 0.0001084331379388459  |
| 34   | Bidirectional-SimpleRNN-50-1  | RMSprop   | 0.00010903566726483405 |
| 35   | Bidirectional-SimpleRNN-100-1 | Adafactor | 0.0001349876110907644  |
| 36   | SimpleRNN-50-50-1             | RMSprop   | 0.00015666404215153307 |
| 37   | SimpleRNN-100-100-1           | Adadelta  | 0.00017835885228123516 |
| 38   | Bidirectional-SimpleRNN-50-1  | Adafactor | 0.0001933307503350079  |
| 39   | SimpleRNN-100-100-1           | RMSprop   | 0.0001989090087590739  |
| 40   | SimpleRNN-50-50-1             | Adadelta  | 0.00033994350815191865 |
| 41   | SimpleRNN-50-50-1             | Adafactor | 0.0005301204510033131  |
| 42   | SimpleRNN-100-100-1           | Adafactor | 0.0006282638059929013  |
| 43   | Bidirectional-SimpleRNN-100-1 | Adadelta  | 0.0007931040017865598  |
| 44   | SimpleRNN-100-1               | Adadelta  | 0.0009286125423386693  |
| 45   | Bidirectional-SimpleRNN-50-1  | Adadelta  | 0.001739894854836166   |
| 46   | SimpleRNN-50-1                | Adadelta  | 0.005772875621914864   |
| 47   | SimpleRNN-50-50-1             | Ftrl      | 0.012297271750867367   |
| 48   | SimpleRNN-100-100-1           | Nadam     | 0.029822541400790215   |
| 49   | SimpleRNN-100-100-1           | Ftrl      | 0.05450371280312538    |
| 50   | Bidirectional-SimpleRNN-50-1  | Ftrl      | 0.05807475373148918    |
| 51   | Bidirectional-SimpleRNN-100-1 | Ftrl      | 0.14164793491363525    |
| 52   | SimpleRNN-100-1               | Ftrl      | 0.14277608692646027    |
| 53   | SimpleRNN-50-1                | Ftrl      | 0.16147620975971222    |

## LSTM

![LSTM Loss](LSTMloss.png)

| Rank | Model                    | Optimizer | Last Loss              |
|------|--------------------------|-----------|------------------------|
| 0    | LSTM-100-1               | Adam      | 1.0339412256143987e-05 |
| 1    | LSTM-100-100-1           | Adam      | 1.2349913049547467e-05 |
| 2    | LSTM-100-1               | SGD       | 1.4022998584550805e-05 |
| 3    | LSTM-50-1                | Adam      | 1.5067796994117089e-05 |
| 4    | LSTM-100-100-1           | Adamax    | 1.5245454960677307e-05 |
| 5    | Bidirectional-LSTM-100-1 | Adam      | 1.5491961676161736e-05 |
| 6    | LSTM-100-1               | Adamax    | 1.559750126034487e-05  |
| 7    | LSTM-50-50-1             | Adam      | 1.5863315638853237e-05 |
| 8    | LSTM-50-1                | Nadam     | 1.6074234736151993e-05 |
| 9    | LSTM-100-1               | Nadam     | 1.767165849742014e-05  |
| 10   | Bidirectional-LSTM-50-1  | Adam      | 1.9828763470286503e-05 |
| 11   | LSTM-50-50-1             | Adamax    | 2.043077620328404e-05  |
| 12   | LSTM-50-1                | Adamax    | 2.0753839635290205e-05 |
| 13   | Bidirectional-LSTM-50-1  | Nadam     | 2.703026621020399e-05  |
| 14   | LSTM-50-50-1             | Nadam     | 2.841568857547827e-05  |
| 15   | Bidirectional-LSTM-100-1 | Adamax    | 2.8701555493171327e-05 |
| 16   | Bidirectional-LSTM-100-1 | Nadam     | 3.527190347085707e-05  |
| 17   | LSTM-100-100-1           | SGD       | 3.6755187466042116e-05 |
| 18   | Bidirectional-LSTM-50-1  | Adamax    | 3.71811656805221e-05   |
| 19   | Bidirectional-LSTM-100-1 | SGD       | 4.006939707323909e-05  |
| 20   | LSTM-100-100-1           | Nadam     | 4.2655414290493354e-05 |
| 21   | LSTM-50-1                | Adafactor | 4.704422826762311e-05  |
| 22   | Bidirectional-LSTM-50-1  | SGD       | 6.383193976944312e-05  |
| 23   | LSTM-100-1               | Adafactor | 7.01018943800591e-05   |
| 24   | LSTM-100-100-1           | Adagrad   | 7.49484242987819e-05   |
| 25   | Bidirectional-LSTM-50-1  | Adafactor | 8.77444981597364e-05   |
| 26   | Bidirectional-LSTM-100-1 | Adafactor | 9.765525464899838e-05  |
| 27   | LSTM-50-50-1             | Adafactor | 9.819125989452004e-05  |
| 28   | LSTM-50-1                | SGD       | 0.00010430644761072472 |
| 29   | Bidirectional-LSTM-50-1  | RMSprop   | 0.00012001615687040612 |
| 30   | LSTM-100-100-1           | Adafactor | 0.00012728323054034263 |
| 31   | LSTM-50-1                | RMSprop   | 0.00012728404544759542 |
| 32   | LSTM-100-1               | RMSprop   | 0.00013790529919788241 |
| 33   | Bidirectional-LSTM-100-1 | RMSprop   | 0.00014845369150862098 |
| 34   | LSTM-50-50-1             | SGD       | 0.00015427528705913574 |
| 35   | LSTM-50-50-1             | RMSprop   | 0.0002789665886666626  |
| 36   | LSTM-100-100-1           | RMSprop   | 0.0003185785317327827  |
| 37   | LSTM-50-50-1             | Adagrad   | 0.0003287503495812416  |
| 38   | Bidirectional-LSTM-100-1 | Adagrad   | 0.00159243936650455    |
| 39   | LSTM-100-1               | Adagrad   | 0.002229538280516863   |
| 40   | Bidirectional-LSTM-50-1  | Adagrad   | 0.00334408157505095    |
| 41   | LSTM-50-1                | Adagrad   | 0.006197857670485973   |
| 42   | LSTM-100-100-1           | Adadelta  | 0.01089305430650711    |
| 43   | Bidirectional-LSTM-100-1 | Adadelta  | 0.066889688372612      |
| 44   | Bidirectional-LSTM-50-1  | Adadelta  | 0.12039549648761749    |
| 45   | LSTM-50-50-1             | Adadelta  | 0.12757839262485504    |
| 46   | LSTM-50-1                | Adadelta  | 0.14293380081653595    |
| 47   | LSTM-100-1               | Adadelta  | 0.14473316073417664    |
| 48   | Bidirectional-LSTM-50-1  | Ftrl      | 0.1608467698097229     |
| 49   | LSTM-50-1                | Ftrl      | 0.1626897007226944     |
| 50   | Bidirectional-LSTM-100-1 | Ftrl      | 0.1633821725845337     |
| 51   | LSTM-100-1               | Ftrl      | 0.1633947789669037     |
| 52   | LSTM-50-50-1             | Ftrl      | 0.16430321335792542    |
| 53   | LSTM-100-100-1           | Ftrl      | 0.16444629430770874    |

## GRU

![GRU Loss](GRUloss.png)

| Rank | Model                   | Optimizer | Last Loss              |
|------|-------------------------|-----------|------------------------|
| 0    | GRU-50-50-1             | Adam      | 4.707890639110701e-06  |
| 1    | GRU-100-1               | Adam      | 4.766522579302546e-06  |
| 2    | GRU-100-100-1           | Adam      | 4.789349077327643e-06  |
| 3    | GRU-50-50-1             | Nadam     | 5.012138444726588e-06  |
| 4    | GRU-100-1               | Nadam     | 5.165178663446568e-06  |
| 5    | GRU-100-1               | SGD       | 5.4459974307974335e-06 |
| 6    | GRU-50-1                | Adafactor | 5.4775073294877075e-06 |
| 7    | GRU-100-100-1           | Adamax    | 5.480169420479797e-06  |
| 8    | GRU-50-1                | Nadam     | 5.524032530956902e-06  |
| 9    | GRU-50-50-1             | Adamax    | 5.756230166298337e-06  |
| 10   | GRU-50-1                | Adam      | 6.245525128178997e-06  |
| 11   | GRU-100-1               | Adamax    | 6.366941761370981e-06  |
| 12   | GRU-50-1                | Adamax    | 6.431740985135548e-06  |
| 13   | GRU-100-100-1           | SGD       | 7.98496330389753e-06   |
| 14   | GRU-50-1                | SGD       | 8.672521289554425e-06  |
| 15   | GRU-100-1               | Adafactor | 9.935271918948274e-06  |
| 16   | Bidirectional-GRU-100-1 | Adam      | 1.5871399227762595e-05 |
| 17   | Bidirectional-GRU-50-1  | Nadam     | 1.592828266439028e-05  |
| 18   | GRU-50-50-1             | SGD       | 1.6886509911273606e-05 |
| 19   | Bidirectional-GRU-100-1 | Nadam     | 1.7679689335636795e-05 |
| 20   | Bidirectional-GRU-100-1 | Adamax    | 2.0068768208147958e-05 |
| 21   | GRU-50-50-1             | Adafactor | 2.0379035049700178e-05 |
| 22   | Bidirectional-GRU-50-1  | SGD       | 2.297994251421187e-05  |
| 23   | Bidirectional-GRU-50-1  | Adam      | 2.3093560230336152e-05 |
| 24   | Bidirectional-GRU-100-1 | SGD       | 2.64266363956267e-05   |
| 25   | GRU-100-100-1           | Nadam     | 2.6985300792148337e-05 |
| 26   | Bidirectional-GRU-50-1  | Adafactor | 2.754455454123672e-05  |
| 27   | GRU-100-100-1           | Adafactor | 2.7930365831707604e-05 |
| 28   | Bidirectional-GRU-100-1 | Adafactor | 2.8062393539585173e-05 |
| 29   | Bidirectional-GRU-50-1  | Adamax    | 3.0205099392333068e-05 |
| 30   | GRU-50-1                | RMSprop   | 0.00012124768545618281 |
| 31   | Bidirectional-GRU-50-1  | RMSprop   | 0.00013024966756347567 |
| 32   | GRU-100-1               | RMSprop   | 0.00013586990826297551 |
| 33   | Bidirectional-GRU-100-1 | RMSprop   | 0.00018074044783134013 |
| 34   | GRU-50-50-1             | RMSprop   | 0.00024269278219435364 |
| 35   | GRU-100-100-1           | RMSprop   | 0.0003259317309129983  |
| 36   | GRU-100-100-1           | Adagrad   | 0.0020435492042452097  |
| 37   | Bidirectional-GRU-100-1 | Adagrad   | 0.0027248687110841274  |
| 38   | GRU-50-50-1             | Adagrad   | 0.004130566027015448   |
| 39   | GRU-100-1               | Adagrad   | 0.006076014135032892   |
| 40   | Bidirectional-GRU-50-1  | Adagrad   | 0.006933880504220724   |
| 41   | GRU-100-100-1           | Adadelta  | 0.007357695139944553   |
| 42   | GRU-50-1                | Adagrad   | 0.00936937890946865    |
| 43   | Bidirectional-GRU-100-1 | Adadelta  | 0.06046106666326523    |
| 44   | Bidirectional-GRU-50-1  | Ftrl      | 0.07972640544176102    |
| 45   | GRU-50-1                | Adadelta  | 0.10427102446556091    |
| 46   | GRU-100-1               | Adadelta  | 0.10565608739852905    |
| 47   | GRU-50-1                | Ftrl      | 0.11111944168806076    |
| 48   | GRU-100-1               | Ftrl      | 0.11140456795692444    |
| 49   | Bidirectional-GRU-100-1 | Ftrl      | 0.11382657289505005    |
| 50   | GRU-50-50-1             | Adadelta  | 0.1153414323925972     |
| 51   | GRU-100-100-1           | Ftrl      | 0.14568881690502167    |
| 52   | GRU-50-50-1             | Ftrl      | 0.1479225903749466     |
| 53   | Bidirectional-GRU-50-1  | Adadelta  | 0.21434378623962402    |
