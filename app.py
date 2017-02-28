from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/PythonApp/login", methods=[POST, GET])
def login():
    if request.method == POST:
        user = request.form('nm')
        return redirect(url_for('sucsess', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('sucsess', name = user))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
