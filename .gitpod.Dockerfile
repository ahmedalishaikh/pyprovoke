FROM python:3.8-slim-buster
                    
USER gitpod

RUN sudo apt-get update && pip install invoke
CMD ["/usr/bin/bash"]
# More information: https://www.gitpod.io/docs/config-docker/
