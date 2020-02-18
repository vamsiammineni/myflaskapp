From python:3.8
WORKDIR /myflaskapp
COPY main.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD python3 main.py