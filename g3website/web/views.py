
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, FileResponse, HttpResponse
from .models import material, notice
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    """Render the home page."""
    return render(request, "index.html")

def subjects(request):
    """Render the subjects page."""
    return render(request, "subjects.html")

def types(request, subject):
    """Render the types page for a given subject."""
    context = {"subject": subject}
    return render(request, "types.html", context)

def materials(request, subject1, types1):
    """Display materials filtered by subject and type, with pagination."""
    sub = {
        "physics": "PHY",
        "mathematics": "MAT",
        "basic electrical": "BEE",
        "ecology and environment": "ECO",
        "sociology and professional ethics": "SOC",
    }
    typ = {
        "syllabus": "SYL",
        "notes": "NOT",
        "books": "BKS",
        "pyq": "PYQ",
        "all": "OTH",
    }
    if typ[types1] == "OTH":
        material_object = material.objects.filter(subject=sub[subject1]).all().order_by("-timestamp")
    else:
        material_object = material.objects.filter(subject=sub[subject1], types=typ[types1]).all()

    page = request.GET.get('page', 1)
    paginator = Paginator(material_object, 8)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    context = {"subject": subject1, "types": types1, "materials": posts}
    return render(request, "material.html", context)
def pdf_view(request, pdf):
    """Render the PDF view page for a given PDF file."""
    context = {"pdf": pdf}
    return render(request, "pdf.html", context)



def gallery(request):
    """Render the gallery page."""
    return render(request, "gallery.html")

def search_post(request):
    """Handle search requests for materials and notices."""
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = material.objects.filter(
            Q(title__icontains=search_query) |
            Q(subject__icontains=search_query) |
            Q(desc__icontains=search_query) |
            Q(types__icontains=search_query) |
            Q(timestamp__icontains=search_query) |
            Q(file__icontains=search_query)
        )
        notices = notice.objects.filter(
            Q(title__icontains=search_query) |
            Q(timestamp__icontains=search_query) |
            Q(desc__icontains=search_query) |
            Q(file__icontains=search_query)
        )
        return render(request, "search_post.html", {"query": search_query, "posts": posts, "notices": notices})
    else:
        return render(request, "search_post.html", {})
    

def notice_view(request):
    """Display notices with pagination."""
    notice_object = notice.objects.all().order_by("-timestamp")
    page = request.GET.get('page', 1)
    paginator = Paginator(notice_object, 8)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {"materials": posts}
    return render(request, "notice.html", context)
    

def gdrive(request, subject):
    """Redirect to the Google Drive folder for the given subject."""
    links = {
        "physics": "https://drive.google.com/drive/folders/1KlBGSDrC0qVnzawxqDPkgSeqa1dGAyjR?usp=drive_link",
        "mathematics": "https://drive.google.com/drive/folders/1cEXXhMKCHrBXDmpaJPaRal3T1XO6z6AO?usp=drive_link",
        "basic electrical": "https://drive.google.com/drive/folders/12Ie9a-rSyoNFMndIyrW0K4rSRsNLHpbO?usp=drive_link",
        "ecology and environment": "https://drive.google.com/drive/folders/1YSrIP2uLK7IqlcwzURzLoQOYOGTwqjB5?usp=drive_link",
        "sociology and professional ethics": "https://drive.google.com/drive/folders/11-U67eVbl-Bpxtraex__nHGMnOwMpG1M?usp=drive_link",
    }
    return redirect(links[subject])


def social(request, app1):
    """Redirect to the social media page for the given app."""
    links = {
        "wpunofficial": "",
        "wpofficial": "",
    }
    return redirect(links[app1])
