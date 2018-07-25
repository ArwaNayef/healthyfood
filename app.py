from flask import Flask, render_template, request
#import dataset
app= Flask (__name__)


#db= dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4")

#recipes_table= db["food_recipes"]


#{% for user in recipes %}
	#	print (";firstame"+ ";lastname"+";message"+";gender")


#print(db.tables)
#print(table.colums)
		

@app.route("/")
def home ():
	return render_template("index.html")

		
@app.route("/healthyfood")
def healthyfood ():
	return render_template("healthyfood.html")
		
@app.route("/workout")
def workout ():
	return render_template("workout.html")

@app.route("/submitrecipes")
def submitrecipes ():
	return render_template("submitrecipes.html")

@app.route("/yourrecipes")
def yourrecipes ():
	recipes= recipes_table.find()
	return render_template("yourrecipes.html", recipes=list(recipes))


#@app.route("/contactus_response",methods= ['POST'])
#def contactushere():
#	user_recipe= request.form["Recipe"]
#	user_email= request.form["Email"]
#	recipes_table.insert(dict(Email=user_email, Recipe=user_recipe))



#	return render_template("form_data.html", Email=user_email, Recipe= user_recipe)




if __name__ =="__main__":
	app.run()


