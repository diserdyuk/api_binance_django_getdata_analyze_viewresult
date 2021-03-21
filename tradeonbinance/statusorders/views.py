from django.shortcuts import render, redirect

from statusorders.models import StatusOrder, Config


def orders_page(request):
    size_position = Config.objects.get(name='size_position')
    percent_deviation = Config.objects.get(name='percent_deviation')

    data = {
        'orders': StatusOrder.objects.all(), 
        'size_position': size_position.value,
        'percent_deviation': percent_deviation.value,
    }

    return render(request, 'index.html', data)


def update_config(request):
    size_position = Config.objects.get(name='size_position')
    size_position.value = request.POST['size_position']
    size_position.save()

    percent_deviation = Config.objects.get(name='percent_deviation')
    percent_deviation.value = request.POST['percent_deviation']
    percent_deviation.save()

    return redirect('/')
