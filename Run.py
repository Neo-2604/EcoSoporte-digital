#!/usr/bin/env python3
import os
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

@app.route("/contactanos", methods=["GET", "POST"])
def contactanos():
    if request.method == "POST":
        flash("Mensaje enviado correctamente. Nos pondremos en contacto pronto.", "success")
        return redirect(url_for("contacto"))
    return redirect(url_for("contacto"))

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Redirección de demostración al dashboard del cliente
        return redirect(url_for("cliente_dashboard"))
    return render_template("login.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        flash("Solicitud de registro enviada correctamente.", "success")
        return redirect(url_for("login"))
    return render_template("registro.html")

@app.route("/logout")
def logout():
    flash("Has cerrado sesión.", "info")
    return redirect(url_for("inicio"))

@app.route("/cliente/dashboard")
def cliente_dashboard():
    return render_template("dashboard_cliente.html", empresa="Empresa Demo", razon_social="Demo S.A.S.", nit="900123456-7")

@app.route("/tecnico/dashboard")
def tecnico_dashboard():
    sample_tickets = [
        {"id": 101, "empresa": "TechCorp", "asunto": "Falla de red", "prioridad": "Alta", "estado": "En proceso"}
    ]
    return render_template("dashboard_tecnico.html", nombre_tecnico="Juan Pérez", tickets=sample_tickets)

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("dashboard_admin.html")

@app.route("/tickets")
@app.route("/tickets/lista")
def tickets():
    sample_tickets = [
        {"id": 101, "asunto": "Falla de red", "descripcion": "Problemas de conectividad en la oficina central.", "categoria": "Redes", "prioridad": "Alta", "estado": "En proceso", "fecha": "2026-09-29"}
    ]
    return render_template("tickets/lista.html", tickets=sample_tickets)

@app.route("/tickets/crear", methods=["GET", "POST"])
def tickets_crear():
    if request.method == "POST":
        flash("Ticket creado con éxito.", "success")
        return redirect(url_for("tickets"))
    return render_template("tickets/crear.html")

@app.route("/tickets/detalle/<int:ticket_id>")
def tickets_detalle(ticket_id):
    ticket_data = {
        "id": ticket_id,
        "asunto": "Falla de red",
        "empresa": "Demo S.A.S.",
        "categoria": "Redes",
        "prioridad": "Alta",
        "nivel_soporte": 2,
        "estado": "En proceso",
        "tecnico": "Carlos Rodríguez",
        "descripcion": "Problemas de conectividad en la oficina principal."
    }
    seguimientos = [
        {"usuario": "Soporte", "fecha": "2026-09-29 10:00", "mensaje": "Ticket asignado a técnico Nivel 2."}
    ]
    return render_template("tickets/detalle.html", ticket=ticket_data, seguimientos=seguimientos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
