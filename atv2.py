from flask import Flask

app = Flask(__name__)

@app.route('/curriculo')
def texto_explicativo():
    return '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - Desenvolvedor & Estudante</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        header {
            border-bottom: 2px solid #3498db;
            padding-bottom: 20px;
            margin-bottom: 20px;
        }
        h1 {
            margin: 0;
            color: #2c3e50;
            text-transform: uppercase;
        }
        .info {
            color: #7f8c8d;
            font-size: 0.9em;
        }
        h2 {
            color: #3498db;
            font-size: 1.2em;
            border-left: 4px solid #3498db;
            padding-left: 10px;
            margin-top: 30px;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        .tag {
            background: #ecf0f1;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 0.9em;
            display: inline-block;
            margin: 2px;
        }
        .highlight {
            font-weight: bold;
            color: #2c3e50;
        }
        ul {
            padding-left: 20px;
        }
        </style>
    </head>
    <body>

    <div class="container">
        <header>
        <h1>Tiago Vinícius Santos Silva</h1>
        <div class="info">
            Estudante COTEMIG Floresta | 17 Anos | Belo Horizonte, MG | (31) 99751-3424 | tiagoviniciusestagio@gmail.com<br>
            <strong>Inglês: Fluente (C2)</strong> | <a href="#">LinkedIn</a> | <a href="#">GitHub</a>
        </div>
    </header>

    <h2>Objetivo</h2>
    <p>Estudante de tecnologia buscando oportunidade de estágio ou nível junior para aplicar conhecimentos em desenvolvimento de software, infraestrutura e robótica.</p>

    <h2>Habilidades Técnicas</h2>
    <div class="grid">
        <div>
            <p class="highlight">Desenvolvimento:</p>
            <span class="tag">Python</span>
            <span class="tag">Java</span>
            <span class="tag">PHP</span>
            <span class="tag">HTML5</span>
            <span class="tag">CSS3</span>
        </div>
        <div>
            <p class="highlight">Hardware & Infra:</p>
            <span class="tag">Redes de Computadores</span>
            <span class="tag">Arquitetura de PCs</span>
            <span class="tag">Robótica</span>
        </div>
    </div>

    <h2>Educação</h2>
    <p>
        <span class="highlight">Bacharelado em Ciência da Computação / Engenharia (ou similar)</span><br>
        Nome da Instituição | <i>Previsão de conclusão: 202X</i>
    </p>

    <h2>Conhecimentos Complementares</h2>
    <ul>
        <li><strong>Redes:</strong> Configuração de roteadores, protocolos TCP/IP e segurança básica.</li>
        <li><strong>Hardware:</strong> Montagem, manutenção e análise de arquitetura de sistemas.</li>
        <li><strong>Robótica:</strong> Desenvolvimento de projetos integrando hardware e software.</li>
        <li><strong>Web:</strong> Criação de interfaces responsivas e integração com back-end em PHP/Python.</li>
    </ul>

    <h2>Idiomas</h2>
        <p><strong>Inglês:</strong> Fluente (Leitura, Escrita e Conversação).</p>
    </div>

    </body>
    </html>
'''

if __name__ == '__main__':
    app.run(debug=True)