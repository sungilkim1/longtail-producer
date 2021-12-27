from flask import Flask, render_template, request
from kafka import KafkaProducer
from confluent_kafka import Producer
import socket

import sqlite3
import sys
import json
import os, datetime
import logging

# logging.basicConfig(filename = "logs/test.log", level = logging.DEBUG)

app 	= Flask(__name__)

kafka_server = 'my-cluster-kafka-bootstrap.my-kafka-project:9092'
confluent_kafka_server = 'kafka.confluent.svc.cluster.local:9071'

@app.route('/')
def hello():
    return "sikim says its {0}".format(datetime.datetime.now())

@app.route('/order')
def orderTransaction():
	logging.info('order topic')
	producer 			= KafkaProducer(bootstrap_servers=kafka_server,
								value_serializer=lambda v: json.dumps(v).encode('utf-8')
						  )
	params_dict = request.args.to_dict()
	if len(params_dict) == 0:
		return 'No Parameter'

	params = {}
	for key in params_dict.keys():
		params[key] = request.args[key]

	producer.send('order', value=params)
	producer.flush()
	return 'Order added to queue';

@app.route('/corder')
def orderTransaction():
	logging.info('confluent order topic')
	conf = {'bootstrap.servers': "host1:9092,host2:9092",
			'client.id': socket.gethostname()}

	params_dict = request.args.to_dict()
	if len(params_dict) == 0:
		return 'No Parameter'

	params = {}
	for key in params_dict.keys():
		params[key] = request.args[key]

	producer.produce('order', value=params)
	producer.flush()
	
	return 'Confluent:Order added to queue';

@app.route('/dispatch')
def dispatchTransaction():
	logging.info('dispatch topic')
	producer 			= KafkaProducer(bootstrap_servers=kafka_server,
								value_serializer=lambda v: json.dumps(v).encode('utf-8')
						  )
	params_dict = request.args.to_dict()
	if len(params_dict) == 0:
		return 'No Parameter'

	params = {}
	for key in params_dict.keys():
		params[key] = request.args[key]

	producer.send('dispatch', value=params)
	producer.flush()
	return 'Dispatch added to queue';

@app.route('/delivery')
def deliveryTransaction():
	logging.info('delivery topic')
	producer 			= KafkaProducer(bootstrap_servers=kafka_server,
								value_serializer=lambda v: json.dumps(v).encode('utf-8')
						  )
	params_dict = request.args.to_dict()
	if len(params_dict) == 0:
		return 'No Parameter'

	params = {}
	for key in params_dict.keys():
		params[key] = request.args[key]

	producer.send('delivery', value=params)
	producer.flush()
	return 'Delivery added to queue';

@app.route('/charge')
def chargeTransaction():
	logging.info('charge topic')
	producer 			= KafkaProducer(bootstrap_servers=kafka_server,
								value_serializer=lambda v: json.dumps(v).encode('utf-8')
						  )
	params_dict = request.args.to_dict()
	if len(params_dict) == 0:
		return 'No Parameter'

	params = {}
	for key in params_dict.keys():
		params[key] = request.args[key]

	producer.send('charge', value=params)
	producer.flush()
	return 'Charge added to queue';

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3002)))

