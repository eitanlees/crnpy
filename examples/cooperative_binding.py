import sys
import os
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..'))

from crnpy.crn import CRN, from_react_file

# Cooperative binding

print "Creating model..."
crn = from_react_file("data/reactions/cooperative_binding")
crn.inspect(True)

print

print("Remove ps1, ps2 and ps3 by qss")
crn.remove(qss = ['ps1', 'ps2', 'ps3'], debug = True)
for s, f in crn.removed_species: print(s + " = " + str(f))
crn.inspect(True)