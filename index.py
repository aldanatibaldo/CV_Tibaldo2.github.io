from flask import Flask, render_template

app = Flask(__name__)


#-------------------------
# @app.route('/')
# def principal():
#     return "Bienvenido a mi sitio web"

# @app.route('/contacto')
# def contacto():
#     return "Esta es la página de contacto"
#-------------------------

@app.route('/doctorado')
def principal():
    return render_template('doctorado.html')

@app.route('/docencia')
def docencia():
    return render_template('docencia.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv("PORT", 5017)))
    
