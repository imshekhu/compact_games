Setup :

Install Docker
cd compactgames
docker-compose up

This will build two images 
1. Django image 
2. PostgresSql image

For tests:
python manage.py test &&

For coverage:
coverage run --source='./api' --omit=*/scripts/*,*/models.py,*/views.py  manage.py test
coverage report
coverage html

NOTE: Coverage report is created inside htmlcov folder and can be peeked using index.html
