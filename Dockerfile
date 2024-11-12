FROM python:3.14-rc-bookworm

WORKDIR /app/

COPY requirements.txt /app/
RUN python -m pip install -r requirements.txt

COPY fib.py /app/

ENTRYPOINT [ "python", "fib.py" ]

CMD [ "8" ]