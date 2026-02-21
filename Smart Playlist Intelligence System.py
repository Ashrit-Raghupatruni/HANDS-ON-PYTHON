user_input = input("Enter playlist (example: [180, 200, 220, 210]): ")
parts = user_input.split(",")
playlist = []
for p in parts:
    if p.strip() != "":
        playlist.append(int(p.strip()))
invalid = False
for d in playlist:
    if d <= 0:
        invalid = True
        break
if invalid:
    print("Invalid Playlist")
else:
    total_duration = sum(playlist)
    songs = len(playlist)
    repetitive = False
    for d in playlist:
        if playlist.count(d) > 1:
            repetitive = True
            break
    if total_duration < 300:
        category = "Too Short Playlist"
        recommendation = "Add more songs"
    elif total_duration > 3600:
        category = "Too Long Playlist"
        recommendation = "Reduce playlist length"
    elif repetitive:
        category = "Repetitive Playlist"
        recommendation = "Add variety"
    else:
        if (max(playlist) - min(playlist)) > 30:
            category = "Balanced Playlist"
            recommendation = "Good listening session"
        else:
            category = "Irregular Playlist"
            recommendation = "Needs better balance"

    print("Total Duration:", total_duration, "seconds")
    print("Songs:", songs)
    print("Category:", category)
    print("Recommendation:", recommendation)