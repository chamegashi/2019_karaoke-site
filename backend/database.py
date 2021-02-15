import os, random
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///music.db")
Base = declarative_base()

class Music(Base):
	__tablename__ = 'musics'
	id = Column(Integer, primary_key=True, unique=True)
	music_name = Column(String)
	music_name_hiragana = Column(String)
	artist = Column(String)
	key = Column(Integer)
	state_1 = Column(Integer)
	state_2 = Column(Integer)
	state_3 = Column(Integer)

	def __repr__(self):
		return "Music<{}, {}, {}, {}, {}, {}, {}, {}>".format(
			self.id,
			self.music_name,
			self.music_name_hiragana,
			self.artist,
			self.key,
			self.state_1,
			self.state_2,
			self.state_3,
			)

	def ret_dictionaly(self):
		return {
			"id":self.id,
			"music_name":self.music_name,
			"music_name_hiragana":self.music_name_hiragana,
			"artist":self.artist,
			"key":self.key,
			"state_1":self.state_1,
			"state_2":self.state_2,
			"state_3":self.state_3,
		}

def add_music_data(music_name, music_name_hiragana, artist, key):
	Base.metadata.create_all(engine)
	SessionMaker = sessionmaker(bind=engine)
	session = SessionMaker()
	
	check_data = get_music_data("music", music_name,"start")
	if(len(check_data) != 0):
		for data in check_data:
			if(check_data["music_name"] == music_name and check_data["artist"] == artist):
				return "same"

	data = Music(music_name=music_name, music_name_hiragana=music_name_hiragana, artist=artist, key=key)
	session.add(data)
	session.commit()
	return "ok"

def get_music_data(text, search_key, search_way):
	Base.metadata.create_all(engine)
	SessionMaker = sessionmaker(bind=engine)
	session = SessionMaker()
	
	if(text == ";"):
		data = session.query(Music).filter().all()
		result = [i.ret_dictionaly() for i in data]
		print("all search")
	elif(text == "rand;"):
		data = session.query(Music).filter().all()
		result = [i.ret_dictionaly() for i in data]
		result = [result[random.randint(0, len(result)-1)]]
		print(result)
	elif(search_key == "music"):
		data = session.query(Music).filter((Music.music_name.like('%'+text+'%')) | Music.music_name_hiragana.like('%'+text+'%')).all()
		change_data = [i.ret_dictionaly() for i in data]

		result = []
		print(change_data)
		if(search_way == 'start'):
			for datum in change_data:
				if(datum['music_name'].startswith(text) or datum['music_name_hiragana'].startswith(text)):
					result.append(datum)
		else:
			result = change_data
	else:
		data = session.query(Music).filter(Music.artist.like('%'+text+'%')).all()
		change_data = [i.ret_dictionaly() for i in data]

		result = []
		print(change_data)
		if(search_way == 'start'):
			for datum in change_data:
				if(datum['artist'].startswith(text)):
					result.append(datum)
		else:
			result = change_data

	return result

def get_music_data_by_id(id):
	Base.metadata.create_all(engine)
	SessionMaker = sessionmaker(bind=engine)
	session = SessionMaker()
	
	result = session.query(Music).filter(Music.id == id).all()

	return result[0].ret_dictionaly()

def change_music_data(id, music_name, music_name_hiragana, artist, key):
	Base.metadata.create_all(engine)
	SessionMaker = sessionmaker(bind=engine)
	session = SessionMaker()
	
	data = session.query(Music).filter(Music.id == id).all()[0]
	data.id = id
	data.music_name = music_name
	data.music_name_hiragana = music_name_hiragana
	data.artist = artist
	data.key = key
	session.commit()

def delete_music_data(id):
	Base.metadata.create_all(engine)
	SessionMaker = sessionmaker(bind=engine)
	session = SessionMaker()
	
	data = session.query(Music).filter(Music.id == id).all()[0]
	session.delete(data)
	session.commit()

def get_artist_data():
	Base.metadata.create_all(engine)
	SessionMaker = sessionmaker(bind=engine)
	session = SessionMaker()

	data = session.query(Music).filter().all()

	artists = list(set([i.ret_dictionaly()["artist"] for i in data]))
	print(artists)

	return artists

class StateNames(Base):
	__tablename__ = 'state_names'
	user_id = Column(Integer, primary_key=True, unique=True)
	state_name_1 = Column(String)
	state_name_2 = Column(String)
	state_name_3 = Column(String)

	def __repr__(self):
		return "StateNames<{}, {}, {}, {}>".format(
			self.user_id,
			self.state_name_1,
			self.state_name_2,
			self.state_name_3
			)

	def ret_dictionaly(self):
		return {
			"user_id":self.user_id,
			"state_name_1":self.state_name_1,
			"state_name_2":self.state_name_2,
			"state_name_3":self.state_name_3,
		}

def get_state_data_by_id(id):
	Base.metadata.create_all(engine)
	SessionMaker = sessionmaker(bind=engine)
	session = SessionMaker()
	
	result = session.query(Music).filter(Music.id == id).all()

	return result[0].ret_dictionaly()