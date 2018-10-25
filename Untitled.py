
from flask import Flask, render_template, request , session , Response
import flask , os
import pandas as pd
import json
from flask_cors import CORS, cross_origin
# from info import cluster_info
# from utility import maker
# import datetime
import requests
import random


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_ALLOW_HEADERS'] = ( 'accept','accept-encoding','authorization','content-type','dnt','origin','user-agent','x-csrftoken','x-requested-with')
app.config["CORS_SUPPORTS_CREDENTIALS"] = True

@app.route('/',methods=['GET','POST'])
def index():
   return render_template('index2.html')


@app.route('/route_map',methods=['GET','POST'])
def route_map():
   return render_template('route.html')


@app.route('/data',methods=['GET','POST'])
def data():
   return render_template('data.html')



@app.route('/route',methods=['GET','POST'])
def route():
   msg = request.get_json()
   loc = json.loads(request.data)
   rna = safest_route(loc)
   analysis = {'Routes':rna}
   print(analysis)
   analysis = flask.jsonify(analysis)
   return analysis



def safest_route(rt):
    p = pd.read_csv("./mapbox/dataset.csv")
    x1 = []
    for i in p:
        if i[3]=='PotHole':
            x1[0].append([p.Latitude,p.Longitude])
        if i[3] == 'Accident':
            x1[1].append([p.Latitude,p.Longitude])
        if i[3] == 'Light':
            x1[2].append([p.Latitude,p.Longitude])

    routes = rt['routes']
    rna = []
    for i in routes:
        rd = i['distance']
        rn = 0
        for j in i['steps']:
            latlong = j['maneuver']['location']['coordinates']
            lat = latlong[1]
            lon = latlong[0]
            absol = []
            for t in range(len(x1)):
                x = x1[t][0]
                y = x1[t][1]
                ps = []
                for k in range(len(x)):
                    d = x[k] - lon
                    d1 = y[k] - lat
                    diff = (d**(2) + d1**(2))**(.5)
                    if (diff < 0.5):
                        ps.append(diff)
                absol.append(sum(ps))
            rn += 2/(sum(absol) + 1)
        rn = rn/((rd+0.1)/1000)
        if rn != 0:
            rna.append(rn*1000)
        else:
            rna.append(5)
    return rna

if __name__ == '__main__':
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0' , port = port , debug=True)
