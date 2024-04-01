from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Diretório onde as imagens enviadas serão salvas
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'imagem' not in request.files:
        return 'Nenhuma imagem enviada', 400

    imagem = request.files['imagem']
    if imagem.filename == '':
        return 'Nenhuma imagem selecionada', 400

    # Salva a imagem no diretório de uploads
    imagem.save(os.path.join(app.config['UPLOAD_FOLDER'], imagem.filename))
    return 'Imagem enviada com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
