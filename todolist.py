class Todolist:
    def __init__(self):
        self.todolist=[]
       

    def add(self,task):
        self.todolist.append({"task":task,"status":"not completed"})
        print("Task added successfully")

    def delete(self,index):
        if 0<index<=len(self.todolist):
            
            del self.todolist[index-1]
            print("Task removed successfully")
        else:
            print("Invalid Index")

    def completed(self,index1):
        if 0<index1<=len(self.todolist):
            self.todolist[index1-1]["status"]="completed"
        else:
            print("invalid index")


    def display(self):
        if self.todolist:
            for  i,task in enumerate(self.todolist,start=1):
                if task["status"]=="completed":
                    print(f"{i}. ☑  {task["task"]}")
                else:
                    print(f"{i}. ☐  {task["task"]}")
        else:
            print("Your Todolist is empty")

todo=Todolist()
while True:
    print()
    print("\n1.Add Task\n2.Delete Task\n3.Mark Task as completed\n4.Display Your Todolist\n5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        task=input("Enter the task:")
        todo.add(task)
    elif choice==2:
        index=int(input("Enter the index to delete task:"))
        todo.delete(index)
    elif choice==3:
        index1=int(input("Enter the index to mark task as completed:"))
        todo.completed(index1)
    elif choice==4:
        todo.display()
    elif choice==5:
        print("END")
        break
    else:
        print("Invalid Choice")
    

