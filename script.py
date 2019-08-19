#offset 1000

from minio import Minio
from minio.error import ResponseError

minioClient = Minio('192.168.1.18',
               access_key='123',
               secret_key='12345678',
               secure=False)
try:
    data = minioClient.get_partial_object('bucket', 'test (1).jpg', 1000)
    with open('iq-option.jpg', 'wb') as file_data:
        for d in data:
            file_data.write(d)
except ResponseError as err:
    print(err)
