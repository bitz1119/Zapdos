
@app.route('/route_map',methods=['GET','POST'])
def route_map():
	return render_template('route.html')


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
    #print(rt['routes'][0]['steps'][0]['maneuver']['location']['coordinates'])
    routes = rt['routes']
    rna = []
    for i in routes:
    	rd = i['distance']
    	rn = 0
    	for j in i['steps']:
    		latlong = j['maneuver']['location']['coordinates']
    		lat = latlong[1]
    		lon = latlong[0]
    		consi = []
    		ps = []
    		for k in range(len(x)):
    			d = x[k] - lon
    			d1 = y[k] - lat
    			diff = (d**(2) + d1**(2))**(.5)
    			if (diff < 0.2):
    				consi.append(k)
    				ps.append(diff)
    		sp = 0
    		for k in range(len(consi)):
    			if ndis[consi[k]] != 0:
    				sp += ps[k]/ndis[consi[k]]
    		if len(consi) != 0:
    			rn += (sp/len(consi))
    	rn = rn/((rd+0.1)/1000)
    	if rn != 0:
    		rna.append(rn*hour_safe*1000)
    	else:
    		rna.append(5)
    return rna
