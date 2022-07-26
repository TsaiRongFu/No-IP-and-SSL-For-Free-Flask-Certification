from flask import Flask, redirect, send_file

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi Bad Guy."

@app.route("/.well-known/pki-validation/<path:filename>",methods=['GET', 'POST'])
def txt(filename):
    path ='./'+ filename
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
