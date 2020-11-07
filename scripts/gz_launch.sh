#!/bin/sh

tmux  new-session -d
# Add top pane status , place to print/show pane title
tmux set -g pane-border-status top
tmux split-window -v
tmux select-pane -t 0
tmux split-window -v

tmux select-pane -t 0
# Print pane title
tmux send-keys "printf '\033]2;Gazebo\033\\'" ENTER 
tmux send-keys "clear" ENTER
tmux send-keys "cd ~/projects/skid" ENTER
# tmux send-keys "gazebo --verbose gz/worlds/rover_ardupilot.world" ENTER
tmux send-keys "gzserver --verbose gz/worlds/rover_ardupilot.world" ENTER

tmux select-pane -t 1
tmux send-keys "printf '\033]2;Video\033\\'" ENTER 
tmux send-keys "clear" ENTER
tmux send-keys "cd ~/projects/skid/bin" ENTER
tmux send-keys "./gz2loopback" ENTER

tmux select-pane -t 2
tmux send-keys "printf '\033]2;SITL\033\\'" ENTER 
tmux send-keys "clear" ENTER
tmux send-keys "sleep 5" ENTER
tmux send-keys "sim_vehicle.py -v APMrover2 -f gazebo-rover  -m --mav10 -I1
" ENTER

tmux att