from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Run the top command to get system processes
    result = subprocess.run(['top', '-b', '-n', '1'], stdout=subprocess.PIPE, text=True)
    return f"<pre>{result.stdout}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
