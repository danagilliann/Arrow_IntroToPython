import csv
from operator import itemgetter


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


def get_inputs(db={}):
    user_artist = input('Enter an artist: ')

    while (db.get(user_artist.lower()) == None):
        print('Error: Your artist cannot be found! Please try again')
        user_artist = input('Enter an artist: ')

    return user_artist


def find_artist(db={}, artist='str'):
    artist = artist.lower()
    tracks = db[artist]

    return tracks


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
    most_popular = 0

    print(artist.format(artist=user_artist.title()))
    for track in tracks:
        popularity = int(track[3])

        track = track_info.format(track=track[0], album=track[1].title(), url=track[2], popularity=popularity)
        print(track)

        if popularity > most_popular:
            popular_info = 'MOST POPULAR TRACK:\n' + track
            most_popular = popularity

    print(total_info.format(total=total))
    print(popular_info)


def main():
    db = create_db('artists.csv')
    user_artist = get_inputs(db)
    tracks = find_artist(db, user_artist)

    print_info(tracks, user_artist)

main()
