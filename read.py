# Read form file

random_file = open("random.txt", "r+")
print(random_file.readlines())

random_file.write("There are lots of crazy things in this world")
random_file.close()


