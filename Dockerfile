# FROM python:3.6-slim
FROM python:3.8-alpine
LABEL maintainer="Jefri Herdi Triyanto jefriherditriyanto@gmail.com"

WORKDIR /app
COPY . .

# ⚒️ Prepare
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN python3 -m pip install -r requirements.txt --no-cache-dir
RUN apk --purge del .build-deps

# 💯 Last Configuration
RUN sed -i 's/localhost/host.docker.internal/g' .env

# 🚀 Finish !!
CMD ["flask", "run", "--host", "0.0.0.0"]
