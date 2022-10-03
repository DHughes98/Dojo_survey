from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Secrets"

@app.route('/')
def front_page():
    return render_template('survey.html')

@app.route('/survey', methods=['POST'])
def survey():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/completed')

@app.route('/completed')
def completed():
    return render_template('completed.html')


if __name__ == "__main__":
    app.run(debug=True)