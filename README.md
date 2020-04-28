## Desafio - IBov

23 de abril

Desafio em prever o ibovespa realizado no dia 23 de abril.


### Clone

```shell
$ git clone https://github.com/helderrezende/coding_challenge_pred_ibov.git
```

### Data

Os dados utilizados no modelo estão dentro da pasta "data/"


### Setup

MacOS:

```shell
$ conda create --name <env> python=3 pip
$ conda activate <env>
$ pip install -r requirements.txt
```


### Model

Dentro do notebook solution.ipynb está a lógica e explicação usada para prever o ibov.

Foi feito um modelo de regressão e backtest simples. O desafio foi feito em 4 horas e meia portanto tem diversos pontos a melhorar.
