from django.contrib.auth import authenticate, login, logout

#Responsable de la la autenticacion de los usuarios
#Valida si el usuarios es valido y inicia la sesion
class AuthService:
    def login_user(self, request, username, password):
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return user
        return None

    def logout_user(self, request):
        logout(request)
