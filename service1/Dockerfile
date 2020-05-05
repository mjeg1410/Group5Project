FROM python:3.6
WORKDIR /app
Copy requirements.txt .
RUN pip3 install -r requirements.txt 
ENTRYPOINT ["/usr/local/bin/python"3, app.py]
COPY . . 
