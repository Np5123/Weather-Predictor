from flask import Flask,request,render_template
import pickle
import weather

app=Flask(__name__)

@app.route("/")
def form():
    return(render_template("index.html"))

@app.route("/predict",methods=["POST"])
def predict():
    if(request.method == "POST"):
        city = request.form["name"]
        app1 = weather.weather_pred(str(city))
        data = app1.data()
        return render_template("result.html", data=data)
        
if __name__ == "__main__":
    app.run(debug=True)
