# magicians6.py, Chapter 4, Python Crash Course
# program uses a for loop to print a list of names
# of magicians
#
# program also includes an unnecessary indentation,
# which produces a logical error
#

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you, everyone. That was a great magic show!")



