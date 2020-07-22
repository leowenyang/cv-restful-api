#导入BosClient配置文件
import os
from .bos_sample_conf import config 

#导入BOS相关模块
from baidubce import exception
from baidubce.services import bos
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient

BUCKET = "yiballmdc"
OBJKEY = "cvman"

#新建BosClient
bos_client = BosClient(config)

def get_bos_file(file_prefix, bucket=BUCKET):
  objects = bos_client.list_all_objects(bucket, prefix=file_prefix)
  return objects

def upload_file_to_bos(file_name, bucket=BUCKET, object_key=OBJKEY):
  object_key = object_key + '/' + os.path.basename(file_name)
  bos_client.put_object_from_file(bucket, object_key, file_name)

def get_bos_file_url(file_name, bucket=BUCKET, object_key=OBJKEY):
  object_key = object_key + '/' + file_name
  url = bos_client.generate_pre_signed_url(bucket, object_key, expiration_in_seconds=-1)
  url = str(url, encoding = "utf8")
  if(url.find('?') >= 0):
    url = url[:url.find('?')]
  return url
