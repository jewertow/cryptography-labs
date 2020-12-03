#!/bin/bash

for i in "$@"
do
case $i in
    -s=*|--size=*)
    SIZE="${i#*=}"
    shift
    ;;
    -u=*|--unit=*)
    UNIT="${i#*=}"
    shift
    ;;
esac
done

if ! [[ "$SIZE" =~ ^[0-9]+$ ]]
then
    echo "Given size is not a number: $SIZE"
    exit 1
fi

MULTIPLIER=1

if [[ "$UNIT" == "K" ]]
then
    MULTIPLIER=1
elif [[ "$UNIT" == "M" ]]
then
    MULTIPLIER=1000
elif [[ "$UNIT" == "G" ]]
then
    MULTIPLIER=1000000
else
    echo "Given unit is not a number: $UNIT"
    exit 1;
fi

ABSOLUTE_SIZE=$((SIZE * MULTIPLIER))
OUTPUT_FILE_NAME="input/${SIZE}${UNIT}b.txt"

for (( i=0; i<$ABSOLUTE_SIZE; i++ ))
do
    cat 1Kb.txt >> $OUTPUT_FILE_NAME
done
