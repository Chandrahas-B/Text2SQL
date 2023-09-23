FROM robd003/python3.10:latest

WORKDIR /app

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN make pip-install

CMD ["make", "run"]

EXPOSE 7860