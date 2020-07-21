import boto3
import sys
import os

def main():
    if (len(sys.argv) < 6):
        print ('Error: Required 5 arguments.')
        # Checks for 6 because the script path is in position 0. So len is 6
        # for 5 arguments.
        sys.exit(1)

    print(os.getcwd())

    sourceDir = os.getcwd()

    upload_file_names = []
    for (sourceDir, dirname, filename) in os.walk(sourceDir):
        # print(filename)
        upload_file_names.extend(filename)
        break

    # upload_file_names.remove('.DS_Store')
    # upload_file_names.remove('test.py')
    # upload_file_names.remove('.gitattributes')
    print(upload_file_names)

    bucket_name=sys.argv[1]
    aws_key=sys.argv[2]
    aws_access_key=sys.argv[3]
    aws_access_secret=sys.argv[4]
    local_path=sys.argv[5]

    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_access_secret,
    )
    client = session.client('s3')

    for file_name in upload_file_names:
        response = client.upload_file(
            Filename=file_name,
            Bucket=bucket_name,
            Key=file_name,
            ExtraArgs={'ContentType':'text/html'}
        )
    print ('Done uploading')


main()