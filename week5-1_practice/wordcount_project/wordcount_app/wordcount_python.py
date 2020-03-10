def textcount(text):
    textcount = len(text)
    divide = text.split()
    dividecount = len(divide)
    dic = {}
    for ch in divide:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    return (
        request,
        "result.html",
        {"text": text, "textcount": textcount, "dic": dic, "divide": divide, "ch": ch,},
    )

