from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import subprocess
import sys
import os
import socket
import time
import psutil

app = Flask(__name__)
CORS(app)  # CORS desteği ekle

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

def kill_process_on_port(port):
    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        try:
            for conn in proc.connections():
                if conn.laddr.port == port:
                    proc.kill()
                    time.sleep(1)  # İşlemin tamamen kapanması için bekle
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False

def find_available_port(start_port=5000, max_port=5010):
    for port in range(start_port, max_port + 1):
        if not is_port_in_use(port):
            return port
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    
    # Geçici Python dosyası oluştur
    with open('temp_code.py', 'w', encoding='utf-8') as f:
        f.write(code)
    
    try:
        # Python kodunu çalıştır
        result = subprocess.run([sys.executable, 'temp_code.py'], 
                              capture_output=True, 
                              text=True, 
                              timeout=10)
        
        # Çıktıyı al
        output = result.stdout
        error = result.stderr
        
        return jsonify({
            'output': output,
            'error': error
        })
    except subprocess.TimeoutExpired:
        return jsonify({
            'output': '',
            'error': 'Kod çalıştırma zaman aşımına uğradı (10 saniye)'
        })
    finally:
        # Geçici dosyayı sil
        if os.path.exists('temp_code.py'):
            os.remove('temp_code.py')

@app.route('/install_package', methods=['POST'])
def install_package():
    try:
        package = request.json.get('package', '')
        if not package:
            return jsonify({'output': 'Lütfen bir paket adı girin.'})

        # pip install komutunu çalıştır
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', package],
                              capture_output=True,
                              text=True)
        
        if result.returncode == 0:
            return jsonify({
                'output': f'Paket başarıyla yüklendi: {package}\n{result.stdout}'
            })
        else:
            return jsonify({
                'output': f'Hata: {result.stderr}'
            })
    except Exception as e:
        return jsonify({
            'output': f'Hata: {str(e)}'
        })

if __name__ == '__main__':
    # Port kontrolü ve temizleme
    port = find_available_port()
    if port is None:
        print("Kullanılabilir port bulunamadı!")
        sys.exit(1)
    
    print(f"Uygulama http://localhost:{port} adresinde başlatılıyor...")
    app.run(host='0.0.0.0', port=port, debug=False) 