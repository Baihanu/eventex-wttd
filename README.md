# Eventex-Wttd
Projeto desenvolvido durante o curso [Welcome to the Django](https://henriquebastos.net/).

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.8.3
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:Baihanu/eventexx-wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o  Heroku.

```console
heroku crete minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py´
heroku config:set DEBUG=False
# Configure o email
git push heroku master --force
```
[![Build Status](https://travis-ci.com/Baihanu/eventex-wttd.svg?branch=main)](https://travis-ci.com/Baihanu/eventex-wttd)
