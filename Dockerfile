FROM python:3
RUN git clone https://github.com/PabloHerrera99/Dispositivo.git
WORKDIR /Dispositivo
CMD ["python3", "-m", "test"]