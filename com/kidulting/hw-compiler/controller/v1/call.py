from flask_restplus import Namespace, fields

api = Namespace('call', description='RESTfull call to HW-Compiler services controller')

call_result_fields = api.model('model_fields', {
    # 'key' : fields.~~~
})

call_request_fields = api.model('model_fields', {
    # 'key' : fields.~~~
})