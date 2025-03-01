def read_write_file():
    songs = []
    with open('canciones.txt' , 'r') as file:
        for line in file:
            #content = file.read()
            songs.append(line)
            
    #list_of_songs = content.split()
    ordered_songs = sorted(songs)

    with open('ordered_songs' , 'w') as output_file:
        for song in ordered_songs:
            output_file.write(song + '\n')

    print('ordered_songs.txt')


read_write_file()