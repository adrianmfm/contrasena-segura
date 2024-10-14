from flask import Flask, request, jsonify
import random
import string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Longitud mínima y máxima
LONGITUD_MINIMA = 8
LONGITUD_MAXIMA = 32

# Ruta para generar la contraseña
@app.route('/generar_contrasena', methods=['POST'])
def generar_contrasena():
    data = request.get_json()  # Obtiene la longitud desde el frontend (JavaScript)
    
    # Verifica que la longitud esté dentro del rango permitido
    longitud = data.get('longitud', LONGITUD_MINIMA)  # Longitud por defecto es mínima si no se especifica
    if longitud < LONGITUD_MINIMA or longitud > LONGITUD_MAXIMA:
        return jsonify({"error": f"La longitud debe estar entre {LONGITUD_MINIMA} y {LONGITUD_MAXIMA} caracteres."}), 400

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

    return jsonify({"contrasena": contrasena})

if __name__ == '__main__':
    app.run(debug=True)
