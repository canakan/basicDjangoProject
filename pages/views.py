from django.shortcuts import render

if __package__ is None or __package__ == '':
    # uses current directory visibility
    import Blogs
else:
    # uses current package visibility
    from blogs.models import Blogs

# Create your views here.


def index(request):
    blogs = Blogs.objects.all().order_by('-date_created')[:3]

    context = {
        'blogs': blogs,
    }

    return render(request, 'pages/index.html', context)
