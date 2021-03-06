#
# animation script notation
# (wait 200) sets default wait to 200ms
# 1 play frame 1, if horizontal or vertical
# (1 2) play frame 2 for 2 sec
# [1 2] play frame (1, 2)
# (1 2 3) or [1 2 3] play frame (1, 2) for 3ms
# > set to positive order
# < set to reverse order
# ^ start here
# $ if reached, end
# >$ restart
# (pos 1 2 3) move 1px right, 2px down [in 3 ms]
# (back 3) move back to 0,0 in [3 ms]
# (# 10) stall 10 ms
# 'wait_anim' call special functions, in this case, wait for animation to complete
