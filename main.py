from flask import Flask, render_template, request
import re

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('prvni_stranka.html'), 200


@app.route('/registrace', methods=['GET', 'POST'])
def druha_stranka():
    return render_template('druha_stranka.html', zprava="..."), 200

@app.route('/odeslat', methods=['GET', 'POST'])
def odeslat():
    data1 = request.form['je_plavec']
    data2 = request.form['nick']
    data3 = request.form['kanoe_kamarad']
    if data1 is True:
        if re.search("[a-zA-Z]{2,20}",data2):
            if re.search("[a-zA-Z]{2,20}",data3):
                formular = {
                    "nick": data2,
                    "kamarad": data3
                }
            else:
                formular = {
                    "nick": data2,
                }
        else:
            return "kod:400"
    else:
        return "kod:400"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
