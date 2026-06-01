try:
    import pyshorteners
except ImportError:
    print("Erro: pyshorteners não está instalado")
    print("Instale usando: pip install pyshorteners")
    exit()

url_longa = input("Digite a URL longa que deseja encurtar: ")

try:
    type_tiny = pyshorteners.Shortener()
    url_curta = type_tiny.tinyurl.short(url_longa)
    print(f"URL Curta: {url_curta}")
except Exception as e:
    print(f"Erro ao encurtar a URL. Verifique se o link está correto. Detalhes: {e}")
