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
        input_write = task_write.writelines("0,"+after_a+"\n")
        task_write.close()

    def remove_a_task(self,remove_this):
        open_file = self.open_separate()
        string = remove_this + "\n"
        for i in open_file:
            if i[1] == string:
                open_file.remove(i)
        #create temporary txt file
        for i in open_file:
            task_write = open('temporary.txt', 'a')
            add = i[0]+ "," +i[1]
            input_write = task_write.writelines(add)
        #temporary's data copy to basic_tasks file
        task_write.close()
        task_read = open('temporary.txt', 'r')
        basic_file = open('basic_tasks.txt', 'w')
        basic_file.write(task_read.read())
        basic_file.close()
        temporary_delete = open('temporary.txt', 'w')
        temporary_delete.write("")
        temporary_delete.close()

    def check_it(self,check_this):
        open_file = self.open_separate()
        string = check_this + "\n"
        for i in open_file:
            if i[1] == string:
                if i[0] == "1":
                    i[0] = "0"
                elif i[0] == "0":
                    i[0] = "1"
        # #create temporary txt file
        for i in open_file:
            task_write = open('temporary.txt', 'a')
            add = i[0]+ "," +i[1]
            input_write = task_write.writelines(add)
        # #temporary's data copy to basic_tasks file
        task_write.close()
        task_read = open('temporary.txt', 'r')
        basic_file = open('basic_tasks.txt', 'w')
        basic_file.write(task_read.read())
        basic_file.close()
        temporary_delete = open('temporary.txt', 'w')
        temporary_delete.write("")
        temporary_delete.close()
        


            
        