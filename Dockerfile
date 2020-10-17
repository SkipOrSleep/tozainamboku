# base image definition
FROM python:3.8.6

# package manager updating
RUN apt-get update
RUN apt-get upgrade -y

# locale & timezone settings
RUN apt-get install -y locales && \
    locale-gen ja_JP.UTF-8     && \
    localedef -f UTF-8 -i ja_JP ja_JP
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# operation tools installation
RUN apt-get install -y vim
RUN apt-get install -y less
RUN apt-get install -y sudo

# app requirements installation
RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install numpy
RUN pip install flask
RUN pip install pyyaml
RUN pip install pandas

# user settings
RUN echo "PS1='\[\e[0;35m\]\u@\h:\w\[\e[m\]\n\$ '" >> ${HOME}/.bashrc
RUN echo "alias ll='ls -l  --color=auto'"          >> ${HOME}/.bashrc
RUN echo "alias la='ls -la --color=auto'"          >> ${HOME}/.bashrc
RUN echo "alias grep='grep --color=auto'"          >> ${HOME}/.bashrc
