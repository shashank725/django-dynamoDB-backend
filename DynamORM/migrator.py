import boto3

from models import *

dynamodb = boto3.resource('dynamodb',
                            # aws_access_key_id='94c6w',
                            # aws_secret_access_key='goloq',  
                            region_name='us-east-2', 
                            endpoint_url='http://localhost:8000')
print(list(dynamodb.tables.all()))  # --> ['table1', 'table2', 'etc...']

# MyModel.Table.get_resource(
#     aws_access_key_id="eoi99p",
#     aws_secret_access_key="bstj3",
#     region_name="us-east-2",
#     endpoint_url="http://localhost:8000"
# )

print("HEY")
# Creating new documents
thing = Thing(id="thing1", name="Thing One", color="purple", unknown=None)
thing.save()