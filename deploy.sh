#!/bin/bash
# tmux kill-session -t django
# tmux new-session -d -s django
# tmux send-keys "cd ~/project/DialogueRobot" C-m
# tmux send-keys "git pull" C-m
# tmux send-keys "cd ~/project/DialogueRobot/DiaRobot" C-m
# tmux send-keys "sudo ~/.conda/envs/robot/bin/python manage.py makemigrations" C-m
# tmux send-keys "sudo ~/.conda/envs/robot/bin/python manage.py migrate" C-m
# tmux send-keys "sudo ~/.conda/envs/robot/bin/python manage.py runserver 0.0.0.0:80" C-m

port=80
pid=$(sudo netstat -nlp | grep :$port | awk '{print $7}' | awk -F"/" '{print $1}')
if [ -n "$pid" ]; then
    sudo kill -9 $pid;
fi
git -C ~/project/DialogueRobot pull
nohup sudo ~/.conda/envs/robot/bin/python ~/project/DialogueRobot/DiaRobot/manage.py runserver 0.0.0.0:80 > /dev/null 2>&1 &
