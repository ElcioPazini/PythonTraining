from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def myFirstEndpoint():
    return "My first python endpointtttt!!!!!!"

if __name__ == "__main__":
    app.run()