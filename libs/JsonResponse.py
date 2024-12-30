from django.shortcuts import HttpResponse
from json import JSONEncoder, dumps
import datetime
from django.utils.deprecation import MiddlewareMixin


class DateEncoder(JSONEncoder):
    def default(self, obj):

        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return JSONEncoder.default(self, obj)

def ReTurn200(data):

    return HttpResponse(
        dumps({
            'code': 200,
            'data': data
        }, cls=DateEncoder)
    )


class DisableCSRF(MiddlewareMixin):
    def process_response(self, request, response):

        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "*"

        return response
