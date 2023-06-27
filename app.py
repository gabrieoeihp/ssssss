from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome'].lower()
        if nome == 'gabriel':
            mensagem = 'Que nome lindo!'
        else:
            mensagem = 'Que nome paia.'
        if nome == 'lucas':
            mensagem = 'que nome de viado'
        return render_template('index.html', mensagem=mensagem)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
