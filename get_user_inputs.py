def userInputs():
    while True:
        use_default = input("Would you like to generate the playlist with default(d) or personalized(p) configurations?")
        if use_default == "d":
            limit = 30
            market="US&UK"
            seed_genres="slow"
            target_danceability=1.0
            uris = [] 
            artist = "w"

            return limit, market,
    
        if use_default == "p":
            limit = input("")
    
            check = input("The setting is. Is this correct?")
            return limit

