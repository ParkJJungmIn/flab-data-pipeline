import boto3
import sys
import datetime

def upload_file_to_s3(bucket_name, file_path, object_name=None):
    if object_name is None:
        object_name = file_path

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_path, bucket_name, object_name)
    except Exception as e:
        print(e)
        return False
    return True

if __name__ == "__main__":
    # 테라폼으로 S3를 구축하면 아래와 같은 파일로 해당 버킷 네임변수가 export됨
    config_path = '../terraform/bucket_config.txt'
    with open(config_path, 'r') as file:
        bucket_name = file.readline().strip().split('=')[1]

    # eventsim에서 생성한 데이터 이름을 적어줘야 함.
    file_path = '../eventsim/data/test_eventsim.csv'
    
    object_name = f'bronze/event_data.csv'

    success = upload_file_to_s3(bucket_name, file_path, object_name)
    if success:
        print(f'File {file_path} uploaded to {bucket_name}/{object_name}')
    else:
        print('Upload failed')
