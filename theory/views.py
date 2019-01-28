from django.shortcuts import render


# Create your views here.
def theory_graphs(request):
    return render(request, 'theory/theory_graphs.html')


def theory_gamilton(request):
    return render(request, 'theory/theory_gamilton.html')

