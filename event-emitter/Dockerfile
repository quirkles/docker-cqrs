FROM python:3.7-alpine
WORKDIR /code

# Install dependencies:
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

# Run the application:
COPY src .

#CMD ["python", "app.py"]
