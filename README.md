# Como usar

curl -L https://raw.githubusercontent.com/cosmun-softwares/django-boilerplate/master/setup.sh | bash -s <project_name>


# <README.md>

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.7
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes
6. Execute o runserver

```console
git <git url>
cd project_name
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

## Gerar Secret Key

1. Ative o virtualenv
2. Execute o gerador
3. Copie a chave
4. Cole na variável SECRET_KEY do arquivo .env

```console
source env/bin/active
python contrib/secret_gen.py
```

## Gerar Backup automático

```console
bash backup/commands.sh
```
