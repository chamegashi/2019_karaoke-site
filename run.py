from flask import Flask, render_template, jsonify, request
from random import *
from backend.database import add_music_data, get_music_data, get_music_data_by_id, change_music_data, delete_music_data

app = Flask(__name__,
			static_folder = "./dist/static",
			template_folder = "./dist")

@app.route('/model/add', methods=['POST'])
def save_music():
	if request.method == 'POST':
		music_name = request.form['music_name']
		music_name_hiragana = request.form['music_name_hiragana']
		artist = request.form['artist']
		key = request.form['key']
		res = add_music_data(music_name, music_name_hiragana, artist, key)
		return jsonify({"responce" : res})
	else:
		return jsonify({"test": "get やん..."})


@app.route('/model/search_id', methods=['POST'])
def search_music_by_id():
	if request.method == 'POST':
		id_num = request.form['id']
		result = get_music_data_by_id(id_num)
		return jsonify({"result":result})
	else:
		return jsonify({"test": "get やん..."})


@app.route('/model/search', methods=['POST'])
def search_music():
	if request.method == 'POST':
		print("done")
		text = request.form['text']
		search_key = request.form['search_key']
		search_way = request.form['search_way']
		result = get_music_data(text, search_key, search_way)
		return jsonify({"result":result})


@app.route('/model/change', methods=['POST'])
def change_music():
	if request.method == 'POST':
		id = request.form['id']
		music_name = request.form['music_name']
		music_name_hiragana = request.form['music_name_hiragana']
		artist = request.form['artist']
		key = request.form['key']
		change_music_data(id, music_name, music_name_hiragana, artist, key)
		return jsonify({"responce" : "OK"})
	else:
		return jsonify({"test": "get やん..."})


@app.route('/model/delete', methods=['POST'])
def delete_music():
	if request.method == 'POST':
		id = request.form['id']
		delete_music_data(id)
		return jsonify({"responce" : "OK"})

@app.route('/model/getArtists', methods=['GET'])
def get_artists():
	if request.methods == 'GET':
		result = get_artist_data()
		return jsonify({"result":result})

@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
def catch_all(path):
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)