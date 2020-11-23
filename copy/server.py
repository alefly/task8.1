from flask import Flask
from flask import request
import io, os, json, logging

logging.basicConfig(filename='./var/log/server.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

app = Flask(__name__)

@app.route('/storage/<file>', methods=['GET', 'PUT', 'DELETE'])
def storage(file):
	if request.method == 'GET':
		if os.path.exists(file):
			return io.open(file).read(), 200
		else:
			return 'file not found', 404
	if request.method == 'DELETE':
		if os.path.exists(file):
			os.remove(file)
		return 'OK', 204
	if request.method == 'PUT':
		try:
			data = json.loads(request.data)
		except:
			return 'data is not json', 400
	f = io.open(file, 'w')
	f.write(request.data.decode('utf-8'))
	return 'OK', 201
	
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)

