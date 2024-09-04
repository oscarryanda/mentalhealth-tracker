from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306217765',
        'name': 'Oscar Ryanda Putra',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
