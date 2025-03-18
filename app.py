from flask import Flask, request, jsonify, render_template
import subprocess
import sys
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    try:
        # Geçici bir Python dosyası oluştur
        with open('temp_code.py', 'w', encoding='utf-8') as f:
            f.write(code)
        
        # Kodu çalıştır ve çıktıyı al
        result = subprocess.run([sys.executable, 'temp_code.py'], 
                              capture_output=True, 
                              text=True)
        
        # Geçici dosyayı sil
        os.remove('temp_code.py')
        
        return jsonify({
            'output': result.stdout,
            'error': result.stderr
        })
    except Exception as e:
        return jsonify({
            'output': str(e),
            'error': True
        })

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
    app.run(host='localhost', port=5000, debug=False) 