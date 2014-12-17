Template for API

Installation
------------
# python3 -m venv flask --without-pip
# source flask/bin/activate
# ./flask_venv.sh
 
# deactivate

The sqlite database must also be created before the application can run, and the `db_create.py` script takes care of that. See the [Database tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) for the details.

Running
-------
Run run.py (or) flask/bin/gunicorn --log-file - app:app (starts on localhost:5000 or localhost:8000)

Deploying (after intalling heroku toolbelt)
---------
heroku login
heroku apps:create flask-template
heroku addons:add heroku-postgresql:dev
heroku pg:promote HEROKU_POSTGRESQL_CHARCOAL_URL
heroku config:set HEROKU=1
git push heroku master
heroku run init --app flask-template1

Celery
------
ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9
celery -A app.celery worker --loglevel=info &

curl -i http://localhost:5000/books?limit=100

curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"Darva"}' http://localhost:5000/books/11

curl -i -H "Content-Type: application/json" -X POST -d '{"title":"D", "author":"D"}' http://localhost:5000/books

curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/books/11


curl -i -H "Content-Type: application/json" -X POST -d '{"title":"D", "author":"D"}' http://book-spider.herokuapp.com/books


curl -i http://alam1.aclibrary.org/search/?searchtype=t&searcharg=flash+boys
curl -i "http://alam1.aclibrary.org/search/q?author=lewis%2C+michael&title=flash+boys"

## Next steps
. clean up frontend/google charts table
. clean up requirements.txt, remove unused files
. mimic blog.luisrei.com/articles/flaskrest.html structure "Implementing a RESTful Web API with Python & Flask"
. authentication
. change detect, goose