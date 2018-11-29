# Como usar

curl -L http://bit.ly/cosmun-softwares-django-boilerplate | bash -s <project_name>


# <README.md>

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.
6. Execute o runserver.

```console
git clone git@gitlab.com:agencia-mentor/cdl.git
cd schedules
virtualenv env --python=python3 # python 3.6 ou mais atual
source env/bin/activate
pip install -r requirements_dev.txt
cp contrib/env-sample .env
coverage run --source='.' manage.py test -v 2 ; coverage report --show-missing
python manage.py runserver
```

## Qualidade do código

```console
flake8 --config=.flake8
```


## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Define um SECRET_KEY segura para instância.
4. Defina DEBUG=True
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia

heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=.herokuapp.com
heroku config:set EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
heroku config:set EMAIL_HOST=localhost
heroku config:set EMAIL_PORT=25
heroku config:set EMAIL_USE_TLS=False
heroku config:set EMAIL_HOST_USER=
heroku config:set EMAIL_HOST_PASSWORD=
heroku config:set DEFAULT_FROM_EMAIL=
heroku config:set SERVER_EMAIL=

git push heroku master --force
```
