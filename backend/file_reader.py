import json
from ec2_scanner import ec2_ip_check, ec2_open_ports_check, mfa_check
from collections import defaultdict

# Path to mock AWS data
FILE_PATH = '../data/mock_aws_data_100.json'

def start_ec2_scanner():
    """
    Load AWS mock data, group resources by account, 
    and scan EC2 instances for public IP exposure.
    """
    # Load the JSON data
    with open(FILE_PATH, encoding="utf-8") as file:
        aws_data = json.load(file)

    
    account_ids = set(item.get("AccountId", "UnknownAccount") for item in aws_data)

  
    grouped_data = defaultdict(list)
    for item in aws_data:
        account_id = item.get("AccountId", "UnknownAccount")
        grouped_data[account_id].append(item)

   
    for account_id in account_ids:
        print('-----------------------------------------')
        print(f"\n 🔍 Scanning EC2 instances for Account: {account_id}: \n")
        for resource in grouped_data[account_id]:
            if resource.get("Type") == "EC2":
                ec2_ip_check(resource)  
            if resource.get("Type") == "SecurityGroup":
                ec2_open_ports_check(resource)
            if resource.get("Type") == "IAM":
                mfa_check(resource)
            

if __name__ == "__main__":
    start_ec2_scanner()
