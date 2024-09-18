#esto es para iniciar la aplicación de Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html')

#esto es para que corra el flask sin dañar las otras configs

if __name__ == "__main__":
  app.run(host= '0.0.0.0', debug=True)
