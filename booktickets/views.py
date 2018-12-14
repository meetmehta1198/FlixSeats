from django.shortcuts import render
from booktickets.models import Theatre,Movie,Show,City,C_city
from django.views.generic import ListView,DetailView
from django.urls.base import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required
@login_required
def Selection(request):
    
    if request.method=='POST':
        data=request.POST.get('city')
        request.session['city']=data
        return SelectTheatre(request)
    else:
        list=City.objects.all()
        return render(request,"select.html",{'list':list}) 
@login_required
def SelectTheatre(request):
    try:
        city=request.session['city']
        cities=City.objects.get(city_name=city)
        city=cities.city_id
        theatre=C_city.objects.filter(city_id=city)
        return render(request,'showTheatre.html',{'theatre':theatre})
    except Exception:
        return Selection(request)
def SelectMovie(request):

    list1={}
    id1=request.GET.get('id','')
    request.session['cinema_id']=id1
    print(id1)
    movie = Movie.objects.all()
    list1['h1']=movie
    list1['h2']=id1
    return render(request,'showMovies.html',list1)
def SelectShow(request):
    
    list2={}
    id2=request.GET.get('id','')
    request.session['movie_id']=id2
    show_data=Show.objects.filter(movie_id_id=id2)
    request.session['movie_id']=id2
    list2['data']=show_data
    list2['id2']=id2
    return render(request,'showDetails.html',list2)
def Seat(request):
    id3=request.GET.get('id','')
    th=request.session['cinema_id']
    mov=request.session['movie_id']
    theatre=Theatre.objects.filter(theatre_id=th)
    time=Show.objects.filter(show_id=id3)
    movies=Movie.objects.filter(movie_id=mov)
    
    return render(request,'seat.html',{'theatre':theatre,'movies':movies,'time':time})