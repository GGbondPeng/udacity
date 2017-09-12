import webbrowser
class Movie():
    '''class for create movie obj'''
    def __init__(self,title,movie_url,poster_image_url):
        self.title = title
        self.trailer_youtube_url = movie_url
        self.poster_image_url = poster_image_url
    def show_movie(self):
        webbrowser.open(self.movie_url)

        