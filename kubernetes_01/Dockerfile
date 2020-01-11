FROM python:3.6-alpine
LABEL maintainer="izaak200@gmail.com"
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev
WORKDIR /kubernetes_01
COPY ./requirements.txt .
RUN	 pip3 install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "kubernetes_01.wsgi:application", "--bind", "0.0.0.0:8001"]
COPY . .
EXPOSE 8001