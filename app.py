from flask import Flask, request, jsonify
import logging
import sys
import os

import boto3

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)


@app.route("/")
def home():
    return "VPC Info API"


@app.route("/vpcinfo", methods=["GET"])
def vpcinfo():
    client = boto3.client('ec2')
    vpc_ids = client.describe_vpcs()
    return jsonify(vpc_ids["Vpcs"][0])


if __name__ == '__main__':

    aaki = os.getenv("AWS_ACCESS_KEY_ID")
    app.logger.info(aaki)
    app.run(debug=True)
