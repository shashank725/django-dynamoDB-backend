from django.db import models

# Marshmallow example
import os
from dynamorm import DynaModel, GlobalIndex, ProjectAll
from marshmallow import fields, validate, validates, ValidationError

# Create your models here.

class Thing(DynaModel):
    class Table:
        name = 'things'
        hash_key = 'id'
        read = 5
        write = 1

    class ByColor(GlobalIndex):
        name = 'by-color'
        hash_key = 'color'
        read = 5
        write = 1
        projection = ProjectAll()

    class Schema:
        id = fields.String(required=True)
        name = fields.String()
        color = fields.String(validate=validate.OneOf(('purple', 'red', 'yellow')))
        compound = fields.Dict(required=True)

        @validates('name')
        def validate_name(self, value):
            # this is a very silly example just to illustrate that you can fill out the
            # inner Schema class just like any other Marshmallow class
            if name.lower() == 'evan':
                raise ValidationError("No Evan's allowed")

    def say_hello(self):
        print("Hello.  {name} here.  My ID is {id} and I'm colored {color}".format(
            id=self.id,
            name=self.name,
            color=self.color
        ))