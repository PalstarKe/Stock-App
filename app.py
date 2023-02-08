from flask import Flask
import os
import requests

app = Flask(__name__)

@app.route("/run_colab")
def run_colab():
    # Request to run the Colab notebook
    response = requests.post(
        "https://colab.research.google.com/drive/1M9hoHHARndOijRPKT1TTwMEEvb2Nd_e-?usp=sharing",
        headers={
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        }
    )
    return "Colab notebook run status: {}".format(response.status_code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
