#!/bin/bash
tuning="E A D G B E"
strings=6
while getopts "n:t:" TUNE
do
	case $TUNE in
		t)
			tuning=$OPTARG;;
		n)
			strings=$OPTARG;;
	esac
done

shift $(( OPTIND - 1 ))

if (( $# != 2 ))
then
	echo -e "Usage: ./chordmap.sh -n 'number of strings' -t 'tuning' 'scale' 'chord numbers'\nEx: ./chordmap.sh -t 'D A D G A D' 'A' '6 5 4 3M'\n"
	echo 'press enter to exit'
	read enter
	exit
fi
scale=$1
chord=$2

python3 chords.py $scale $strings $tuning $chord
