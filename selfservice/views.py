from django.shortcuts import render
from django.http import HttpResponse
from .fmnquery import run_query

def index(request):
    return render(request, 'home.html')

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            searchresult = run_query(search_id)
            html = "<H1>{}</H1>".format(searchresult)
            return HttpResponse(html)
        except:
            return HttpResponse("search failed")
    else:
        return render(request, 'home.html')
