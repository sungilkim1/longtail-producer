FROM python:3

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

ENV LIBRDKAFKA_VERSION 0.11.4
RUN curl -Lk -o /root/librdkafka-${LIBRDKAFKA_VERSION}.tar.gz https://github.com/edenhill/librdkafka/archive/v${LIBRDKAFKA_VERSION}.tar.gz && \
    tar -xzf /root/librdkafka-${LIBRDKAFKA_VERSION}.tar.gz -C /root && \
    cd /root/librdkafka-${LIBRDKAFKA_VERSION} && \
    ./configure && make && make install && make clean && ./configure --clean

ENV CPLUS_INCLUDE_PATH /usr/local/include
ENV LIBRARY_PATH /usr/local/lib
ENV LD_LIBRARY_PATH /usr/local/lib

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 3002

# run the command
ENTRYPOINT ["python3"]
CMD ["order.py"]