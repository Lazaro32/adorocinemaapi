# PARTE1
import os
from urllib.request import urlopen

from bs4 import BeautifulSoup
from flask import Flask, jsonify

# PARTE2
app = Flask(__name__)
html_doc = urlopen("http://www.adorocinema.com/filmes/numero-cinemas/").read()
soup = BeautifulSoup(html_doc, "html.parser")
data = []
for dataBox in soup.select("div.card.entity-card.entity-card-list.cf"):
    nomeObj = dataBox.find("h2", "meta-title").find("a", "meta-title-link")
    imgObj = dataBox.find("figure").find("img")
    sinopseObj = dataBox.find("div", "synopsis").find("div")
    dataObj = dataBox.find("span", "date")
    if 'data:image' in imgObj['src']:
        data.append({'nome': nomeObj.text.strip(),
                     'poster': imgObj['data-src'].strip(),
                     'sinopse': sinopseObj.text.strip(),
                     'data': dataObj.text.strip()})
    else:
        data.append({'nome': nomeObj.text.strip(),
                     'poster': imgObj['src'].strip(),
                     'sinopse': sinopseObj.text.strip(),
                     'data': dataObj.text.strip()})


# PARTE3
@app.route('/', methods=['GET'])
def filmes():
    return jsonify({'filmes': data})
    # return"Tudo pronto!"


# PARTE4
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
