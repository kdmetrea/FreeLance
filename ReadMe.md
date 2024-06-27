

# Freelance
![Static Badge](https://img.shields.io/badge/-blue?style=flat&logo=telegram&link=t.me%2FKdmetrea) ![Static Badge](https://img.shields.io/badge/Kdmetrea-FreeLance-green) ![GitHub top language](https://img.shields.io/github/languages/top/Kdmetrea/Freelance) ![GitHub](https://img.shields.io/github/license/Kdmetrea/Freelance) ![GitHub Repo stars](https://img.shields.io/github/stars/Kdmetrea/Freelance) ![GitHub issues](https://img.shields.io/github/issues/Kdmetrea/Freelance)


This website template is designed for general use to create similar sites. When using the site, **you must specify the name** of the creator of the original template.
# Stack
 - MySql
 - React(Node.js)
 - Python3(Django)
# Installation
All stack programs must be installed on your server before installation
## Installation on Linux(arch)

*If yay is not installed*

      sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si

**Python**

    yay -S python312

**React**

    yay -S nvm

**MySql**

    sudo pacman -S Mariadb
    
    mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
    
    sudo systemd start mariadb

## Installation on windows
**Python**
[Python Installers for windows](https://www.python.org/downloads/windows/)

**React**
   [NodeJs Installer for windows](https://nodejs.org/en/download/prebuilt-installer)
   
**MySql**
 [Mariadb Installer for windows](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.4.2&os=windows&cpu=x86_64&pkg=msi&mirror=mobinhost)
# Building

## For development
 1. Clone a git repository
 
	 `git clone https://github.com/kdmetrea/FreeLance/tree/main`
 
 2. Go to the project folder
 
    `cd Freelance`
    
 3. Create a virtual environment for Python
 
	 `python -m venv <NameForVenv>`
4.  Installing the necessary Python libraries

	`pip install django django-rest-framework pillow django-extra-fields fuzzywuzzy mysqlclient psycopg2 django-imagekit`

5. Installing React

	`npm install React`

6. Creating a Database in MySQL

	`mysql -u root -p -e "CREATE DATABASE FreeLance"`

7. Project Launch

	`cd MainAppFreelance`
	
	`python manage.py migrte`
	
	`python manage.py runserver`

## For exploration on the server
 1. Clone a git repository
 
	 `git clone <MylinkRep>`
 
 2. Go to the project folder
 
    `cd Freelance`
    
 3. Create a virtual environment for Python
 
	 `python -m venv <NameForVenv>`
4.  Installing the necessary Python libraries

	`pip install django django-rest-framework pillow django-extra-fields fuzzywuzzy mysqlclient psycopg2 django-imagekit`
	
5. Creating a Database in MySQL

	`mysql -u root -p -e "CREATE DATABASE FreeLance"`
