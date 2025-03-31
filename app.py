from flask import Flask, render_template

app = Flask(__name__)

# Rota pentru pagina de start
@app.route("/")
def home():
    return render_template("index.html")

# Rota pentru listarea studenților
@app.route("/studenti")
def studenti():
    # Date statice de exemplu
    lista_studenti = [
        {"nume": "Ion Popescu", "matricol": "ST001"},
        {"nume": "Ana Ionescu", "matricol": "ST002"},
        {"nume": "Maria Georgescu", "matricol": "ST003"}
    ]
    return render_template("studenti.html", studenti=lista_studenti)

if __name__ == '__main__':
    app.run(debug=True)