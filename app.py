from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import subprocess
import sys
import os
import socket
import time
import psutil
import tempfile

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:*", "http://127.0.0.1:*"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "Access-Control-Allow-Origin"],
        "supports_credentials": True,
        "expose_headers": ["Content-Type", "Authorization"],
        "max_age": 600
    }
})
app.config['SECRET_KEY'] = os.urandom(24)

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

def kill_process_on_port(port):
    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        try:
            for conn in proc.connections():
                if conn.laddr.port == port:
                    proc.kill()
                    time.sleep(1)
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

@app.route('/api/run_code', methods=['POST', 'OPTIONS'])
def run_code():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
        
    code = request.json.get('code', '')
    
    # Güvenlik kontrolleri
    if any(keyword in code.lower() for keyword in ['import os', 'import sys', 'import subprocess', 'eval(', 'exec(']):
        return jsonify({
            'output': 'Güvenlik nedeniyle bu komutlara izin verilmiyor.',
            'error': True
        })
    
    # Geçici dosya oluştur
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code)
            temp_file = f.name
        
        # Python yorumlayıcısının tam yolunu al
        python_path = sys.executable
        
        # Kodu çalıştır
        result = subprocess.run([python_path, temp_file], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        
        response = jsonify({
            'output': result.stderr if result.stderr else (result.stdout or 'Program çalıştı ama çıktı üretmedi.'),
            'error': bool(result.stderr)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    except subprocess.TimeoutExpired:
        response = jsonify({
            'output': 'Kod çalıştırma zaman aşımına uğradı (5 saniye limit).',
            'error': True
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({
            'output': f'Hata oluştu: {str(e)}',
            'error': True
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    finally:
        # Geçici dosyayı temizle
        try:
            if 'temp_file' in locals():
                os.unlink(temp_file)
        except:
            pass

@app.route('/api/install_package', methods=['POST', 'OPTIONS'])
def install_package():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
        
    package = request.json.get('package', '')
    
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', package],
                              capture_output=True,
                              text=True,
                              timeout=30)
        
        response = jsonify({
            'output': result.stderr if result.stderr else (result.stdout or f'{package} paketi başarıyla yüklendi.'),
            'error': bool(result.stderr)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except subprocess.TimeoutExpired:
        response = jsonify({
            'output': 'Paket yükleme zaman aşımına uğradı.',
            'error': True
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({
            'output': f'Hata oluştu: {str(e)}',
            'error': True
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

if __name__ == '__main__':
    # Port kontrolü ve temizleme
    port = find_available_port()
    if port is None:
        print("Kullanılabilir port bulunamadı!")
        sys.exit(1)
    
    print(f"Uygulama http://localhost:{port} adresinde başlatılıyor...")
    app.run(host='0.0.0.0', port=port, debug=False) 