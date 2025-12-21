from flask import Flask, render_template, request
from real_walmart.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

# Initialize prediction pipeline
prediction_pipeline = PredictionPipeline()


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        try:
            input_data = {
                "Store": int(request.form["Store"]),
                "Holiday_Flag": int(request.form["Holiday_Flag"]),
                "Temperature": float(request.form["Temperature"]),
                "Fuel_Price": float(request.form["Fuel_Price"]),
                "CPI": float(request.form["CPI"]),
                "Unemployment": float(request.form["Unemployment"]),
            }

            prediction = prediction_pipeline.predict(input_data)

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
