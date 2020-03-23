FROM python:3

ADD tester.py /

RUN pip install twilio

CMD [ "python", "./tester.py" ]
