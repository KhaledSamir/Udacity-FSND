import Media
import fresh_tomatoes

TOYSTORY = Media.Movie('Toy Story',
                       'A Story of Toy like a boy!',
                       'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                       'https://www.youtube.com/watch?v=NTdKQzVFeis')

AVATAR = Media.Movie('Avatar',
                     'A Marine on an alient planet',
                     'http://www.impawards.com/2009/posters/avatar_xlg.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

WHITEFANG = Media.Movie('White Fang',
                        'A story of half dog and half wolf',
                        'http://www.impawards.com/1991/posters/white_fang_xlg.jpg',
                        'https://www.youtube.com/watch?v=u6rpsATIqes')

TITANIC = Media.Movie('Titanic',
                      'A sink ship on 1914',
                      'https://www.movieposter.com/posters/archive/main/142/MPW-71146',
                      'https://www.youtube.com/watch?v=zCy5WQ9S4c0')

movies = [TOYSTORY, AVATAR, WHITEFANG, TITANIC]
#fresh_tomatoes.open_movies_page(movies)

print Media.Movie.VALIDRATINGS
print Media.Movie.__name__
print Media.Movie.__doc__
print Media.Movie.__module__