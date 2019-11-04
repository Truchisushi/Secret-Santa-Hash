# Secret-Santa-Hash
Python solutiuon for secret santa.

Requirements -> Need to have data.dat file in the same location as main.py

**data.dat** needs to have the following format:

person1
person2
person3 exclude1 exclude2
person4 exclude3
person5
...

Here person1, person2, etc. are the names of people participating in secret santa. The exclude1, exclude2, ... are people that need to be excluded from that specific persons line when considering secret santa matches.

The output will be saved in *output.out* containing a list of matches:

person1 person2
person3 person5
person4 person6
...
