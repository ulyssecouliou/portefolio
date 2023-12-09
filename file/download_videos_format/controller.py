import delete, download, getId, prog, videos_to_tiktok

# on entre le nom de la chaine youtube dans le terminal
while True:
    channel_name = input("Entrez le nom de la chaîne YouTube que vous souhaitez scraper: ")
    channel_id = getId.get_channel_id_by_name(channel_name)
    if channel_id:
        with open('channel_id.txt', 'w') as file:
            file.write(channel_id)
        print(f"L'ID du canal '{channel_name}' a été enregistré dans channel_id.txt")
        break
    else:
        print(f"Le canal '{channel_name}' n'a pas été trouvé.")






 
