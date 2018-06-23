import sys
try:
    import boto3
    print"Sucessfully imported boto3"
except Exception as e:
    print"The error is: ",e
    sys.exit(1)
bucket = raw_input("Enter bucket name to create: ")
print"creating a  bucket   %s ..............." %(bucket)
s3 = boto3.resource('s3')
try:
    s3.create_bucket(Bucket=bucket,ACL='private') 
    print"The %sis sucessfully created with private permission"%(bucket)
    sys.exit(0)
except Exception as e:
    print"The error is: ",e
    sys.exit(2)
