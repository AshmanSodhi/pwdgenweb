from flask import Flask , render_template , request
from core import low
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')
    #return 'Hello World Ashman! Jai Maha'

@app.route('/genpassword' , methods=['GET','POST'])
def genpassword():
    length = int(request.form.get('passlen'))
    type = int(request.form.get('flexRadioDefault'))
    return render_template('home.html' , generated_pws = low(length , type))
    #return low(length , type)



if __name__ == "__main__":
    app.run(debug=True)
