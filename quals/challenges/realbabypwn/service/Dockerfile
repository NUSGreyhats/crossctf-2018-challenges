FROM ubuntu:latest
ENV user=realbabypwnuser
RUN apt-get update
RUN apt-get install -y xinetd
RUN useradd -m $user
RUN echo "$user     hard    nproc       20" >> /etc/security/limits.conf
COPY ./realbabypwn /home/$user/realbabypwn
COPY ./flag /home/$user/flag
COPY ./realbabypwnservice /etc/xinetd.d/realbabypwnservice
RUN chown -R root:$user /home/$user
RUN chmod -R 750 /home/$user
RUN chown root:$user /home/$user/flag
RUN chmod 440 /home/$user/flag
EXPOSE 31337
CMD ["/usr/sbin/xinetd", "-d"]
