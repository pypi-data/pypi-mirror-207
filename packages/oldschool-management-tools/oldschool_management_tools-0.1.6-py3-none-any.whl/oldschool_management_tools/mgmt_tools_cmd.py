import cmd
from oldschool_management_tools.calendar_tools import parse_day, prompt_day_tasks
from oldschool_management_tools.calendar_tools import CalendarReader


class MgmtToolsCmd(cmd.Cmd):
    intro = "Welcome to Old School Management Tools"
    prompt = "(mgmt) "

    def __init__(self):
        super(MgmtToolsCmd, self).__init__()
        self.calendar_reader = CalendarReader()

    def do_prompt_tasks(self, day):
        parsed_day = parse_day(day)
        prompt_day_tasks(parsed_day)

    def do_show_sched(self, day):
        parsed_day = parse_day(day)
        self.calendar_reader.show_day_sched(parsed_day)

    def do_fill_prep(self, day):
        parsed_day = parse_day(day)
        self.calendar_reader.fill_prep(parsed_day)

    def do_wipe_prep(self, day):
        parsed_day = parse_day(day)
        self.calendar_reader.wipe_prep(parsed_day)

    def do_die(self, args):
        return True


    def do_exit(self, args):
        return True

    def do_EOF(self, args):
        return True

def run():
    MgmtToolsCmd().cmdloop()
    exit(0)
