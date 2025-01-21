from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
    if extraspaceremover == 'on':
        analyzed = ""
        for index in range(len(djtext) - 1):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += djtext[index]
        analyzed += djtext[-1] 
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    if removepunc != "on" and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on':
        return HttpResponse("Error: No options were selected.")

    return render(request, 'analyze.html', params)



