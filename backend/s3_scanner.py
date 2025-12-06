def s3_access_check(s3_instance):
    access_grants = s3_instance.get('Acl').get('Grants')
    for access_grant in access_grants:
        if access_grant.get('Grantee').get('URI') == "http://acs.amazonaws.com/groups/global/AllUsers":
             print(f"🚨 Bucket {s3_instance.get('BucketName')} is exposed to AllUsers with "
                        f"{access_grant.get('Permission')} permission"
              )

def s3_encryption_check(s3_instance):
    if s3_instance.get('Encryption') == None:
         print(f"🚨 Bucket {s3_instance.get('BucketName')} data is not encrypted "
              )

  