# importing modules from flask library
from flask import render_template
# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
# define the route to father webpage
@app.route("/father")

# define the route to mother webpage
@app.route("/friend")

# define the route to friends webpage
@app.route("/mother")
def home():

    name = "Levin" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want
if __name__  ==  '__main__':
    app.run(debug=True)