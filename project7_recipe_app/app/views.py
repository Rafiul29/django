from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#   return HttpResponse("this is home page")
  meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "description":"BeaverTails are a popular Canadian pastry known for their unique shape and delicious taste."
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "description":"Breakfast is often referred to as the most important meal of the day because it breaks the overnight fasting period, replenishes your supply of glucose, and provides other essential nutrients to keep your energy levels up throughout the day."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "description":"Canadian butter tarts are a classic Canadian dessert, known for their flaky pastry crust and sweet, gooey filling. They are simple to make and are a beloved treat across Canada."
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "description": "Montreal smoked meat is a beloved delicacy originating from Montreal, Quebec, known for its rich flavor and tender texture. It's similar to pastrami but has distinct spices and preparation methods. "
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "description":"Nanaimo bars are a classic Canadian no-bake dessert that features three delicious layers: a crumbly base, a creamy custard-flavored middle, and a rich chocolate topping. "
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "description":"Pâté chinois is a traditional Quebecois dish similar to shepherd's pie, consisting of a flavorful meat layer, a layer of creamed corn, and a topping of mashed potatoes. "
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "description":"Pouding chômeur, translating to s pudding, is a classic Quebecois dessert that originated during the Great Depression."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "description":"Poutine is a beloved Canadian dish that originated in Quebec and has gained popularity across the country and beyond."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "description":"Rappie pie, also known as râpure or rapure pie, is a traditional Acadian dish originating from the Maritime provinces of Canada, particularly Nova Scotia."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "description":"Split pea soup is a comforting and hearty dish made from dried split peas, vegetables, and often ham or bacon for added flavor"
        }
    ]

  return render(request,"index.html",{"meals":meals})
