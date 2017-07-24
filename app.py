from flask import Flask, render_template
app= Flask (__name__)
import dataset

db=dataset.connectus( "postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4") 
table=db["user"]
table.insert(dict(Email="halabarka11@gmail.com",message ="hi" )) 
table.insert(dict(Email="hlabarka00@gmail.com",message ="hello" ))  

for user in table:
	print ("id :"+ str(user["id"])+"Email:"+user["Email"]+"message:"+str(user["message"]))
	
@app.route("/")
def home ():
	return render_template("index.html")

		
@app.route("/healthyfood")
def healtyfood ():
	return render_template("healthyfood.html")
		
@app.route("/workout")
def workout ():
	return render_template("workout.html")

if __name__ =="__main__":
	app.run()


