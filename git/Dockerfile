from alpine:latest

# TODO cannot get lighttpd to work so whatever
#RUN apk add --no-cache git git-gitweb lighttpd
RUN apk add --no-cache git git-gitweb perl perl-cgi

#WORKDIR /repos/test
#RUN git config --global --add safe.directory /repos/test
# Mount the repos in /repos with a volume when you run
COPY gitweb.conf /etc/gitweb.conf
COPY gitgo/gitcgi /gitcgi

EXPOSE 8080

CMD ["/gitcgi"]
#CMD ["git", "instaweb"]
