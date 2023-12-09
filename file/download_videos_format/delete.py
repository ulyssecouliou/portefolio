import os



def programme():
    for file_name in os.listdir():
        if file_name.endswith('.mp4'):
            os.remove(file_name)
            print("Fichier supprimé")
        if file_name.endswith('.txt'):
            os.remove(file_name)
            print("Fichier supprimé")
        if file_name.endswith('.mp3'):
            os.remove(file_name)
            print("Fichier supprimé")
            
programme()
