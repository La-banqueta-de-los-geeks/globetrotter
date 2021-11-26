FROM python:3.7
COPY . /src/
WORKDIR /src
# run server
ENTRYPOINT [ "./entrypoints/docker-entrypoint.sh" ]