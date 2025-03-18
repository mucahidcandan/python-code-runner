from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import tempfile
import os
import sys

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/api/run_code', methods=['POST'])
def run_code():
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
        
        if result.stderr:
            # Hata varsa
            return jsonify({
                'output': result.stderr,
                'error': True
            })
        else:
            # Başarılı çalıştıysa
            return jsonify({
                'output': result.stdout or 'Program çalıştı ama çıktı üretmedi.',
                'error': False
            })
    
    except subprocess.TimeoutExpired:
        return jsonify({
            'output': 'Kod çalıştırma zaman aşımına uğradı (5 saniye limit).',
            'error': True
        })
    except Exception as e:
        return jsonify({
            'output': f'Hata oluştu: {str(e)}',
            'error': True
        })
    finally:
        # Geçici dosyayı temizle
        try:
            if 'temp_file' in locals():
                os.unlink(temp_file)
        except:
            pass

@app.route('/api/install_package', methods=['POST'])
def install_package():
    package = request.json.get('package', '')
    
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', package],
                              capture_output=True,
                              text=True,
                              timeout=30)
        
        if result.stderr:
            return jsonify({
                'output': result.stderr,
                'error': True
            })
        else:
            return jsonify({
                'output': result.stdout or f'{package} paketi başarıyla yüklendi.',
                'error': False
            })
    except subprocess.TimeoutExpired:
        return jsonify({
            'output': 'Paket yükleme zaman aşımına uğradı.',
            'error': True
        })
    except Exception as e:
        return jsonify({
            'output': f'Hata oluştu: {str(e)}',
            'error': True
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 