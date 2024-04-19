class MovieResponse:

    class MPAARating:
        def __init__(self, type, label):
            self.type = type
            self.label = label        
    
    def __init__(self, id, name, description, img_path, duration, genre, language, mpaa_rating_type, mpaa_rating_label, user_rating) -> None:
        self.id = id
        self.name= name
        self.description = description
        self.img_path = img_path
        self.duration = duration
        self.genre = genre
        self.language = language
        self.mpaaRating = self.MPAARating(mpaa_rating_type, mpaa_rating_label)
        self.user_rating = str(user_rating)