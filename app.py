#####################################################################
# Name: Rashel Rojas
# Uni: rdr2139
# Flask file for linking other pages of this website.
#####################################################################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("index.html", active='home')

@app.route('/classes/')
def classes():
    return render_template('classes.html', active='classes')

@app.route('/fun/')
def fun():
    return render_template('fun.html', active="fun")

#start the server
if __name__ == "__main__":
    app.run()