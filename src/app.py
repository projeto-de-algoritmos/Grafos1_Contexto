#coding = utf-8
from flask import Flask, render_template, request
import graph 
from unicodedata import normalize

app = Flask(__name__)
palavras = graph.Graph()
palavras.load_graph("./src/data.json")
correct_word = palavras.random_vertex()
print(correct_word)

@app.route('/', methods=['GET', 'POST'])

def index():
    
    #COMO JOGAR
    if request.method == 'GET':
        return render_template('index.html')
    

    if request.method == 'POST':
        word = request.form['word']
        word = (normalize('NFKD', word).encode('ASCII','ignore').decode('ASCII')).lower()

        if word == correct_word:
            return render_template('index.html', result_correct='Acertou!!', message='A palavra correta era: ' + correct_word + '.')
        else:
            distance = palavras.bfs_distance(correct_word, word)
            if distance == -1:
                return render_template('index.html', result_error='Palavra não encontrada :(', message='A palavra digitada ainda não está presente em nosso sistema.')
            return render_template('index.html', result_error='Errou!', message=f'Seu palpite está a {distance} contextos da palavra correta.')
    


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)