# ==========MATCH CASE ==========

# ALTERNATE FOR IF-ELIF-ELSE 
color = input("enter color: ")

match color:
    case "Green": # take one look at identation 
        print("Go")
    case "Yellow":
        print("Look")
    case "Red" :
        print("Stop")
    case _: # this is default case ==>> when no other ase will executed then it's willl be executed
        print("Wrong color!")