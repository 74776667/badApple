from instagrapi import Client
import credentials
import os
import time
import re
cl = Client()


def logIntoClient():
    user = credentials.USERNAME
    psswrd = credentials.PASSWORD
    cl.login(user,psswrd)
    loginOk = cl.create_note("Succesfully logged in!",0)
    time.sleep(5)
    loginBA = cl.create_note("Bad Apple in instagram!!!!",0)

    
logIntoClient()

def extract_frame_number(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group()) if match else -1

def read_emoji_art_files(folder_path):
    files_processed = 0
    files_skipped = 0

    # Get the list of .txt files and sort them numerically
    files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    files.sort(key=extract_frame_number)

    for filename in files:
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                time.sleep(0.0350)
                print(f"Reading file: {filename}")
                emoji_art = file.read()
                print(emoji_art)

                print("\n")
            files_processed += 1
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
            files_skipped += 1
    
    print(f"Processed {files_processed} files successfully.")
    print(f"Skipped {files_skipped} files due to errors.")


#AFter you've rendered everything, paste the emoji art folde path here

emojiArtPath = 'PATH'


read_emoji_art_files(emojiArtPath)

