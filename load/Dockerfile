#!/bin/bash
FROM google/cloud-sdk:latest
COPY ./src /src
WORKDIR /src
RUN pip3 install pip-tools
RUN pip-compile
RUN pip3 install -r requirements.txt
RUN chmod +x /src/config/set_conf_gcp.sh
RUN /src/config/set_conf_gcp.sh

ENTRYPOINT ["python3", "/src/app/main.py", "/src/config/parameters.json"]