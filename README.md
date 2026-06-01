# 🔗 Encurtador de URL em Python

Projeto simples desenvolvido em Python para encurtar URLs utilizando a biblioteca `pyshorteners` e o serviço TinyURL.

---

## 🚀 Funcionalidades

* Encurta links rapidamente
* Interface simples via terminal
* Tratamento básico de erros
* Fácil de usar e modificar

---

## 🛠 Tecnologias Utilizadas

* Python 3
* pyshorteners

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/VictorEmanoel-SQl/encurtador-de-url.git
```

Acesse a pasta do projeto:

```bash
cd encurtador-url-python
```

Instale a dependência necessária:

```bash
pip install pyshorteners
```

---

## ▶ Como Executar

Execute o arquivo Python:

```bash
python main.py
```

Digite a URL desejada quando solicitado:

```bash
Digite a URL longa que deseja encurtar:
```

---

## 💻 Exemplo de Uso

```bash
Digite a URL longa que deseja encurtar:
https://www.google.com

URL Curta: https://tinyurl.com/xxxxx
```

---

## 📄 Código

```python
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
```

---

## 🎯 Objetivo do Projeto

Este projeto foi criado para praticar:

* Uso de bibliotecas externas
* Entrada de dados pelo terminal
* Tratamento de exceções
* Consumo simples de APIs e serviços web

---

## 📌 Autor

Desenvolvido por mim, Victor Emanoel 🚀
