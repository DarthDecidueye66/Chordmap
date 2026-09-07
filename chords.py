import sys

args = sys.argv
scale = args[1]
strings_no = int(args[2])
tuning = args[3:(3+strings_no)]
chords = args[(3+strings_no):]
target=[]

#debug string 
#print(f"scale:{scale}\nstrgno:{strings_no}\ntuning:{tuning}\nchords:{chords}")


#--------------------------------------------------------------------------------------------
#init chord list
#--------------------------------------------------------------------------------------------
degrees_rom={
        "i":0,
        "i#":1,
        "ii":2,
        "ii#":3,
        "iii":4,
        "iv":5,
        "iv#":6,
        "v":7,
        "v#":8,
        "vi":9,
        "vi#":10,
        "vii":11,
        }

targets = {
        'scale':['1', '2', '3', '4', '5', '6', '7'],

        '1':['1', '3', '5'],
        '2':['2', '4', '6'],
        '3':['3', '5', '7'],
        '4':['4', '6', '1'],
        '5':['5', '7', '2'],
        '6':['6', '1', '3'],
        '7':['7', '2', '4'],

        '1M':['1', '3', '5'],
        '2M':['2', '4#', '6'],
        '3M':['3', '5#', '7'],
        '4M':['4', '6', '1'],
        '5M':['5', '7', '2'],
        '6M':['6', '1#', '3'],
        '7M':['7', '2#', '4#'],

        '1m':['1', '2#', '5'],
        '2m':['2', '4', '6'],
        '3m':['3', '5', '7'],
        '4m':['4', '5#', '1'],
        '5m':['5', '6#', '2'],
        '6m':['6', '1', '3'],
        '7m':['7', '2', '4#'],

        '1d':['1', '2#', '4#'],
        '2d':['2', '4', '5#'],
        '3d':['3', '5', '6#'],
        '4d':['4', '5#', '7'],
        '5d':['5', '7', '1#'],
        '6d':['6', '1', '2#'],
        '7d':['7', '2', '4'],

        '1a':['1', '3', '5#'],
        '2a':['2', '4#', '6#'],
        '3a':['3', '5#', '1'],
        '4a':['4', '6', '1#'],
        '5a':['5', '7', '2#'],
        '6a':['6', '1#', '4'],
        '7a':['7', '2#', '4#'],
        }



#--------------------------------------------------------------------------------------------
#cleaning input and removing extra garbage values/wrong usages
#--------------------------------------------------------------------------------------------
rmlist=[]

for i in chords:
    #print(i)
    if i.strip() not in targets.keys():
        rmlist.append(i)

for i in rmlist:
    chords.remove(i)

chords.insert(0, 'scale')
#print(f"fixed chords: {chords}")


#--------------------------------------------------------------------------------------------
#init fretboard
#--------------------------------------------------------------------------------------------
degree_nums_full = [' 1 ', ' 1#', ' 2 ', ' 2#', ' 3 ', ' 4 ', ' 4#', ' 5 ', ' 5#', ' 6 ', ' 6#', ' 7 ']
degree_nums = [' 1 ', '   ', ' 2 ', '   ', ' 3 ', ' 4 ', '   ', ' 5 ', '   ', ' 6 ', '   ', ' 7 ']

notes = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "G#", "A", "Bb", "B"]
notes_print = [" C ", " C#", " D ", " Eb", " E ", " F ", " F#", " G ", " G#", " A ", " Bb", " B "]

frets = [" 0 ", '   ', '   ', ' . ', '   ', ' . ', '   ', ' . ', '   ', ' . ', '   ', '   ', ' : ', '   ', '   ', ' . ', '   ', ' . ']
header = ['_' for i in range(60)]


#--------------------------------------------------------------------------------------------
#print full fretboard
#--------------------------------------------------------------------------------------------

board = [frets]
strings = tuning

print() #making space for fretboard
for strng in strings[:strings_no]:
    lst = []
    offset = notes.index(strng)
    for i in range(18):
        lst.append(notes_print[(i + offset) % 12])
    board.append(lst)


for row in board:
    print(" | ".join(row))
    pass
print("\n")


#--------------------------------------------------------------------------------------------
#print chord positions
#--------------------------------------------------------------------------------------------

board = [frets]
scale_offset = notes.index(scale)


for chord in chords:
    print(f"[ {chord} ]:\n")
    for strng in strings[:strings_no]:
        lst = []
        offset = notes.index(strng)
        for i in range(18):
            term = degree_nums_full[(i + offset) % 12 - scale_offset]
            if term.strip() in targets[chord]:
                lst.append(term)
            else:
                lst.append('   ')
        board.append(lst)


    for row in board:
        print(" | ".join(row))
        pass

    print()

    board = [frets]

