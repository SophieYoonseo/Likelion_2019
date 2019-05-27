from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request,'about.html')

def result_view(request):
    text = request.GET['fulltext']
    splited_text = text.split()

    full = {}

    for word in splited_text:
        if word in full:
            full[word] += 1
        else:
            full[word] = 1 

    context = {
        'text' : text,
        'full' : full.items(),
        'total' : len(splited_text)

    }

    return render(request, 'result.html', context)    