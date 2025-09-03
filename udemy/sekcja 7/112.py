# string replace

def cleanText(text):
    text = text.replace("javascript", "********")
    text = text.replace("java", "*" * 4)
    text = text.replace("php", "*" * 3)
    text = text.replace("html", "*" * 4)
    text = text.replace("css", "*" * 3)
    return text

content = """Programowanie zacząłem z językiem php, następnie korzystałem z
html i css, a na koniec poznałem python, java i javascript """

newContent = cleanText(content)
print(newContent)
