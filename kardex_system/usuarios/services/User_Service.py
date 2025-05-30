from django.contrib.auth import login

#Responsable de registrar un usuarios
class UserService:
    def register_user(self, request, form):
        user = form.save()
        login(request, user)
        return user
