FROM python:3.11

WORKDIR /dashboard_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["sh", "-c", "python populate.py && python -u app.py"]