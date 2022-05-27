from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import DetailView, DeleteView
from .forms import registerForm, postForm, updateProfile, registerCustom, calculatorForm, updateForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.forms import User
from django.contrib import messages


@login_required(login_url='/login')
def homePage(request):
    post = Post.objects.all()
    return render(request, 'app/home.html', {'posts': post})


def profilePage(request):
    if request.method == 'POST':
        form = updateProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            print('ok')
            form.save()
            return redirect('profile')
    else:
        form = updateProfile()
        context = {'form': form}
    return render(request, 'app/profile.html', context)


def registerPage(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register successfully !')
            return redirect('/login')
    else:
        form = registerForm()
    return render(request, 'app/register.html', {'form': form})


def postPage(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            body = request.POST.get('body')
            user = User.objects.filter(username=request.user.username).first()
            post = Post.objects.create(title=title, body=body, author=user)
            post.save()
            return redirect('home')
    else:
        form = postForm()

    return render(request, 'app/post.html', {'form': form})


class postview(DetailView):
    model = Post



def register(request):
    if request.method == 'POST':
        form = registerCustom()
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        if User.objects.filter(username=username).first():
            messages.error(request, 'Username already existed')

        elif len(password) < 8 and len(password2) < 8:
            messages.error(request, 'Your password is too weak at least 8 character up !')
            return redirect('/reg')
        else:
            if password == password2:
                user = User.objects.create(username=username, password=password)
                user.save()
                messages.success(request, 'Register successfully !')
                return redirect('/login')
            else:
                messages.error(request, 'Password is not match')
                return redirect('/reg')
    else:
        form = registerCustom()
    return render(request, 'app/register.html', {'form': form})


@login_required(login_url='/login')
def calculaotrpage(request):
    if request.method == 'POST':
        form = calculatorForm(request.POST)
        if form.is_valid():
            number = request.POST['number']
            number2 = request.POST['number2']
            result = int(number) + int(number2)
            print(result)
            context = {'form': form, 'result': result}
            return render(request, 'app/calculator.html', context)
    else:
        form = calculatorForm()

    return render(request, 'app/calculator.html', {'form': form})


@login_required(login_url='/login')
def posteditpage(request, pk):
    if request.method == 'POST':
        try:
            updateForm()
            title = request.POST['title']
            body = request.POST['body']
            user = User.objects.filter(username=request.user.username).first()
            post = Post.objects.get(id=pk, author=user)
            post.title = title
            post.body = body
            post.save()
            return redirect('/post/' + str(pk))
        except:
            return redirect('/')
    else:
        form = updateForm()
    return render(request, 'app/update-profile.html', {'form': form})


class deletpost(DeleteView):
    model = Post
    success_url = '/'


def test(request):
    post = Post.objects.filter(id=21,author=request.user.username)
    print(post)


def delete_view(request, id):
    obj = get_object_or_404(Post,id=id)
    if obj.author.id == request.user.id:
        if request.method == 'POST':
            print(3)
            obj.delete()
            return redirect("/")
        return render(request, "app/post_confirm_delete.html")
    return redirect('/')