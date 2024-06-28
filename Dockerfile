FROM python:3.10
WORKDIR /code
COPY req.txt /code/req.txt
RUN pip install --no-cache-dir --upgrade -r /code/req.txt
COPY ./src /code/src
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--log-level", "info"]