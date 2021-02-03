from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # create new user.
        # is form valid ?
        if form.is_valid():
            # create user account
            form.save() # save the user.
            username = form.cleaned_data.get('username')
            # pop up message
            messages.success(request, f'Account created for {username}!')
            # after creating user, return to home.
            return redirect('blog-home')
            
    else: # if condtion not met, return blank form.
        form = UserRegisterForm() 
    return render(request, 'users/register.html', {'form': form})

    