#!/usr/bin/python

print "\nHello, Python!"

str1 = 'Hello World!'

print str1          # Prints complete string
print str1[0]       # Prints first character of the string
print str1[2:5]     # Prints characters starting from 3rd to 5th
print str1[2:]      # Prints string starting from 3rd character
print str1* 2      # Prints string two times
print str1 + "TEST" # Prints concatenated string

del str1

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "Mark"       # A string

print "\nCounter: " + str(counter)
print "\nMiles: " + str(miles)
print "\nName: " + str(name)
# or
print "\nCounter: %d" % (counter)

var1 = 1
var2 = "Mark"

print var1
print var2

var1 = 2
del var2

print var1
#print var2  #errors because del var2

raw_input("\n\nPress the enter key to exit.")
