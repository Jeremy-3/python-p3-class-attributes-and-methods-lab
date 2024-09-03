
class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self,name,artist,genre):
        self.name=name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artsit_count(artist)
        
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        return cls.count
            
    
    @classmethod
    def add_to_genres(cls,genres):
        cls.genres.append(genres)
        return cls.genres
    
    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.append(artist)
        return cls.artists       
    
    @classmethod
    def add_to_genre_count(cls,genre):
        if genre in cls.genre_count:
            cls.genre_count [genre] += 1
        else:
            cls.genre_count [genre]  = 1   
            
    @classmethod
    def add_to_artsit_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else: 
            cls.artist_count [artist] = 1 
                      