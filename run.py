from flask import Flask, render_template, request, redirect, url_for, flash

# =========================================================
# CONFIGURACIÓN DE FLASK
# =========================================================

app = Flask(__name__,
    template_folder="app/template",
    static_folder="app/static"
)

app.secret_key = "clave-secreta-ecosporte"

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")





if __name__ == "__main__":
    app.run(debug=True)