not mode: sleep

-

^presentation mode$: 
    mode.disable('command')
    mode.disable('dictation')
    mode.enable('user.permitted_commands')

^disable presentation mode$: 
    mode.enable('command')
    mode.disable('user.permitted_commands')



