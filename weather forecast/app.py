from flask import Flask, render_template, request
from flask_cors import CORS
from controller import EZWController
""""set DARK_SKY_KEY=15b1fb57be2b7184d28f5c2edb854c23 
    python ezw_app.py"""
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
   return render_template('index.html')

@app.route('/ezw', methods=['POST', 'GET'])
def ezw():
    if request.method == 'POST': 
       data = request.json
       input_location = data['location']

       ezw = EZWController()

       geo_location = ezw.getLocation(input_location)
       if geo_location == None:
           ezw_address = "Unknown location"
           report_template = render_template('reports.html', weather_address=ezw_address)
           return report_template 
       
       ezw_address = geo_location.address       
       ezw_reports = ezw.getWeatherReports(data, geo_location)

       report_template = render_template('reports.html', weather_address=ezw_address, weather_reports=ezw_reports)

    return report_template  

if __name__ == '__main__':
    app.run(debug=False,host='127.0.0.1')   
