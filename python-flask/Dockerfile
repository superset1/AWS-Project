FROM alpine

ENV dir="/web/"
ENV PYTHONUNBUFFERED=1

WORKDIR $dir

COPY . $dir/

RUN apk add --update --no-cache python3 &&\
    ln -sf python3 /usr/bin/python &&\
    python3 -m ensurepip &&\
    pip3 install --no-cache --upgrade pip setuptools &&\
    pip3 install -r $dir/requirements.txt

ENTRYPOINT ["python3", "application.py"]

EXPOSE 8000

# Run following command for start container
# docker build -t flask .
# docker run --name flask -d --restart=always -p 8000:5000 superset1/flask:v2
# docker run --name flask -d --restart=always -p 8000:5000 -v /usr/share/nginx/html/assets:/web/static:ro superset1/flask:v2