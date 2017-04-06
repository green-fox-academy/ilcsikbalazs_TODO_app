class Backend:
    
    def open_separate(self):
        tasks_read = open('basic_tasks.txt', 'r')
        inputs = tasks_read.readlines()
        output = []
        for i in inputs:
            output.append(i.split(","))
        return output      

