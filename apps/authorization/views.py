from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username, password=password)
        return JsonResponse({"message": "Registrado com sucesso!"})


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login bem-sucedido!"})
        return JsonResponse({"error": "Nome de usuário ou senha incorretos."}, status=400)


def logout_view(request):
    logout(request)
    return redirect('/siom/login-page/')
