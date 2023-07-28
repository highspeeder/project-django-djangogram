from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password

is_singup = False


class Signup(APIView):
    def get(self, request):
        is_singup = True
        return render(request, "user/singup.html", {'is_singup': is_singup})

    def post(self, request):
        email = request.POST['email']
        nickname = request.POST['nickname']
        name = request.POST['name']
        password = request.POST['password']

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image='default_profile.png')

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        is_singup = False
        return render(request, "user/login.html", {'is_singup': is_singup})

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=404, data=dict(message='회원정보가 잘못되었습니다.'))

        if user.check_password(password):
            # 세션 or 쿠키에 정보를 넣는다.
            request.session['email'] = email
            return Response(status=200)
        else:
            return Response(status=404, data=dict(message='회원정보가 잘못되었습니다.'))