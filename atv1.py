from flask import Flask

app = Flask(__name__)

@app.route('/decorator')
def texto_explicativo():
    return 'O que é: É uma função que "envolve" outra função para estender seu comportamento sem modificar o código original. É identificado pelo símbolo @.Para que serve: Para reaproveitar lógica e adicionar funções extras (como segurança, logs ou cache) de forma limpa e rápida.No Flask: O @app.route() funciona como um "rastreador". Ele avisa ao Flask que aquela função específica deve ser disparada sempre que um usuário acessar um determinado link (URL).' 

if __name__ == '__main__':
    app.run(debug=True)