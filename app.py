# import necessary libraries
from flask import Flask, request, render_template, redirect, url_for
import wikipedia
from wikipedia.wikipedia import summary

app = Flask(__name__)

#home view
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        try:
            wiki = request.form['Wikipedia']

            #summarize the data from wikipedia
            data = wikipedia.summary(wiki, sentences=2)
            return f'{data}'
        except Exception as e:
            return f'<p>{e} </p>'
    else:
        return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)
