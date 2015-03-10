# UrlShorterner
Encurtador de url 

Intalando projeto

ubunto: 
Instalando a virtualenv
Setting up Virtualenvwrapper
Install pip for Python 3:
sudo apt-get install python3-pip Install Virtualenvwrapper
for Python 3:
sudo pip3 install virtualenvwrapper 

So far so good. Now it is time to configure Virtualenvwrapper.
Create a folder for your virtualenvs (I use ~/.virtualenvs) and set it as 

WORKON_HOME:
mkdir ~/.virtualenvs
export WORKON_HOME=~/.virtualenvs
Add the following lines to ~/.bashrc:
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'

Ativando virtualenv:
mkvirtualenv venv
workon venv
ou
source virtualenvs/venv/bin/activate



