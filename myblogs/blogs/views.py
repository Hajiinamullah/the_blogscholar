from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View

from .models import blogs
from django.shortcuts import render, get_object_or_404, redirect
from .models import blogs, Comment
# from myblogs.user.views import user_login, custom_authenticate

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http.response import HttpResponse



# from ..user.views import custom_authenticate


def create_blog(request):
    if request.method == 'POST':
        image_url = request.FILES.get('image')
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        post_date = request.POST.get('post_date')

        blog_post = blogs(image=image_url, title=title, detail=detail, post_date=post_date)
        blog_post.save()

        return redirect('blogs:blogg')  # Assuming you have a URL pattern named 'all_posts' to display all blog posts

    return render(request, 'upload_blog.html')
def blogg(request):
    blogs_data = blogs.objects.all()
    contaxt = {
        'blogs': blogs_data,
    }
    return render(request, 'blogs.html',contaxt)

def blog_detail(request, id):
    blog = get_object_or_404(blogs, id=id)
    comments = blog.comments.all()  # Use the correct related name for comments
    return render(request, 'detail.html', {'blog': blog, 'comments': comments})


# ... your other views ...


# ... your other views ...

@login_required(login_url='blogs:user_login')  # Redirect to the login page if the user is not authenticated
def comment_submit(request, blog_id):
    blog = get_object_or_404(blogs, id=blog_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        if comment_text:
            comment = Comment(blog=blog,
                              user=request.user,
                              comment_text=comment_text,
                              created_at=timezone.now())
            comment.save()

    return redirect('blogs:comment_form', blog_id=blog_id)

def comment_form(request, blog_id):
    blog = get_object_or_404(blogs, id=blog_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        if comment_text:
            comment = Comment(blog=blog, user=request.user, comment_text=comment_text)
            comment.save()
            return redirect('blogs:comment_form', id=blog_id)  # Redirect to the blog_detail page

    else:
        # If it's a GET request, create an empty form to display on the page
       pass

    return render(request, 'detail.html', {'blog': blog, })
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Your custom user authentication logic here.
        from myblogs.user.views import custom_authenticate
        user = custom_authenticate(username, password)

        if user is not None:
            login(request, user)
            return redirect('comment_form')  # Redirect to the index page after successful login
        else:
            # The provided credentials are invalid
            return render(request, 'login.html', {'error_message': 'Invalid login credentials. Please try again.'})

    return render(request, 'login.html')


def blog_list(request):
    blog_posts2 = blogs.objects.all().order_by('-post_date')  # Order the posts by the most recent first
    # Number of blogs to display per page
    items_per_page = 9

    paginator = Paginator(blog_posts2, items_per_page)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_obj = paginator.page(1)

    return render(request, 'blogs.html', {'page_obj': page_obj})