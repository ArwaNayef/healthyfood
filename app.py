from flask import Flask, render_template, request
app= Flask (__name__)
		
@app.route("/")
def home ():
	return render_template("index.html")

		
@app.route("/healthy food")
def healtyfood ():
	return render_template("healthyfood.html")
		
@app.route("/workout")
def workout ():
	return render_template("workout.html")

@app.route("/contactus")
def contactus ():
	return render_template("contactus.html")

@app.route("/contactus_response",methods= ['POST'])
def contactushere():
	user_message= request.form["messege"]
	user_email= request.form["Email"]

	return render_template("form_data.html", Email=user_email, message= user_message)



if __name__ =="__main__":
	app.run()


