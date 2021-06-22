import json
from django.http import JsonResponse
from django.views import View
from owners.models import Owner, Dog

# Create your views here.

class OwnersView(View): 
    def post(self, request): 
        data  = json.loads(request.body)
        owner = Owner.objects.create(
            name  = data['name'],
            email = data['email'],
            age   = data['age']
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request): 
        owners  = Owner.objects.all()
        results = []
        for owner in owners:
            dogs = owner.dog_set.all()
            dog_list = []
            for dog in dogs:
                dog_name_age = {
                    'name': dog.name,
                    'age': dog.age
                }
                dog_list.append(dog_name_age)
            results.append(
                {
                    'name' : owner.name,
                    'email': owner.email,
                    'age'  : owner.age,
                    'pets' : dog_list
                }
            )
        return JsonResponse({'Results':results}, status=200)


class DogsView(View): 
    def post(self, request): 
        data = json.loads(request.body)
        dog  = Dog.objects.create(
            name  = data['name'],
            age   = data['age'],
            owner = Owner.objects.get(name=data['owner'])
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:

            results.append(
                {
                    'name' : dog.name,
                    'age' : dog.age,
                    'owner' : dog.owner.name,
                }
            )
        return JsonResponse({"Results":results}, status=200)
