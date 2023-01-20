from flask import Flask, render_template, request
from string import digits
app = Flask(__name__)

def f(x):
    b = ''
    if all(i in digits for i in x):
        return sum(int(j) for j in x)
    else: 
        for j in x:
            if j not in digits: b += j
        return b
    

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == "POST": 
        result = f(str(request.form["input"]))
    return render_template('index.html', result=result)
    
if __name__ == "__main__":
    app.run()
