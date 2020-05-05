FROM python:3.7
WORKDIR /app
Copy requirements.txt .
RUN pip3 install -r requirements.txt 
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]
COPY . . 
