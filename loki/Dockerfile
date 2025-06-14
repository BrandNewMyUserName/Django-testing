FROM python:3.11.8
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY myproject ./myproject
CMD ["sh", "-c", "env && python myproject/manage.py migrate && gunicorn --bind 0.0.0.0:8000 myproject.myproject.wsgi:application"]
