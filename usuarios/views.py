from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth #-> Lib do django que já se importa com as autenticações de login (verificação de db, etc)
from django.contrib import messages #-> Lib do django que facilita a entrada de mensagens de erro, sucesso, etc

def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()
        
        #o usuário será autenticado
        
        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )
        #Se o usuario não é vazio ou nulo, ele faz a autenticação, loga e redireciona para a página index
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado com sucesso!")
            return redirect('index')
        else:
        #Se não, irá ser redecionado para a página de login (permanecendo na mesma página)
            messages.error(request, "Erro ao efetuar o login!")
            return redirect('login') 
            
    
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, "Senhas não são iguais!")
                return redirect('cadastro')
            
            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, "O username já existe em nosso banco de dados")
                return redirect('cadastro')
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Usuario cadastrado com sucesso!")
            return redirect('login')
            
    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout Efetuado com sucesso!")
    return redirect("login")