import sqlite3

def get_films_by_string(str):
	conn = sqlite3.connect('data/films.db')

	sql = '''		
		SELECT * FROM films f WHERE f.Title LIKE ?
								OR f.TitleVN LIKE ?
								OR f.Release LIKE ?
								OR f.Certificate LIKE ?
								OR f.Genre LIKE ?
								OR f.Directors LIKE ?
	'''

	data = conn.execute(sql, (str, str, str, str, str, str,)).fetchall()
	conn.close()

	return data
if __name__ == '__main__':
	print(get_films_by_string('%'+'drama'+'%'))