from flask import*
app=Flask(__name__)
@app.route('/')
def home():
	return render_template('maps.html')
@app.route('/result',methods=['POST'])
def classic():
	result=request.form
	return render_template('result.html',result=result)

if(__name__=='__main__'):
	app.run(debug=True)