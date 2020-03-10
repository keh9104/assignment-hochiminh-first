from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def result(request):
    text = request.GET["fulltext"]
    textcount = len(text)
    divide = text.split()
    dic = {}
    for ch in divide:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    return render(
        request,
        "result.html",
        {"text": text, "textcount": textcount, "dic": dic, "divide": divide, "ch": ch},
    )

