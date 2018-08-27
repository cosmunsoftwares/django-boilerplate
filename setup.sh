#!/bin/bash

if [ $1 ]
then
    project_name=$1

    echo "Criando diretório $project_name"

    mkdir $project_name
    cd $project_name

    echo "Criando virtualenv"
    virtualenv env -p python3
    . env/bin/activate

    echo "Instalando django"
    pip install django

    echo "Iniciando projeto"
    django-admin startproject --template https://github.com/cosmun-softwares/django-boilerplate/archive/master.zip $project_name .

    sed -i "s/project_name/$project_name/g" $project_name/wsgi.py
    sed -i "s/project_name/$project_name/g" $project_name/settings.py
    sed -i "s/project_name/$project_name/g" $project_name/urls.py
    sed -i "s/project_name/$project_name/g" $project_name/core/urls.py
    sed -i "s/project_name/$project_name/g" $project_name/core/apps.py
    sed -i "s/project_name/$project_name/g" $project_name/core/models.py
    sed -i "s/project_name/$project_name/g" Procfile
    sed -i "s/project_name/$project_name/g" manage.py

    pip install -r requirements_dev.txt

    cp contrib/env-sample .env

    echo "Verificando Projeto"

    python manage.py check
else
    echo 'Informe o nome do projeto'
fi
