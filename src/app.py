from flask import Flask, render_template, request
import graph 

app = Flask(__name__)
palavras = graph.Graph()
palavras.load_graph("./src/data.csv")
correct_word = palavras.random_vertex()

@app.route('/', methods=['GET', 'POST'])
def index():
    

    if request.method == 'POST':
        word = request.form['word']
        if word == correct_word:
            return render_template('index.html', message='Correct!')
        else:
            distance = palavras.bfs_distance(correct_word, word)
            return render_template('index.html', message=f'Errou! Seu palpite está a {distance} da palavra correta. CORRETA {correct_word}')
    


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)