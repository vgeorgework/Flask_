FROM python:3.6
EXPOSE 5000
RUN mkdir -p /app
RUN ls /app
COPY . /app
RUN ls /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python3 app.py

