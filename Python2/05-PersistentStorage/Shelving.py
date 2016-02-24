__author__ = 'Fadel'

import shelve

# Build up the Database
shelf = shelve.open("favorites")
shelf["movie_list"] = ["X man","Lord of the rings"]
shelf["songs_list"] = ["cos I love u","I believe I can fly","turn down for what"]
shelf.close()

# Editing the database
shelf2 = shelve.open("favorites")
edit_songs_list = shelf2["songs_list"]
edit_songs_list.append("Imagine")
shelf2["songs_list"] = edit_songs_list
shelf2.close()


# Editing the Database
shelf3 = shelve.open("favorites",writeback=True)
shelf3["songs_list"].append("Im a single "
                            ""
                            "")
shelf3.sync()
shelf3.close()

# Viewing the Database
shelf4 = shelve.open("favorites")
print(shelf4["songs_list"])
