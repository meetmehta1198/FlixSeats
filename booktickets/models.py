from django.db import models

class Theatre(models.Model):
    
    theatre_id=models.CharField(max_length=10,primary_key=True)
    theatre_name=models.CharField(max_length=10)
    location=models.CharField(max_length=10)
    #movie=models.ForeignKey(Movie,related_name='movie_list',on_delete=models.CASCADE)
class Movie(models.Model):
    
    movie_id=models.CharField(max_length=10,primary_key=True)
    movie_name=models.CharField(max_length=60)
    director=models.CharField(max_length=20)
    cast=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    duration=models.CharField(max_length=100)
    theatre=models.ForeignKey(Theatre,related_name='theatre',on_delete=models.CASCADE)

    
class Show(models.Model):
    show_id=models.IntegerField(primary_key=True)
    theatre_id=models.ForeignKey(Theatre,related_name='cinema',on_delete=models.CASCADE)
    movie_id=models.ForeignKey(Movie,related_name='movie',on_delete=models.CASCADE)
    time=models.TimeField()

class City(models.Model):
    city_id=models.CharField(max_length=30,primary_key='true')
    city_name=models.CharField(max_length=50)
    
class C_city(models.Model):
    city_id=models.ForeignKey(City,related_name='city',on_delete='true')
    theatre_id=models.ForeignKey(Theatre,related_name='theatre1',on_delete=models.CASCADE)
    
