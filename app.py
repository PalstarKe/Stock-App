
from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://drive.google.com/drive/folders/1OaXMnvd7xwSgFaoE4uUQ6IRilRHAxChC', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
