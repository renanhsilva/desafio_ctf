#crie um conteiner para executar o flask e o sqlite

FROM python:3.7-alpine

WORKDIR /app
COPY . /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["main.py"]
