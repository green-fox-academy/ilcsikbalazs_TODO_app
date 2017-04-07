from backend import Backend
import sys
from prettytable import *

class Frontend:
    def sys_argvs(self):
        if len(sys.argv) == 1:
            return self.print_help()
        elif sys.argv[1] == "-l":
            if len(sys.argv) == 2:
                return self.list_tasks()
            elif len(sys.argv) >= 2:
                print("You can't have an argument after -l")
        elif sys.argv[1] == "-a":
            backend = Backend()
            add_this = " ".join(sys.argv[2:])
            return backend.write_into_file(add_this)
        elif sys.argv[1] == "-r":
            backend = Backend()
            remove_this = " ".join(sys.argv[2:])
            return backend.remove_a_task(remove_this)
        elif sys.argv[1] == "-c":
            backend = Backend()
            check_this = " ".join(sys.argv[2:])
            backend.check_it(check_this)

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
        for x in range(len(backend.open_separate())):
            if backend.open_separate()[x][0] == '0':
                no_enter = backend.open_separate()[x][1].replace("\n","")
                print(x+1,"[ ]"," - ", no_enter)
            elif backend.open_separate()[x][0] == '1':
                no_enter = backend.open_separate()[x][1].replace("\n","")
                print(x+1,"[x]"," - ", no_enter)
    




front = Frontend()
front.sys_argvs()