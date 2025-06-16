from flask import Flask, render_template, request
   
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def post_test():

	get_string = None

	if request.method == 'POST':

		get_string = request.form.get('string')
		print(f"The string I got back is: {get_string}")

	#Render the HTML template, passing received string if any
	return render_template('post_test.html', string=get_string)

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000, debug = True)
