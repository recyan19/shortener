README for url shortening service

1. First clone project:
  git clone https://github.com/recyan19/shortener.git
2. Create virtualenv and install all requirements:
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
3. Create database:
  python manage.py migrate
4. Create superuser:
  python manage.py createsuperuser (follow instructions and don't forget to provide email, without it you will be able to       login only via /admin page.
5. Test app:
  python manage.py test
6. Run locally:
  python manage.py runserver
  
You can use service without authentication but you will be unable to watch your shortened urls and statistics for them.
