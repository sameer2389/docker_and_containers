FROM python:3-onbuild
COPY . /usr/src/app
RUN pip install -r requirements.txt
CMD ["python","api1_which_calls_api.py"]