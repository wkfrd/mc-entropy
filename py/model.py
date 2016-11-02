import web

# Define the database we will be writing to. Theoretically this works. Ugh.
mc_database = web.database(dbn='mysql', db='wakeforc1_db', user='wakeforc1', pw='w8n2fr')

# List of things we want to do with the database, functions
#__________________________________________________________

# Create user upon registration, store email and password in DB. Username not
# a necessary function of this, as it is not a social website.
def create_user():
	pass

# Deletes a user from the database by email.
def delete_user():
	pass

# A song point is what I have dubbed the shortened string that expands to make
# beuatiful music. It translates a few aspects of a song that I have yet to
# create, ergo I cannot yet provide a good explanation of how that works.
def add_song_point():
	pass

# Should really only be called upon user deletion of all of their preferences
# through their time with MC Entropy, or when the limit of the song points in
# the database is reached.
def remove_song_point():
	pass

# The big one. Use previous knowledge on the user from the database to create
# a new song point worthy of them. Store it in the database. I will explain how
# to generate music in a friendly format
def generate_song_point():
	pass

# AHHHHHHHHHHHH
def generate_visuals():
	pass
