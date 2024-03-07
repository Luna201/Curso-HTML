from flask import Flask

app = Flask(__name__)

@app.route("/") # url: http://localhot:500/
def inicio():
    app.logger.debug("Entramos al path de inicio /")
    return "<p> Hola mundo"

if __name__ == "__main__":
    app.run(debug=True)