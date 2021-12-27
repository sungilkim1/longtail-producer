FROM python:3

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-binary :all: confluent-kafka

# tell the port number the container should expose
EXPOSE 3002

# run the command
ENTRYPOINT ["python3"]
CMD ["order.py"]