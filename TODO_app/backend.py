class Backend:
    def open_separate(self):
        tasks_read = open('basic_tasks.txt', 'r')
        input_read = tasks_read.readlines()
        output = []
        for i in input_read:
            output.append(i.split(","))
        return output      

    def write_into_file(self,after_a):
        task_write = open('basic_tasks.txt', 'a')
        append = "0,"+after_a+"\n"
        input_write = task_write.writelines(append)

    def save_file(self):
        open_file = self.open_separate()
        for i in open_file:
            for j in i:
                print(j)

    def remove_a_task(self,remove_this):
        open_file = self.open_separate()
        string = remove_this + "\n"
        for i in open_file:
            if i[1] == string:
                open_file.remove(i)
                print(open_file)


a = Backend()
a.save_file()