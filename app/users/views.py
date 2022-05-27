from django.shortcuts import render, redirect
from .forms import registerForm, userUpdate, updateProfile
from django.views.generic import DetailView
from app.models import Post
from django.contrib.auth.decorators import login_required

def registerPage(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            print('ok')
            return redirect('login')
    else:
        form = registerForm()
    return render(request, 'users/register.html', {'form': form})


def userpage(request):
    if request.method == 'POST':
        form = userUpdate(request.POST, instance=request.user)
        form1 = updateProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() or form1.is_valid():
            form.save()
            form1.save()
            return redirect('profile')
    else:
        form = userUpdate()
        form1 = updateProfile()
    context = {'form': form,
               'form1': form1}
    return render(request, 'users/profile.html', context)
def updatePost(request):
    if request.method == 'POST':
        form = Post(request.POST,)
class viewDetail(DetailView):
    model = Post
