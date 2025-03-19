#app.py

from flask import Flask, render_template, request, redirect, url_for
import csv
from scrapers import scrapers_list
import os  # Importa la librería os

app = Flask(__name__)

# Define la ruta del archivo CSV (asegúrate de que la carpeta "data" exista)
CSV_FILE = os.path.join('data', 'feedback.csv')

# Crea la carpeta "data" si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Inicializa el archivo CSV con los encabezados si no existe
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Consulta', 'Resultado Encontrado', 'Nombre', 'Apellido', 'Nacionalidad', 'Satisfaccion', 'Feedback'])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    print(f"Buscando: {query}")
    results = []
    search_urls = []
    for scraper in scrapers_list:
        print(f"Usando scraper: {scraper.name}")
        search_result = scraper.search(query)
        results.extend(search_result["products"])
        search_urls.append({"name": scraper.name, "url": search_result["search_url"]})
    print(f"Resultados encontrados: {results}")
    return render_template("results.html", results=results, search_urls=search_urls, query=query) # Pasar la consulta a la plantilla

@app.route("/feedback", methods=["POST"])
def feedback():
    query = request.form["query"]
    found_results = request.form["found_results"] #Indica si encontro resultados o no
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    nacionalidad = request.form["nacionalidad"]
    satisfaccion = request.form["satisfaccion"]
    feedback = request.form["feedback"]
    print(f"Feedback recibido: {feedback}")

    # Escribe el feedback en el archivo CSV
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([query, found_results, nombre, apellido, nacionalidad, satisfaccion, feedback])

    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)
