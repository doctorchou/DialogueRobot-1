#!/bin/bash
tmux kill-session -t django
tmux new-session -d -s django
tmux send-keys "cd ~/DialogueRobot" C-m
tmux send-keys "git pull" C-m
tmux send-keys "cd ~/DialogueRobot/DiaRobot" C-m
tmux send-keys "sudo ~/.conda/envs/robot/bin/python manage.py makemigrations" C-m
tmux send-keys "sudo ~/.conda/envs/robot/bin/python manage.py migrate" C-m
tmux send-keys "sudo ~/.conda/envs/robot/bin/python manage.py runserver 0.0.0.0:80" C-m
# port=8000
# pid=$(netstat -nlp | grep :$port | awk '{print $7}' | awk -F"/" '{print $1}')
# if [ -n "$pid" ]; then
#     kill -9 $pid;
# fi

# source /usr/local/anaconda3/etc/profile.d/conda.sh
# conda activate robot
# git -C ~/DialogueRobot pull
# nohup python ~/DialogueRobot/DiaRobot/manage.py runserver 0.0.0.0:8000 >/dev/null 2>&1 &
