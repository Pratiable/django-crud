import json
from django.http import JsonResponse
from django.views import View
from movies.models import Actor, Movie, ActorMovie
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
            results.append(
                {
                    'first_name' : actor.first_name,
                    'last_name': actor.last_name,
                    'movies' : list(actor.actors.values('title'))
                }
            )
        return JsonResponse({'Results':results}, status=200)

class MovieViews(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            results.append(
                {
                    'title' : movie.title,
                    'running_time': movie.running_time,
                    'actors' : list(movie.actors.values('first_name'))
                }
            )
        return JsonResponse({'Results':results}, status=200)
