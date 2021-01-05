FROM ruby:2.6.0

EXPOSE 3000

RUN git clone https://github.com/docker-hy/rails-example-project
WORKDIR rails-example-project

RUN apt update && apt install nodejs -y && bundle install

##DEV
#ENV RAILS_LOG_TO_STDOUT=true
#RUN rails db:migrate
#CMD ["rails", "s"]

# PRODUCTION
ENV SECRET_KEY_BASE=randomstring
ENV RAILS_ENV=production
RUN rails db:migrate && rake assets:precompile
CMD ["rails", "s", "-e", "production"]

# docker image build -t exercise:14 . && docker container run -p 3000:3000 --name rials-example -d --rm exercise:14