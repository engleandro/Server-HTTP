from flask import Flask, jsonify, url_for


def getNumberName(num):
    
    # DATABASE
    db = {
        0: {'1': 'um',     '2': 'dois',  '3': 'três',
            '4': 'quatro', '5': 'cinco', '6': 'seis',
            '7': 'sete',   '8': 'oito',  '9': 'nove', '0':''},
        1: {'2': 'vinte',     '3': "trinta",   '4': "quarenta",
            '5': "cinquenta", '6': "sessenta", '7': "setenta",
            '8': "oitenta",   '9': "noventa",  '0':'', '1':''},
        2: {'1': 'cento',        '2': 'duzentos',   '3': "trezentos",
            '4': "quatrocentos", '5': "quinhentos", '6': "seiscentos",
            '7': "setecentos",   '8': "oitocentos", '9': "novecentos", '0':''},
        3: {'1': 'um',     '2': 'dois',  '3': 'três',
            '4': 'quatro', '5': 'cinco', '6': 'seis',
            '7': 'sete',   '8': 'oito',  '9': 'nove', '0':''},
        4: {'2': 'vinte',     '3': "trinta",   '4': "quarenta",
            '5': "cinquenta", '6': "sessenta", '7': "setenta",
            '8': "oitenta",   '9': "noventa",  '0':'', '1':''},
        "e": {'0': 'dez', '1': 'onze', '2': 'doze', '3': 'treze',
            '4': 'quatorze', '5': "quinze", "6": 'dezesseis',
            '7': 'dezessete','8': 'dezoito', '9': 'dezenove'}
        }
    
    # WRITE NAME
    snum = str(num)
    size = len(snum)
    words = []
    
    for i, n in enumerate(snum[::-1]):
        
        if i is 0:
            
            if size==(i+1):
                words.append(db[i][n])
            elif size>(i+1):
                if snum[::-1][i+1] is not '1':
                    words.append(db[i][n])
                elif snum[::-1][i+1] is '1':
                    continue
            
        elif i is 1:
            
            if n is not '1':
                if snum[::-1][i-1] is not "0": words.append("e")
                words.append(db[i][n])
            elif n is '1':
                words.append(db['e'][snum[::-1][i-1]])
            
        elif i is 2:
            
            if snum[::-1][i-1] is not "0": words.append("e")
            words.append(db[i][n])
            
        elif i is 3:
        
            if size==(i+1):
                words.append("mil")
                words.append(db[i][n])
            elif size>(i+1):
                if snum[::-1][i+1] is not '1':
                    words.append("mil")
                    words.append(db[i][n])
                elif snum[::-1][i+1] is '1':
                    continue
            
        elif i is 4:
            
            if n is not '1':
                if snum[::-1][i-1] is not "0": words.append("e")
                words.append(db[i][n])
            elif n is '1':
                words.append("mil")
                words.append(db['e'][snum[::-1][i-1]])
            
        elif i is 5:
            
            if snum[::-1][i-1] is not "0": words.append("e")
            words.append(db[i][n])
    
    sname = ""
    words.reverse()
    for word in words:
        sname += word+" "
    sname = sname[:-1]
    
    return sname


def server():
    
    # DATABASE
    db = {
        0: {'1': 'um',     '2': 'dois',  '3': 'três',
            '4': 'quatro', '5': 'cinco', '6': 'seis',
            '7': 'sete',   '8': 'oito',  '9': 'nove'},
        1: {"0":"", "1":"", '2': 'vinte',    '3': "trinta",
            '4': "quarenta", '5': "cinquenta", '6': "sessenta",
            '7': "setenta",  '8': "oitenta",   '9': "noventa"},
        2: {'1': 'cento',        '2': 'duzentos',   '3': "trezentos",
            '4': "quatrocentos", '5': "quinhentos", '6': "seiscentos",
            '7': "setecentos",   '8': "oitocentos", '9': "novecentos"},
        "e": {'0': 'dez', '1': 'onze', '2': 'doze', '3': 'treze',
            '4': 'quatorze', '5': "quinze", "6": 'dezesseis',
            '7': 'dezessete','8': 'dezoito', '9': 'dezenove'}
        }
    
    app = Flask(__name__)
    
    @app.route('/hello', methods=['GET'])
    def sayHello():
        return jsonify({"msg": "hello world"})
    
    @app.route('/<int:num>', methods=['GET'])
    def positive_convert(num):
        if not (num < 100000):
            return jsonify({"mgs": "INVALID URL"})
        sname = getNumberName(num)
        if num is 0:
            return jsonify({"extenso": "zero"})
        else:
            return jsonify({"extenso": sname})
    
    @app.route('/-<int:num>', methods=['GET'])
    def negative_convert(num):
        if not (num < 100000):
            return jsonify({"mgs": "INVALID URL"})
        sname = getNumberName(num)
        if num is 0:
            return jsonify({"extenso": "zero"})
        else:
            return jsonify({"extenso": "menos "+sname})
    
    return app



if __name__ == '__main__':
    app = server()
    app.run(host="localhost", port=3000, debug=True)

