import re

# sentence = input()
sentence = "Please contact us at: support@github.com."

regex = "()[@]()"

matches = re.findall(regex, sentence, flags=)

print()


######################################################
# Input 1:
# Please contact us at: support@github.com.
# Output 1:
# support@github.com
# ######################################################
# Input 2:
# Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.
# Output 2:
# s.miller@mit.edu
# j.hopking@york.ac.uk
# ######################################################
# Input 3:
# Many users @ SoftUni confuse email addresses. We @Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de.
# Output 3:
# steve.parker@softuni.d
######################################################
