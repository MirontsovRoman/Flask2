from marshmallow import Schema, fields, validate


class AuthorSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True, error_messages={'required': {
                      'message': 'name is required', 'code': 400}})
    email = fields.Email(required=True, error_messages={
                       'required': 'email is required'})
    
    
class LearnerSchema(Schema):
    uid = fields.Integer()
    name = fields.Str(
        required=True,
        error_messages={
            'required': {
                'message': 'name is requided',
                'code': 400
            }
        },
        validate=[validate.Length(max=50)]
    )
    final_test = fields.Boolean(required=True, error_messages={
        'required': 'final_test is required'})    
