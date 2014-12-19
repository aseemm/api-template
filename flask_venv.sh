cd flask
mkdir pypioffline
cd pypioffline/
curl -O https://pypi.python.org/packages/source/s/setuptools/setuptools-6.1.tar.gz
tar xvzf setuptools-6.1.tar.gz 
cd setuptools-6.1/
python ez_setup.py
easy_install pip
cd ../../..
sudo apt-get install rabbitmq-server
sudo apt-get install mysql-server mysql-client
sudo apt-get install python-mysqldb
flask/bin/pip install pymysql
flask/bin/pip install flask
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install sqlalchemy-migrate
flask/bin/pip install flask-whooshalchemy
flask/bin/pip install flask-wtf
flask/bin/pip install flask-babel
flask/bin/pip install guess_language
flask/bin/pip install flipflop
flask/bin/pip install coverage
flask/bin/pip install gunicorn
flask/bin/pip install celery
flask/bin/pip install requests
flask/bin/pip install beautifulsoup4