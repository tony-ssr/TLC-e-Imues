#!/usr/bin/env python3
"""
Servidor HTTP simple para servir el proyecto web
Uso: python server.py
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Puerto por defecto
PORT = 8000

# Directorio actual
DIRECTORY = Path(__file__).parent

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def end_headers(self):
        # Agregar headers CORS si es necesario
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    # Cambiar al directorio del script
    os.chdir(DIRECTORY)
    
    # Crear el servidor
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print(f"Servidor HTTP iniciado en el puerto {PORT}")
        print(f"Accede a: {url}")
        print("=" * 60)
        print("\nPresiona Ctrl+C para detener el servidor\n")
        
        # Abrir el navegador automáticamente
        try:
            webbrowser.open(url)
        except:
            print("No se pudo abrir el navegador automáticamente")
        
        # Iniciar el servidor
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServidor detenido por el usuario")
            httpd.shutdown()

if __name__ == "__main__":
    main()

