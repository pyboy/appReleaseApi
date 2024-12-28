from django.views.generic import View
from libs.JsonResponse import ReTurn200

class LoginView(View):

    def post(self, request):
        return ReTurn200({"msg": "登录成功"})
    def put(self, request):
        return ReTurn200({"msg": "登录成功"})