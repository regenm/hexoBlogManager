from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import subprocess

# 从 backend 模块导入 Flask 实例和 MySQL 连接
from backend import app, mysql

# 启用 CORS，允许前端跨域访问
CORS(app, origins=['http://localhost:5173'])

# 配置上传文件的保存路径
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 确保上传目录存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 文件上传路由
@app.route('/upload', methods=['POST'])
def upload_file():
    # 检查请求中是否包含文件
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    # 检查文件是否有名字
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # 保存文件
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'message': 'File successfully uploaded'}), 200

# 数据获取路由
@app.route('/api/data', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM test_data')
    results = cur.fetchall()
    cur.close()
    return jsonify(results)



@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        
        result = subprocess.run(['python', 'test.py'], capture_output=True, text=True)
        
        return jsonify({
            'output': result.stdout,
            'error': result.stderr,
            'returncode': result.returncode
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 启动应用
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
