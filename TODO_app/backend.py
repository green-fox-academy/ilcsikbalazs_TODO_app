class Backend:
    def open_separate(self):
        tasks_read = open('basic_tasks.txt', 'r')
        input_read = tasks_read.readlines()
        output = []
        for i in input_read:
            output.append(i.split(","))
        tasks_read.close()
        return output      

    def write_into_file(self,after_a):
        task_write = open('basic_tasks.txt', 'a')
        append = "0,"+after_a+"\n"
        input_write = task_write.writelines(append)
        task_write.close()

    def remove_a_task(self,remove_this):
        open_file = self.open_separate()
        string = remove_this + "\n"
        for i in open_file:
            if i[1] == string:
                open_file.remove(i)

        for i in open_file:
            task_write = open('temporary.txt', 'a')
            add = i[0]+ "," +i[1]
            input_write = task_write.writelines(add)
        
        task_write.close()
        task_read = open('temporary.txt', 'r')
        basic_file = open('basic_tasks.txt', 'w')
        basic_file.write(task_read.read())
        basic_file.close()
        temporary_delete = open('temporary.txt', 'w')
        temporary_delete.write("")
        temporary_delete.close()