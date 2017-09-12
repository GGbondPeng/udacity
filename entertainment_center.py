import fresh_tomatoes
import media

movie_lists = [
            ["Alien:Covenant",'https://www.youtube.com/watch?v=svnAD0TApb8','https://upload.wikimedia.org/wikipedia/zh/thumb/4/48/Alien_Covenant_Poster.jpg/220px-Alien_Covenant_Poster.jpg'],
            ["Pacific Rim",'https://www.youtube.com/watch?v=B7-EqMGOM4E','https://resizing.flixster.com/MIJJI53SxxKEU56ewWLh3ZeGDYg=/300x300/v1.bTsxMTE3MzkzMztqOzE3NDk5OzEyMDA7ODAwOzEyMDA']
        ]
movie_obj = [];
for e in movie_lists:
    #print e
    movie_obj.append(media.Movie(e[0],e[1],e[2]))
#fresh_tomatoes.create_movie_tiles_content([alien_covenant])
fresh_tomatoes.open_movies_page(movie_obj)
