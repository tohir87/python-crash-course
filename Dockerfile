FROM python:3

ADD methods.py /

CMD [ "python", "./methods.py" ]
