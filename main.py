from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')
nicknames = set()
zprava=[]
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Endpont, ktery vygeneruje privni_stranka.html, a posila atribut zprava
    """
    return render_template('prvni_stranka.html', zprava=zprava), 200

@app.route('/api/check-nickname', methods=['GET'])
def check_nickname():
    """
    kontroluje jestli je v query atribut nick a vraci jestli nick uz neni ulozen
    """
    nick = request.args.get('nick')
    print(nick)
    print(nicknames)
    if nick in nicknames:
        return jsonify({"exists": True})
    else:
        return jsonify({"exists": False})


@app.route('/registrace', methods=['GET', 'POST'])
def druha_stranka():
    """
    GET
        renderuje druha_stranka.html
    POT
        jestli jsou validni data, tak renderuje prvni nebo druhou stranku
    """
    if request.method == 'GET':
        return render_template('druha_stranka.html', zprava=zprava), 200
    if request.method == 'POST':
        data1 = request.form.get('je_plavec')
        data2 = request.form.get('nick')
        data3 = request.form.get('kanoe_kamarad')
        if data1 == "True":
            if re.search("[a-zA-Z0-9]{2,20}",data2):
                if re.search("[a-zA-Z0-9]{2,20}",data3):
                    zprava.append([data2, data3])
                    nicknames.add(data2)
                    return render_template('prvni_stranka.html', zprava=zprava), 200
                else:
                    zprava.append(data2)
                    nicknames.add(data2)
                    return render_template('prvni_stranka.html', zprava=zprava), 200
            else:
                return render_template('druha_stranka.html'), 400
        else:
            return render_template('druha_stranka.html'), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
