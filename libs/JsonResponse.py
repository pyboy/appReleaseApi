from django.shortcuts import HttpResponse
from json import JSONEncoder, dumps
import datetime

class DateEncoder(JSONEncoder):
    def default(self, obj):

        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return JSONEncoder.default(self, obj)

def ReTurn200(data, msg=None):

    return HttpResponse(
        dumps({
            'code': 200,
            'data': data,
            'msg': msg
        }, cls=DateEncoder)
    )
