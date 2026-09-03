# Chordmap
My first git project: A small guitar fretboard mapping tool

Usage: ./chordmap.sh -n 'number of strings' -t 'tuning string' 'scale' 'chord numbers'

Ex: ./chordmap.sh -n 5 -t 'D A D G D' 'A' '6 5 4 3M'\n"


If no options are selected then the default number of strings is 6 and default tuning is 'E A D G B E'
The chords are takes as the scale degrees by default; 
1 ~ 1M (major)
2 ~ 2m (minor)
3 ~ 3m (minor)
4 ~ 4M (major)
5 ~ 5M (major)
6 ~ 6m (minor)
7 ~ 7d (diminished)

Any version of any chord may be given by suffixing with appropiate identifier as: major (M), minor (m), diminished (d) or augmented (a)
Ex: major 3 ~ 3M, augmented 5 ~ 5a


custom tunings can be entered in as: -t 'A D F G E B A A' etc
the number of strings given in -t must not be lower than the number of strings given in -n 
