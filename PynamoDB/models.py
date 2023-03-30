from django.db import models

# Create your models here.

"""
An example using Amazon's Thread example for motivation
http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SampleTablesAndData.html
"""

import logging
from pynamodb.models import Model
from pynamodb.attributes import (
    ListAttribute, UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
)
from datetime import datetime

logging.basicConfig()
log = logging.getLogger("pynamodb")
log.setLevel(logging.DEBUG)
log.propagate = True


class Thread(Model):
    class Meta:
        table_name = 'Thread'
        # Specifies the region
        region = 'us-east-2'
        # Optional: Specify the hostname only if it needs to be changed from the default AWS setting
        host = 'http://localhost:8000'
        # Specifies the write capacity
        write_capacity_units = 10
        # Specifies the read capacity
        read_capacity_units = 10
    forum_name = UnicodeAttribute(hash_key=True)
    subject = UnicodeAttribute(range_key=True)
    views = NumberAttribute(default=0)
    replies = NumberAttribute(default=0)
    answered = NumberAttribute(default=0)
    tags = UnicodeSetAttribute()
    last_post_datetime = UTCDateTimeAttribute(null=True)
    notes = ListAttribute(default=list)  # type: ignore  # todo: add ability for basic list types



# A model that uses aliased attribute names
class AliasedModel(Model):
    class Meta:
        table_name = "AliasedModel"
        host = "http://localhost:8000"
    forum_name = UnicodeAttribute(hash_key=True, attr_name='fn')
    subject = UnicodeAttribute(range_key=True, attr_name='s')
    views = NumberAttribute(default=0, attr_name='v')
    replies = NumberAttribute(default=0, attr_name='rp')
    answered = NumberAttribute(default=0, attr_name='an')
    tags = UnicodeSetAttribute(attr_name='t')
    last_post_datetime = UTCDateTimeAttribute(attr_name='lp')


