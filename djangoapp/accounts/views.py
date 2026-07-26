from django.shortcuts import render, redirect

def view_entrada(request):
    if request.user.is_authenticated:
        return redirect('accounts:perfil_proprio')
    return render(request, 'accounts/index.html')

def perfil_proprio(request):
    return render(request, 'accounts/config.html') # Ou outro template de perfil que você tenha
