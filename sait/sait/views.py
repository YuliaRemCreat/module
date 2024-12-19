from django.shortcuts import render

def home(request):
    return render(request, 'third_task/page1.html')

def shop(request):
    items = {
        'item1': 'Игровая приставка',
        'item2': 'Игра 1',
        'item3': 'Игра 2',
    }
    return render(request, 'third_task/page2.html', {'items': items})

def cart(request):
    return render(request, 'third_task/page3.html')
