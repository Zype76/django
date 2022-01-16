FROM quay.io/generic/centos8

ENV PYTHONUNBUFFERED=1

COPY . .

RUN dnf install python38 sqlite -y

RUN /usr/bin/python3.8 -m venv /djangosite

# Virtual environment activation: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV=/djangosite
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt
