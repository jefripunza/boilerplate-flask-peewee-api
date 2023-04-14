# FROM python:3.6-slim
FROM python:3.8-alpine
LABEL maintainer="Jefri Herdi Triyanto jefriherditriyanto@gmail.com"


ENV PORT 5001
ENV STATIC_PATH /server/static


WORKDIR /server
COPY . .
RUN pip install -r /server/requirements.txt


# 🚀 Finish !!
ENTRYPOINT [ "python" ]
CMD ["main.py"]