#!/bin/sh

tmux  new-session -d
# Add top pane status , place to print/show pane title
tmux set -g pane-border-status top
tmux split-window -v
tmux select-pane -t 0
# Print pane title
tmux send-keys "printf '\033]2;main\033\\'" ENTER 
tmux send-keys "clear" ENTER
tmux send-keys "cd ~/projects/skid" ENTER
# tmux send-keys "gazebo --verbose gz/worlds/rover_ardupilot.world" ENTER
tmux send-keys "gzserver --verbose gz/worlds/rover_ardupilot.world" ENTER

tmux select-pane -t 1
tmux send-keys "printf '\033]2;tree-view\033\\'" ENTER 
tmux send-keys "clear" ENTER
tmux send-keys "cd ~/projects/skid/bin" ENTER
tmux send-keys "./gz2loopback" ENTER

tmux att