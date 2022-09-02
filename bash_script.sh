#!/bin/bash
trap 'Blad' SIGINT

username=$1
password=$2
ip=$3

#Dzialajace polaczenie ssh
START=$SECONDS
sshpass -p "$2" ssh -o StrictHostKeyChecking=no $1@$3
duration=$(( SECONDS - start ))


echo "$duration"
if [ $duration -gt 1 ];
then
  sleep 0.5
  clear
fi
