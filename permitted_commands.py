from talon import Context, Module, app, clip, cron, imgui, actions, ui, fs
import os

mod = Module()
ctx = Context()

mod.list("permitted_commands", desc="A restricted subset of commands for use during a tutorial or presentation or the like")
mod.mode("permitted_commands", desc="A mode for a restricted subset commands")

cwd = os.path.dirname(os.path.realpath(__file__))
permitted_command_file = os.path.join(cwd, "presentation_commands.csv")

def update_permitted_commands(name, flags):
    if name != permitted_command_file:
        return

    phones = {}
    canonical_list = []
    with open(permitted_command_file, "r") as f:
        for line in f:
            words = line.rstrip()
            canonical_list.append(words)


    global all_permitted_command
    all_permitted_command = phones
    ctx.lists["user.permitted_commands"] = canonical_list
    print(ctx.lists['user.permitted_commands'])

update_permitted_commands(permitted_command_file, None)
fs.watch(cwd, update_permitted_commands)

