from backend import Backend
import sys

class Frontend:

    def sys_argvs(self):
        if len(sys.argv) == 1:
            return self.print_help()
        elif sys.argv[1] == "-l":
            return self.list_tasks()

    def print_help(self):
        print(
            "                       \n"
            "Python Todo application\n"
            "=======================\n"
            "                       \n"
            "Command line arguments:\n"
            "-l   Lists all the tasks\n"
            "-a   Adds a new task\n"
            "-r   Removes an task\n"
            "-c   Completes an task")

    def list_tasks(self):
        backend = Backend()
        for x in  backend.open_separate():
            if x[0] == '0':
                print("[ ]"," - ", x[1])
            elif x[0] == '1':
                print("[x]"," - ", x[1])
    



front = Frontend()
front.sys_argvs()