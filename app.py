import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    # Carica la pagina iniziale
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # 1. Recupera i dati inseriti dall'utente nel browser
    lunghezza = float(request.form["lungh"])
    peso = float(request.form["peso"])

    # 2. Logica aziendale standard (Invece dell'AI)
    # Esempio: Se il peso è > 30kg O la lunghezza è > 800mm, serve l'isola grande
    if peso > 30 or lunghezza > 800:
        risultato = "Isola Robotizzata HEAVY (Portata Elevata)"
        descrizione = "Consigliata per carichi pesanti o ingombranti."
    else:
        risultato = "Isola Robotizzata COMPACT (Alta Velocità)"
        descrizione = "Ideale per pezzi leggeri e cicli rapidi."

    # 3. Rispedisce il risultato alla pagina HTML
    return render_template("index.html", previsione=risultato, dettaglio=descrizione)


if __name__ == "__main__":
    # Render assegna una porta dinamicamente, quindi dobbiamo leggerla dalle variabili d'ambiente
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
