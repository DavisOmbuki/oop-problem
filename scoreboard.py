def create_scoreboard(participants):
    scoreboard = []
    
    for participant in participants:
        name = participant["name"]
        score = 5 * participant["Chickenwings"] + 3 * participant["Hamburgers"] + 2 * participant["Hotdogs"]
        scoreboard.append({"name": name, "score": score})
    
    sorted_scoreboard = sorted(scoreboard, key=lambda x: (-x["score"], x["name"]))
    
    return sorted_scoreboard
