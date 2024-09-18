#esto es para iniciar la aplicación de Flask
from flask import Flask, render_template, jsonify

app = Flask(__name__)

#esto es la lista de trabajos disponibles
JOBS = [
  {
    'id' : 1,   
    'title' : 'Data Analyst',
    'location' : 'Bogota, Colombia',
    'salary' : 'COP $12,000,000',
  },
  {
    'id' : 2,   
    'title' : 'Data Scientist',
    'location' : 'Bogota, Colombia',
    'salary' : 'COP $13,000,000',
  },
  {
    'id' : 3,   
    'title' : 'Data Engineer',
    'location' : 'Bogota, Colombia',
    'salary' : 'COP $12,000,000',
  },
  {
    'id' : 4,   
    'title' : 'Data Analyst',
    'location' : 'Bogota, Colombia',

  }
  
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Chris.Org")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

#esto es para que corra el flask sin dañar las otras configs

if __name__ == "__main__":
  app.run(host= '0.0.0.0', debug=True)
