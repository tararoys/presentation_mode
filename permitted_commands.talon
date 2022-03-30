mode: user.permitted_commands
-

settings():
    speech.timeout = 0.300

{user.permitted_commands} : 
    user.dont_add_to_history()
    mode.enable('command')
    mode.disable('user.permitted_commands')
    mimic(permitted_commands)
    mode.disable('command')
    mode.enable('user.permitted_commands')
    user.add_to_history()

<phrase>: user.add_to_history()

#^listen: skip()

#^dictate: skip()

^listen <phrase>$: 
    user.dont_add_to_history()
    user.momentary() 

^dictate <phrase>$:
    user.dont_add_to_history() 
    user.momentary_dictation()

Hello worldhello worldhello world




