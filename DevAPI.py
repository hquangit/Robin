from flask import Flask, jsonify
import utils

app = Flask(__name__)

@app.route('/films_searched/<str>', methods=['GET'])
def search_films(str):
	new_str = "%"+str+"%"
	rows = utils.get_films_by_string(new_str)
	data = []

	for r in rows:
		data.append({
			'id': r[0],
			'title': r[1],
			'titleVN': r[2],
			'release': r[3],
			'certificate': r[4],
			'runtime': r[5],
			'genre': r[6],
			'rates': r[7],
			'directors': r[8]
			})

	return jsonify ({'films': data})
if __name__ == '__main__':
	app.run()
