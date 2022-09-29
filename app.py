from flask import Flask

app = Flask(__name__)

@app.route("/")
def reciteMemoryVerse():
    return "Blessed is he whose transgression is forgiven, whose sin is covered.\n"

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)