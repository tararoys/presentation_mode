mode: user.permitted_commands
-

settings():
    speech.timeout = 0.300

{user.permitted_commands} : 
    mode.enable('command')
    mode.disable('user.permitted_commands')
    mimic(permitted_commands)
    mode.disable('command')
    mode.enable('user.permitted_commands')

<phrase>: user.add_to_history()

#^listen: skip()

#^dictate: skip()

^listen <phrase>$: 
    user.momentary() 

^dictate <phrase>$:
    user.momentary_dictation()




