#!/bin/bash

if [ $1 ]
then
    project_name=$1

    echo ""
    echo -e "\e[32m###############################################################################################\e[0m"
    echo -e "\e[32m# CRIANDO DIRETÓRIO ###########################################################################\e[0m"
    echo -e "\e[32m###############################################################################################\e[0m"
    echo ""

    mkdir $project_name
    cd $project_name

    echo ""
    echo -e "\e[32m###############################################################################################\e[0m"
    echo -e "\e[32m# CRIANDO VIRTUALENV ##########################################################################\e[0m"
    echo -e "\e[32m###############################################################################################\e[0m"
    echo ""

    virtualenv env -p python3
    . env/bin/activate

    echo ""
    echo -e "\e[32m###############################################################################################\e[0m"
    echo -e "\e[32m# INSTALANDO DJANGO ###########################################################################\e[0m"
    echo -e "\e[32m###############################################################################################\e[0m"
    echo ""

    pip install django

    echo ""
    echo -e "\e[32m###############################################################################################\e[0m"
    echo -e "\e[32m# INICIANDO PROJETO ###########################################################################\e[0m"
    echo -e "\e[32m###############################################################################################\e[0m"
    echo ""

    django-admin startproject --template https://github.com/cosmun-softwares/django-boilerplate/archive/master.zip $project_name .

    # sed -i "s/project_name/$project_name/g" $project_name/wsgi.py
    # sed -i "s/project_name/$project_name/g" $project_name/settings.py
    # sed -i "s/project_name/$project_name/g" $project_name/urls.py
    # sed -i "s/project_name/$project_name/g" $project_name/core/urls.py
    # sed -i "s/project_name/$project_name/g" $project_name/core/apps.py
    # sed -i "s/project_name/$project_name/g" $project_name/core/models.py
    # sed -i "s/project_name/$project_name/g" manage.py

    sed -i "s/project_name/$project_name/g" Procfile
    sed -i 's/project_name/$project_name/g' *.py

    pip install -r requirements_dev.txt

    cp contrib/env-sample .env

    echo ""
    echo -e "\e[32m##############################################################################################\e[0m"
    echo -e "\e[32m# VERIFICANDO PROJETO ########################################################################\e[0m"
    echo -e "\e[32m##############################################################################################\e[0m"
    echo ""

    python manage.py check
else
    echo -e "\e[31m##############################################################################################\e[0m"
    echo -e "\e[31m# INFORME O NOME DO PROJETO ##################################################################\e[0m"
    echo -e "\e[31m##############################################################################################\e[0m"
fi
