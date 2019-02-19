from django.shortcuts import render,redirect
from .models import Movie
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request,"movie/index.html",{"movies":movies})
    
def new(request):
    return render(request,"movie/new.html")
    
def create(request):

    title = request.POST.get("title")
    title_en = request.POST.get("title_en")
    audience = request.POST.get("audience")
    open_date = request.POST.get("open_date")
    genre = request.POST.get("genre")
    watch_grade = request.POST.get("watch_grade")
    score = request.POST.get("score")
    poster_url = request.POST.get("poster_url")
    description = request.POST.get("description")
    movie= Movie(title=title,title_en=title_en,audience=audience,open_date=open_date,genre=genre,watch_grade=watch_grade,
    score=score,poster_url=poster_url,description=description)
    movie.save()
    
    return redirect(f"/movies/{movie.id}/")
    
def read(request,id):
    movie = Movie.objects.get(pk=id)
    
    return render(request,"movie/read.html",{"movie":movie})
    
def edit(request,id):    
    movie = Movie.objects.get(pk=id)
    return render(request,"movie/edit.html",{"movie":movie})
    
def update(request,id):
    movie = Movie.objects.get(pk=id)
    
    title = request.POST.get("title")
    title_en = request.POST.get("title_en")
    audience = request.POST.get("audience")
    open_date = request.POST.get("open_date")
    genre = request.POST.get("genre")
    watch_grade = request.POST.get("watch_grade")
    score = request.POST.get("score")
    poster_url = request.POST.get("poster_url")
    description = request.POST.get("description")

    
    movie.title = title
    movie.title_en = title_en
    movie.audience = audience
    movie.open_date = open_date
    movie.genre = genre
    movie.watch_grade = watch_grade
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()
    
    return redirect(f"/movies/{id}/")

def delete(request,id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    
    return redirect("/movies")    