FROM rasa/rasa:3.6.4-full

WORKDIR  '/app'
COPY . /app
USER root
COPY ./data /app/data
RUN  rasa train
VOLUME /app
VOLUME /app/data
VOLUME /app/models
ENTRYPOINT [ "rasa" ]
CMD [ "run","-m","/app/models","--enable-api","--cors","\"*\"","--endpoints", "endpoints.yml"]

EXPOSE 5055
USER 1001