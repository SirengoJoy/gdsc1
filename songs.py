import json
import os #initiates the os library which will be used later on to open the playlists directories
import random;

folderName="Playlists"   #You make sure you playlists folder is named 'Playlists'

tracks=os.listdir(folderName) # This command now reads the directory of the folder_name which is 'Paylists'. So your folder name for playlists must be saved Playlists.

while True:  #initiating a loop which will make the program ask for input unless one decides to quit.

    songName = input("\n\nEnter the song or artist name (Enter q to quit): ").lower()      #When one enters 'q' as input, we will terminate the while loop initiated above.
    
    def readfile(file):
        filePath = folderName+"/"+file+".json"
        if(not os.path.isfile(filePath)):   #If the directory is not found return false
           return False
        
        with open(filePath) as f:
            data = json.load(f) # Load the JSON data from the file into a Python dictionary
            
            totalSongs = len(data) # Get the total number of songs in the JSON data
            for song in data:
                found = False
                if song['song'].lower() == songName:
                    found = True
                    print("Below are great alternatives to ", song['song'], ":\n")
                if song['artist'].lower() == songName:
                    found = True
                    print("Recommended alternatives for", song['artist'], "song:",song['song'],"\n")

                if found:
                    print(file ,"alternatives:")
                    for i in range(3):
                        songNumber = random.randint(0, totalSongs)
                        song = data[songNumber]['song'] # Access the 'song' key to get the song name
                        artist = data[songNumber]['artist'] # Access the 'artist' key to get the artist name
                        print(str(i+1) + ". " + song + " by " + artist)
                    return True
            else:
                return False
            

    if songName=="q":  #Here we now implement the loop termination. If one inserts q as input, we break. That means that the program stops running.
        print("Thank you for using our recommendation system.... ")     #This is the message the user gets
        break                                                       #The program is then terminated
            

    checker = False
    for track in tracks:
        track_name= str.split(track, ".")
        if(readfile(track_name[0]) and track_name[1] == "json"):  #checks if the file in the folder has a ".json" part. In short checking if it is json file.
            checker = True
            break

    if checker == False: 
        print("Song not found. Can you please check the spelling.")