import pyshorteners

url_longa = input("Digite a URL longa que deseja encurtar: ")

type_tiny = pyshorteners.Shortener()

url_curta = type_tiny.tinyurl.short(url_longa)

print(f"URL Curta: {url_curta}")