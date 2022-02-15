FROM python:3.8

# updating SO
RUN apt -y update

# Updating pip
RUN pip3 install --upgrade pip
# Installing ngspice
RUN apt -y install ngspice
RUN apt -y install libngspice0-dev
RUN apt -y install libngspice0

WORKDIR /skywater-pdk

WORKDIR /usr/app

COPY requirements.txt .

RUN pip3 install -r ./requirements.txt

RUN pyspice-post-installation --check-install

COPY . .

CMD [ "python3", "App.py" ]
