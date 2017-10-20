# Arrow_IntroToPython

This is the workshop plan for the Introduction to Python Workshop for the [Arrow Conference](https://www.arrownyc.org/).


## Before we begin

#### Python2 vs. Python3
Same idea, slightly different syntax for certain operations (ie: printing, division).
Python2 will no longer be maintained by 2020. Unfortunately some libraries do not support Python3
I'm teaching Python3.

#### Code editors
Atom, Sublime Text, Vim (needs some configuration), Idle, PyCharm (IDE by Jetbrains)
Free, except for PyCharm Professional Edition (luckily there's a Community Edition)
Atom, Sublime Text, and Vim go with your terminal

#### Running Python
```
$ python
$ python mycoolfile.py
```
or
```
$ python3
$ python3 mycoolfile.py
```
Python automatically installed with Mac. Windows does not have this.


#### Questions?
## Let's Start!

We're going to making a mini-artist look up program. Let's say we're given some streaming data (a csv file) from a certain period of time. This data contains the tracks which were played from a certain period of time. Their representatives want to know the tracks which were played and their artist's most popular track. Let's start!

### 1: Basics
First, go to your terminal. In your terminal, create a new folder `artist_db`. Then cd into your folder to create a new file called `artist_db.py`. After, download the csv from [here](https://drive.google.com/file/d/0BxDLztvJC_1KRGZkQVlfdm0zWjQ/view?usp=sharing) and add it to your project. The command-line instructions are below.

```
$ mkdir artist_db
$ cd artist_db
$ touch artist_db.py
$ mv ~/Downloads/artists.csv .
```

Open up artist_db.py and say hello!
```python
# artist_db.py

print('hello!')
```

Now, wrap it in function
```python
# artist_db.py

# declare function
def main():
  print('hello!')

# call function
main()
```

Let's prompt our user.
```python
# artist_db.py

def main():
  user_artist = input('Enter an artist: ') # "raw_input" for python2
  print(user_artist)

main()
```

Let's add some formatting!
```python
# artist_db.py

def main():
  user_artist = input('Enter an artist: ') # "raw_input" for python2
  print('I\'m looking for...{artist}'.format(artist=user_artist))

main()
```

Now that we know the basics, we can start building out our mini-database.

### 2: The Database

We will create a new function in `artist_db.py`. This will be our mini-database for storing artists and their information.

First, let's create the function, a dictionary (also known as a map), and a return statement
```Python
# artist_db.py

def create_db(filename='str'):
  db = {}

  return db
```

Now let's start parsing out our csv. We'll import the csv library, open our file, and instantiate our csv reader. We have `','` as our delimiter since we know the file we are given will be comma separated.
```Python
# artist_db.py
import csv

def create_db(filename='str'):
  db = {}

  with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')

  return db
```

Next, we will iterate through our csv reader and get the values.
```Python
# artist_db.py
import csv

def create_db(filename='str'):
  db = {}

  with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')

    # parse out csv
    for row in reader:
        artist = row[0].lower()
        track = row[1]
        album = row[2]
        url = row[3]
        popularity = row[4]

  return db
```

Now, we will add the data from the csv to our database.
```Python
# artist_db.py
import csv

def create_db(filename='str'):
  db = {}

  with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')

    # parse out csv
    for row in reader:
        artist = row[0].lower()
        track = row[1]
        album = row[2]
        url = row[3]
        popularity = row[4]

        track_tuple = (track, album, url, popularity)

        db[artist] = [track_tuple]

  return db
```

Let's add a validation feature when adding something to the database. We want to make sure we get all our data!
```Python
# artist_db.py
import csv

def create_db(filename='str'):
  db = {}

  with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')

    # parse out csv
    for row in reader:
        artist = row[0].lower()
        track = row[1]
        album = row[2]
        url = row[3]
        popularity = row[4]

        track_tuple = (track, album, url, popularity)

        # construct db
        if db.get(artist) == None:
            db[artist] = [track_tuple]
        else:
            track_info = db[artist]
            track_info.append(track_tuple)

            db[artist] = track_info

  return db
```

Awesome! We have our database!

### 3: Validating inputs
Let's move back to our `main()`. We have something which looks like this
```python
# artist_db.py

def main():
  user_artist = input('Enter an artist: ') # "raw_input" for python2
  print('I\'m looking for...{artist}'.format(artist=user_artist))

main()
```

We want to do 2 things with our `main()`. First, we want to call `create_db()`.
```python
# artist_db.py

def main():
  db = create_db('artists.csv')

  user_artist = input('Enter an artist: ') # "raw_input" for python2
  print('I\'m looking for...{artist}'.format(artist=user_artist))

main()
```

Excellent. Now, we want to separate our user prompt to a different function. This is for cleaner code.

```python
# artist_db.py

def get_inputs():
  user_artist = input('Enter an artist: ') # "raw_input" for python2

  return user_artist

def main():
  db = create_db('artists.csv')
  user_artist = get_inputs()

main()
```

This is great. But we want to prevent using invalid data, like data we do not have in the database, from being used. We can do this with a while-loop and test the user data against the data we have.

```Python
# artist_db.py

def get_inputs(db={}):
  user_artist = input('Enter an artist: ') # "raw_input" for python2

  while (db.get(user_artist.lower()) == None):
      print('Error: Your artist cannot be found! Please try again')
      user_artist = input('Enter an artist: ')

  return user_artist

def main():
  db = create_db('artists.csv')
  user_artist = get_inputs(db)

main()
```

Awesome! Now, we need to work on finding our artist.

### 4: Finding the Artist
Let's create a new function which finds the artist's information.

```Python
# artist_db.py

def find_artist(artist='str'):
  return artist
```

Now, let's work with `main()` to work with the function we just wrote and find the artist in our db.

```Python
# artist_db.py

def find_artist(db={}, artist='str'):
  return artist

def main():
  db = create_db('artists.csv')
  user_artist = get_inputs(db)
  find_artist(db, user_artist)
```

Next, we will find our artist in the db we passed in. We don't need to check if the artist is there since we do this in `get_inputs(db)`.

```Python
# artist_db.py

def find_artist(db={}, artist='str'):
  artist = artist.lower()
  tracks = db[artist]

  return tracks

def main():
  db = create_db('artists.csv')
  user_artist = get_inputs(db)
  find_artist(db, user_artist)
```

Back in `main()`, we want to be able to have access to the tracks so let's set it as a variable.
```Python
# artist_db.py

def find_artist(db={}, artist='str'):
  artist = artist.lower()
  tracks = db[artist]

  return tracks

def main():
  db = create_db('artists.csv')
  user_artist = get_inputs(db)
  tracks = find_artist(db, user_artist)
```

We're almost done! We just need to print the information from `find_artist(db, user_artist)`.

### 5: Print
Let's create a function to print the information we have. This is where we will also also print out the most popular song and the total number of tracks. We will also call this function from main.

```Python
# artist_db.py

def print_info(tracks=[], user_artist='str'):
  print tracks

def main():
  db = create_db('artists.csv')
  user_artist = get_inputs(db)
  tracks = find_artist(db, user_artist)

  print_info(tracks, user_artist)
```

In print_info, let's setup a few strings to print.
```Python
# artist_db.py

def print_info(tracks=[], user_artist='str'):
  artist = '\n\nHere is some information about {artist}:'
  track_info = '=======================================================================\n' \
  'TRACK: {track}\n' \
  'ALBUM: {album}\n' \
  'SPOTIFY_URL: {url}\n' \
  'POPULARITY: {popularity}\n'
  total_info = '\nTOTAL NUMBER OF TRACKS: {total}'
  popular_info = 'MOST POPULAR TRACK:\n'
```

Now, let's sort the tracks so we print them in order. To do this, we will need to import itemgetter.

```Python
# artist_db.py
from operator import itemgetter

def print_info(tracks=[], user_artist='str'):
  artist = '\n\nHere is some information about {artist}:'
  track_info = '=======================================================================\n' \
  'TRACK: {track}\n' \
  'ALBUM: {album}\n' \
  'SPOTIFY_URL: {url}\n' \
  'POPULARITY: {popularity}\n'
  total_info = '\nTOTAL NUMBER OF TRACKS: {total}'
  popular_info = 'MOST POPULAR TRACK:\n'

  tracks = sorted(tracks, key=itemgetter(1))
```

Let's work on printing our header or the artist's name.
```Python
# artist_db.py
from operator import itemgetter

def print_info(tracks=[], user_artist='str'):
  artist = '\n\nHere is some information about {artist}:'
  track_info = '=======================================================================\n' \
  'TRACK: {track}\n' \
  'ALBUM: {album}\n' \
  'SPOTIFY_URL: {url}\n' \
  'POPULARITY: {popularity}\n'
  total_info = '\nTOTAL NUMBER OF TRACKS: {total}'
  popular_info = 'MOST POPULAR TRACK:\n'

  tracks = sorted(tracks, key=itemgetter(1))

  print(artist.format(artist=user_artist.title()))
```

Now, let's iterate through each track and print out its information.
```Python
# artist_db.py
from operator import itemgetter

def print_info(tracks=[], user_artist='str'):
  artist = '\n\nHere is some information about {artist}:'
  track_info = '=======================================================================\n' \
  'TRACK: {track}\n' \
  'ALBUM: {album}\n' \
  'SPOTIFY_URL: {url}\n' \
  'POPULARITY: {popularity}\n'
  total_info = '\nTOTAL NUMBER OF TRACKS: {total}'
  popular_info = 'MOST POPULAR TRACK:\n'

  tracks = sorted(tracks, key=itemgetter(1))

  print(artist.format(artist=user_artist.title()))
  for track in tracks:
    track = track_info.format(track=track[0], album=track[1].title(), url=track[2], popularity=popularity)
        print(track)
```

Great! We have most of it done. Now, we let's add the total number of tracks counter.
```Python
# artist_db.py
from operator import itemgetter

def print_info(tracks=[], user_artist='str'):
  artist = '\n\nHere is some information about {artist}:'
  track_info = '=======================================================================\n' \
  'TRACK: {track}\n' \
  'ALBUM: {album}\n' \
  'SPOTIFY_URL: {url}\n' \
  'POPULARITY: {popularity}\n'
  total_info = '\nTOTAL NUMBER OF TRACKS: {total}'
  popular_info = 'MOST POPULAR TRACK:\n'

  tracks = sorted(tracks, key=itemgetter(1))
  total = len(tracks) # We add this!

  print(artist.format(artist=user_artist.title()))
  for track in tracks:
    track = track_info.format(track=track[0], album=track[1].title(), url=track[2], popularity=popularity)
    print(track)

  print(total_info.format(total=total)) # We also added this!
```

Lastly, let's add the popularity counter. What we're doing is comparing the previously most popular track with the current track.
```Python
# artist_db.py
from operator import itemgetter

def print_info(tracks=[], user_artist='str'):
  artist = '\n\nHere is some information about {artist}:'
  track_info = '=======================================================================\n' \
  'TRACK: {track}\n' \
  'ALBUM: {album}\n' \
  'SPOTIFY_URL: {url}\n' \
  'POPULARITY: {popularity}\n'
  total_info = '\nTOTAL NUMBER OF TRACKS: {total}'
  popular_info = 'MOST POPULAR TRACK:\n'

  tracks = sorted(tracks, key=itemgetter(1))
  total = len(tracks)
  most_popular = 0 # We add this!

  print(artist.format(artist=user_artist.title()))
  for track in tracks:
    popularity = int(track[3]) # We also add this!

    track = track_info.format(track=track[0], album=track[1].title(), url=track[2], popularity=popularity)
    print(track)

    # Most importantly, add this!
    if popularity > most_popular:
        popular_info = 'MOST POPULAR TRACK:\n' + track
        most_popular = popularity


  print(total_info.format(total=total))
  print(popular_info) # let's print the info we just added!
```

## YOU'RE DONE!

If you would like to read more about Python, check out...
- [learnxiny](https://learnxinyminutes.com/docs/python3/)
- [learnpython.org](https://www.learnpython.org/)
- [Codecademy: Python](https://www.codecademy.com/learn/learn-python)
