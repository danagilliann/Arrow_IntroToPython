import csv
from operator import itemgetter, attrgetter

def create_db(filename='str'):
    # db = {
    #   artist : {
    #       track: (album, url)
    #   }
    # }
    db = {}

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')

        # parse out csv
        for row in reader:
            artist = row[0].lower()
            track = row[1].lower()
            album = row[2]
            url = row[3]

            track_tuple = (track, album, url)

            # construct db
            if db.get(artist) == None:
                track_obj = {}

                db[artist] = [track_tuple]
            else:
                track_info = db[artist]
                track_info.append(track_tuple)

                db[artist] = track_info

    return db

def get_inputs(db={}):
    user_artist = input('Enter an artist: ')

    while (db.get(user_artist.lower()) == None):
        print("Error: Your artist cannot be found! Please try again")
        user_artist = input('Enter an artist: ')

    return user_artist

def find_artist(db={}, artist='str'):
    artist = artist.lower()
    tracks = db[artist]

    return tracks

def print_info(tracks=[], user_artist="str"):
    artist = "{artist} INFORMATION"
    info = "====================================================\n\
    TRACK: {track}\n\
    ALBUM: {album}\n\
    SPOTIFY_URL: {url}\n"
    total_info = "====================================================\n\
    TOTAL NUMBER OF TRACKS: {total}"

    tracks = sorted(tracks, key=itemgetter(1))
    total = 0

    print(artist.format(artist=user_artist.title()))
    for track in tracks:
        total += 1
        print(info.format(track=track[0].title(), album=track[1].title(), url=track[2]))

    print(total_info.format(total=total))

def main():
    db = create_db('artists.csv')
    user_artist = get_inputs(db)
    tracks = find_artist(db, user_artist)

    print_info(tracks, user_artist)

main()
