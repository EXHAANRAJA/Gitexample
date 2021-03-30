# Get key and related value through dictionary 

#Dictionary initialized
movieonair = {"No Time to Die":"11:00 AM",
               "Black Down":"12:00 AM",
               "Hooper" :"13:00 AM"}

# User input from upper mentioned movies
print("which movie you want to see we are airing following movies:")
for key in movieonair:
    print(key)

watchinterest=input("Please provide your interest IN airing movies:")
watchtime = movieonair.get(watchinterest)


# Search dictionary to find the selected movies
if watchinterest in movieonair:
    print(watchinterest + " will air on night " + watchtime)
else:
    print("Please stay in touch for your choice we will air soon")    



