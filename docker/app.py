from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Despliegue DevOps Exitoso</h1><p>Aplicación corriendo en Docker!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
