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

scale=$1
chord=$2

python3 chords.py $scale $strings $tuning $chord
