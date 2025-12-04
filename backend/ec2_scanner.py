from datetime import datetime
def ec2_ip_check(ec2_instance) :
    """
    Check if the the IP adress is exposed publicly. If so retun a warning message.
    """ 
    public_ip = ec2_instance.get('PublicIpAddress')
    if public_ip:
        ec2_instance['PubliclyExposed'] = True
        print(f"🚨 Instance {ec2_instance.get('InstanceId')} is publicly exposed with IP {public_ip}."
                    f"Please review and configure the security groups carefully to avoid unintended exposure.")
    else:
        ec2_instance['PubliclyExposed'] = False

def ec2_open_ports_check(ec2_instance):
    """
    """
    ipPermissions = ec2_instance.get('IpPermissions')
    for permissionRule in ipPermissions:
        ip_ranges = permissionRule.get('IpRanges')
        for range in ip_ranges:
            if range.get('CidrIp') == "0.0.0.0/0":
                print( f"🚨 EC2 instance {ec2_instance.get('InstanceId')} has security group {ec2_instance.get('GroupId')} "
                                    f"exposing port {permissionRule.get('FromPort')}-{permissionRule.get('ToPort')} to the entire internet (0.0.0.0/0). "
                                    f"Please restrict the CIDR range.")

def mfa_check(ec2_instance):
    """
    Check if the Multi Factor Authentication is enabled for IAM User
    """
    isMFAenabled= ec2_instance.get('MFAEnabled')
    if isMFAenabled == False:
        print(f"🚨 IAM User '{ec2_instance.get('UserName')} - {ec2_instance.get('UserId')}' does not have MFA enabled.")
    
def active_key_duration_check(ec2_instance):
    """
    Check if the key is active more than 90 days
    """
    accessKeys = ec2_instance.get('AccessKeys')
    for accessKey in accessKeys:
        if accessKey.get('Status') == 'Active':
            date_now = datetime.now()
            date_access_key_generated = datetime.strptime(accessKey.get('CreateDate'), "%Y-%m-%dT%H:%M:%SZ")
            if ((date_now - date_access_key_generated).total_seconds() / (24 * 3600)) > 90:
                print(f"🚨 IAM User '{ec2_instance.get('UserName')} - {ec2_instance.get('UserId')}' "
                                    f"Access key is active more than 90 days")
              