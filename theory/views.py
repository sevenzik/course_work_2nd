from django.shortcuts import render


# Create your views here.
def theory_graphs(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'theory/theory_graphs.html',
                  context={'num_visits': num_visits},
                  )


def theory_gamilton(request):
    return render(request, 'theory/theory_gamilton.html')
