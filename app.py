from flask import Flask, render_template
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

if __name__ =="__main__":
	app.run()


