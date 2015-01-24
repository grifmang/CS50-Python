hash = 2
counter = 1
height = raw_input("Enter the height of your mario wall (1-23): ")
row = int(height) - 1
if height <= 0:
    print "Please enter a height greater than zero."
if height > 23:
    print "Please enter a height of 23 or less."
while counter < int(height):
    print " " * row, \
          "#" * hash, \
          " ", \
          "#" * hash, \
          " " * row
    hash += 1
    counter += 1
    row -= 1