from crypt import methods
from http import client
from operator import methodcaller
from config import config
from flask import Flask, request, jsonify
from configparser import ConfigParser
import logging
import boto3

app = Flask(__name__)

logging.basicConfig(
    filename=config['log_file'], 
    level=config['log_level']
)


@app.route('/ec2/list', methods=['GET'])
def get_instance_id():

    client = boto3.client('ec2',
    aws_access_key_id= request.args.get("aws_access_key_id"),
    aws_secret_access_key= request.args.get("aws_secret_access_key"),
    region_name= request.args.get("region_name")
)

    response = client.describe_instances(
    Filters=[
        
    ]
)

    InstanceIds = []

    for i in range(len(response['Reservations'])):
        InstanceIds.append(response['Reservations'][i]['Instances'][0]['InstanceId'])


    return jsonify(InstanceIds)

@app.route('/ec2/start', methods=['GET'])
def start_instance():

    client = boto3.client('ec2',
    aws_access_key_id= request.args.get("aws_access_key_id"),
    aws_secret_access_key= request.args.get("aws_secret_access_key"),
    region_name= request.args.get("region_name")
    )

    IDS = request.args.get("InstanceIds").split(',')

    for j in IDS:
        response = client.start_instances(
                InstanceIds=[ j,
                ]   
        )   

    return jsonify(response)


@app.route('/ec2/stop', methods=['GET'])
def stop_instance():
    
    client = boto3.client('ec2',
    aws_access_key_id= request.args.get("aws_access_key_id"),
    aws_secret_access_key= request.args.get("aws_secret_access_key"),
    region_name= request.args.get("region_name")
    )

    IDS = request.args.get("InstanceIds").split(',')

    for x in IDS:
        response = client.stop_instances(
        InstanceIds=[x,
        ]
    )

    return jsonify(response)

if __name__ == "__main__":
    app.run(host=config["host"], port=config["port"], debug=True)




