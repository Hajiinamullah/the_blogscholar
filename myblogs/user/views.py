from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from .form import CustomPasswordChangeForm
from django.contrib.auth.views import PasswordResetCompleteView
from .models import UserProfile




@login_required
def user_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = request.POST
        user_profile.bio = form['bio']
        profile_picture = request.FILES.get('profile_picture', None)
        if profile_picture:
            user_profile.profile_picture = profile_picture
        user_profile.save()
        return redirect('user:user_profile')

    else:
        form = {
            'bio': user_profile.bio,
            'profile_picture': user_profile.profile_picture,
        }

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'profile.html', context)
# accounts/views.py
def signup_success(request):
    return render(request, 'signup_success.html')






def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Your custom user authentication logic here.
        user = custom_authenticate(username, password)

        if user is not None:
            login(request, user)
            return redirect('user:user_profile')  # Redirect to the index page after successful login
        else:
            # The provided credentials are invalid
            return render(request, 'login.html', {'error_message': 'Invalid login credentials. Please try again.'})

    return render(request, 'login.html')

def custom_authenticate(username, password):
    # Your custom authentication logic here.
    # You can use Django's built-in authenticate() function to check the credentials against the User model.
    user = authenticate(username=username, password=password)
    return user



def sign_up(request, profile_picture=None):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if User.objects.filter(username=username).exists():
            error_message = "Username already taken. Please choose a different one."
            return render(request, 'sign_up.html', {'error_message': error_message})
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        return redirect('user:login_user')
    return render(request, 'sign_up.html')

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('password_change_done')
        else:
            # Display individual field errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'resetpassword.html', {'form': form})


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
