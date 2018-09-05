FROM python:2.7
EXPOSE 80
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "launcher.py"]
