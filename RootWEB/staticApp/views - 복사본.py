from django.shortcuts import render

# Create your views here.
def index(request) :
    print('>>>> static index')
    return render(request , 'nondynamic/index.html')

def line(request) :
    print('>>>> static line')
    installation = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
    context = {
        'installation' : installation
    }
    return render(request, 'nondynamic/line.html', context)

def bar(request) :
    print('>>>> static bar')

    return render(request , 'nondynamic/bar.html')
