from talon import Module, actions, speech_system, scope

flag = False
dictation_flag = False

def on_phrase_post(j):
    global flag
    global dictation_flag
    if flag:
        flag = False
        checked_modes = list(scope.get('mode').intersection({'sleep', 'dictation', 'user.permitted_commands'}))
        # make sure we're in sleep or dictation mode:
        if len(checked_modes) == 1:
            mode = checked_modes[0]
            actions.mode.enable('command')
            actions.mode.disable(mode)
            try:
                # NOTE: the following API is completely private and subject to change with no notice
                speech_system._on_audio_frame(j['samples'])
            finally:
                actions.mode.disable('command')
                actions.mode.enable(mode)
    elif dictation_flag == True: 
        dictation_flag = False
        checked_modes = list(scope.get('mode').intersection({'sleep', 'command', 'user.permitted_commands'}))
        # make sure we're in sleep or dictation mode:
        if len(checked_modes) == 1:
            mode = checked_modes[0]
            actions.mode.enable('dictation')
            actions.mode.disable(mode)
            try:
                # NOTE: the following API is completely private and subject to change with no notice
                print('rerunning audio')
                speech_system._on_audio_frame(j['samples'])
            finally:
                actions.mode.disable('dictation')
                actions.mode.enable(mode)
speech_system.register('post:phrase', on_phrase_post)

mod = Module()
@mod.action_class
class Actions:
    def momentary():
        """Wake up Talon and re-run the entire current audio"""
        global flag
        flag = True
    
    def momentary_dictation():
        """wake up talon and dictate entire current audio"""
        global dictation_flag
        dictation_flag = True



 