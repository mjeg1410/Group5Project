FROM python:3.6
WORKDIR /app
Copy requirements.txt .
RUN pip3 install -r requirements.txt 
ENTRYPOINT [/user/local/bin/python3, app.py]
COPY . . 
