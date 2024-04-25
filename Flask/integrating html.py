from flask import Flask, redirect, url_for, render_template,request
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')




 


@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = 'PASS'
    
    else:
        res = 'FAIL'
    
    return render_template('result.html', result = res)



@app.route('/fail/<int:score>')
def fail(score):
    return 'The Person has faild and the marks is ' + str(score)




@app.route('/results/<int:marks>')
def result(marks):
    result = ''
    if marks < 50:
        result = 'fail'

    else :
        result = 'success'
    
    return redirect(url_for(result, score = marks))




@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':

        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + c + datascience) / 4

    res = ''

    if total_score >= 50:
        res = 'success'

    else:
        res = 'fail'

    return redirect(url_for(res, score = total_score))




if __name__ == '__main__':
    app.run(debug=True)
