FROM python
#FROM ubuntu:20.04

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

ENV NOTVISIBLE="in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN pip install debugpy

CMD ["/usr/sbin/sshd", "-D"]
EXPOSE 22


#CMD    ["/usr/sbin/sshd", "-D"]

#copy ./src /code

#CMD ["python","-m","debugpy","--listen","localhost:3000","--wait-for-client","hello.py" ]