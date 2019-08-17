#offset 1000

from minio import Minio
from minio.error import ResponseError

minioClient = Minio('192.168.1.18',
               access_key='ASDsdadsafasfasfRFSAFS',
               secret_key='sdadsasdasfFGASFASFVvac',
               secure=False)
try:
    data = minioClient.get_partial_object('bucket', 'test (1).jpg', 1000)
    with open('my-testfile', 'wb') as file_data:
        for d in data:
            file_data.write(d)
except ResponseError as err:
    print(err)
