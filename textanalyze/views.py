from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def analyze(request):
    textdata = request.POST.get('text', 'no text')
    removepunc = request.POST.get('removepunc', 'off')
    capup = request.POST.get('capup', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    
    if removepunc == 'on':
        punctuation = '''?!.,_-;:'"}{[]()!@#$%^&*><?/\|'''
        analyzed = ""
        for char in textdata:
            if char not in punctuation:
                analyzed += char
        textdata = analyzed
    
    if capup == 'on':
        analyzed = ""
        for char in textdata:
            analyzed += char.upper()
        textdata = analyzed
    
    if newlineremover == 'on':
        analyzed = ""
        for char in textdata:
            if char != '\n' and char != '\r':
                analyzed += char
        textdata = analyzed
    
    if spaceremover == 'on':
        words = textdata.split()
        analyzed = ' '.join(words)
        textdata = analyzed
    
    if charcounter == 'on':
        analyzed = "Number of character in your text is - " + str(len(textdata))
        params = {'perpose':'Character Counter', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    if(removepunc=='off' and capup=='off' and newlineremover=='off' and spaceremover=='off' and charcounter=='off'):
        return HttpResponse("Pahle Kuchh to pick kar")
    
    params = {'perpose':'Analysation done!', 'analyzed_text':textdata}
    return render(request, 'analyze.html', params)
