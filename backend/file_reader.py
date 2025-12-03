
import json
from ec2_scanner import ec2_ip_check 

EC2_INSTANCES = []
FILE_PATH = '../data/mock_aws_data_100.json'

def start_scanner():
    with open(FILE_PATH, encoding="utf-8") as awsMockJsonData:
        data = json.load(awsMockJsonData)
        for item in data:
            if item.get('Type') == 'EC2':
                ec2_ip_check(item) # Call the function to check IP exposure
            
 