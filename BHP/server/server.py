from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('access-control-allow-origin', '*')
    return response

@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    balacony = int(request.form['balacony'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, balacony, bath)
    })

    response.headers.add('access-control-allow-origin', '*')

    return response

if __name__ == "__main__":
    print("Starting python Flask server for bangluru house price prediction")
    util.load_saved_artifacts()
    app.run()