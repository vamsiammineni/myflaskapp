From python:3.8
WORKDIR /myflaskapp
COPY main.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python3 main.py