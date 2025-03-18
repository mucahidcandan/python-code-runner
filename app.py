from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import subprocess
import tempfile
import os
import sys

app = Flask(__name__)
CORS(app)  # CORS desteği ekle
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True) 