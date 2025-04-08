from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

def index(request):
    return render(request, 'main/index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('loginEmail')
        password = request.POST.get('loginPassword')

        # Buscar el usuario por email
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Correo o contraseña incorrectos, o el usuario no existe. Por favor intente nuevamente...")
            return redirect('login')

    return render(request, 'main/login.html')


def registro(request):
    if request.method == "POST":
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        id_number = request.POST['idNumber']
        id_front = request.FILES.get('idFront')
        id_back = request.FILES.get('idBack')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        postal_code = request.POST['postalCode']
        city = request.POST['city']
        province = request.POST['province']
        country = request.POST['country']
        phone = request.POST['phone']

        # Validaciones
        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('registro')

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect('registro')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Ya existe una cuenta con este correo electrónico.")
            return redirect('registro')

        # Crear usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Crear perfil
        Profile.objects.create(
            user=user,
            id_number=id_number,
            id_front=id_front,
            id_back=id_back,
            address1=address1,
            address2=address2,
            postal_code=postal_code,
            city=city,
            province=province,
            country=country,
            phone=phone,
        )

        messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
        return redirect('login')

    return render(request, 'main/registro.html')


def contacto(request):
    return render(request, 'main/contacto.html')


def pagos(request):
    return render(request, 'main/pagos.html')


def retiros(request):
    return render(request, 'main/retiros.html')


def logout_view(request):
    auth_logout(request)
    return redirect('login')


@login_required
def area_cliente(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if created:
        messages.info(request, "Tu perfil fue creado automáticamente. Completa o actualiza tus datos.")

    return render(request, 'main/area_cliente.html', {'profile': profile})