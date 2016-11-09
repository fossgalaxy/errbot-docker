from python:3

# don't be root inside the container
RUN adduser --disabled-password --gecos '' errbot

# install requirements (do this bit first)
ADD requirements.txt /home/errbot/
RUN pip install -r /home/errbot/requirements.txt

# copy bot code to it's new home
USER errbot
RUN mkdir -p /home/errbot/bot/ /home/errbot/bot/log
WORKDIR /home/errbot/bot/
ADD bot /home/errbot/bot/

VOLUME ["/home/errbot/data", "/home/errbot/plugins"]
CMD ["errbot"]
