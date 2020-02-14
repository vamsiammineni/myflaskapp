From python:3.8
WORKDIR /myflaskapp
COPY main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD python main.py