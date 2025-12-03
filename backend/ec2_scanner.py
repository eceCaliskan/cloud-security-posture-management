def ec2_ip_check(ec2_instance) :
    """
    Check if the the IP adress is exposed publicly. If so retun a warning message.
    """ 
    public_ip = ec2_instance.get('PublicIpAddress')
    if public_ip:
        ec2_instance['PubliclyExposed'] = True
        print(f"Instance {ec2_instance.get('InstanceId')} is publicly exposed with IP {public_ip}."f"Please review and configure the security groups carefully to avoid unintended exposure.")
    else:
        ec2_instance['PubliclyExposed'] = False