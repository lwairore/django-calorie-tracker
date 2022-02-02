from calorie_tracker_app.models import ConsumeModel, FoodModel
from django.shortcuts import render

# Create your views here.
def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = FoodModel.objects.get(name=food_consumed)
        user = request.user
        consume = ConsumeModel(user=user, food_consumed=consume)
        consume.save()
        foods = FoodModel.objects.all()

    else:
        foods = FoodModel.objects.all()
    consumed_food = ConsumeModel.objects.filter(user=request.user)

    return render(request, 'calorie_tracker/index.html', {'foods': foods, 'consumed_food': consumed_food})
