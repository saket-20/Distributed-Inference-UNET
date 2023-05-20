FROM python:3.9.16
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip install tensorflow-cpu --user
RUN pip install flask --user
RUN pip install matplotlib --user
RUN pip3 install --upgrade --force-reinstall setuptools
RUN find /usr -name '*.pyc' -delete
COPY . /
ENTRYPOINT [ "python3" ]
CMD ["app.py"]