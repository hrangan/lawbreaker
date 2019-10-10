FROM python:3.7.6
COPY . /opt/lawbreaker
WORKDIR /opt/lawbreaker
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim-tiny"]
RUN ["pip", "install", "--trusted-host", "pypi.python.org", "-e", ".[web]"]
CMD ["knave.web"]
