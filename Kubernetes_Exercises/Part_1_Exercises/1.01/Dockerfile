FROM python:3.9-slim

WORKDIR code

COPY main_application.py .

ENTRYPOINT ["python"]
CMD ["main_application.py"]

# docker image build -t fauxsys/kubernetes . && docker container run -t -i fauxsys/kubernetes
# docker image push fauxsys/kubernetes