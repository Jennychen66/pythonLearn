import fresh_tomatoes
import media

qiyiDoctor = media.Movie("qiyiDoctor",
                         "the story of world-famous neurosurgeon Dr. Stephen Strange whose life changes forever after a horrific car accident robs him of the use of his hands ",
                         "qiyiDoctor.jpg",
                         "http://www.mgtv.com/b/303020/3801140.html")
print(qiyiDoctor.storyline)

print(media.Movie.__doc__)

print(media.Movie.__name__)

print(media.Movie.__module__)

#qiyiDoctor.show_trailer()
movies=[qiyiDoctor]


fresh_tomatoes.open_movies_page(movies)

