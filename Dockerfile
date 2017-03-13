FROM amancevice/superset:0.15.4
MAINTAINER  PeertoPark
USER root
ADD superset/runserver .bin/runserver
RUN chown -R superset:superset .bin/runserver
USER superset
RUN chmod +x .bin/runserver
ADD superset_config.py /home/superset/superset_config.py
ENTRYPOINT ["runserver"]
CMD [""]
