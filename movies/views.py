import json
from django.http import JsonResponse
from django.views import View
from movies.models import Actor, Movie
# Create your views here.

class ActorViews(View):
    # def post(self, request):
    #     data = json.loads(request.body)
    #     actor = Actor.objects.create(
    #         {
    #             'first_name': data['first_name'],
    #             'last_name': data['last_name'],
    #             'date_of_birth': data['date_of_birth'],
    #         }
    #     )
    #     return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
    
    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            titles = []
            t = actor.movies.values('title')
            for i in range(len(t)):
                titles.append(t[i]['title'])
            results.append(
                {
                    'first_name' : actor.first_name,
                    'last_name': actor.last_name,
                    'movies' : titles
                }
            )
        return JsonResponse({'Results':results}, status=200)

class MovieViews(View):
    # def post(self, request):
    #     data = json.loads(request.body)
    #     movie = Movie.objects.create(
    #         {
    #             'title': data['title'],
    #             'release_date': data['release_date'],
    #             'running_time': data['running_time'],
                
    #         }
    #     )
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            actors=[]
            m = movie.actors.values_list('first_name', 'last_name')
            for i in range(len(m)):
                name = f'''{m[i][0]} {m[i][1]}'''
                actors.append(name)
            results.append(
                {
                    'title' : movie.title,
                    'running_time': movie.running_time,
                    'actors' : actors
                }
            )
        return JsonResponse({'Results':results}, status=200)
