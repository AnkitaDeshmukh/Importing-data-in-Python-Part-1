#Import titanic.csv using the function np.recfromcsv() and assign it to the variable, d.
# You'll only need to pass file to it because it has the defaults delimiter=',' and names=True in addition to dtype=None!
# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])

