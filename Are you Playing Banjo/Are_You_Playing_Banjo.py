#If your name starts with R you play banjo

def are_you_playing_banjo(name):
    Name = name.upper()
    if Name[0] == 'R':
        Play = f"{name} plays banjo"
    else:
        Play = f"{name} does not play banjo"
    print(Play)

#Function
name = input("What's your name? ")
are_you_playing_banjo(name)


