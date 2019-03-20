FROM python:3.6.7
MAINTAINER portofolio "dzinsyah@alphatech.id"
RUN mkdir -p /portofolio
COPY . /portofolio
RUN pip3 install -r /portofolio/requirements.txt
WORKDIR /portofolio
ENTRYPOINT ["python3"]
CMD ["app.py"]