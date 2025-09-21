class event:
    def __init__(self,data):
        self.data = data
        self.next = None
        
from colorama import Fore, Back, Style
class eventProcess:
    def __init__(self):
        self.head = event(None)
    #method to add new event
    def Addevent(self,data):
        if self.head.data == None:
            self.head.data = data
            print(Fore.GREEN+f"{self.head.data} event is added to the queue")
            return
        temp = self.head
        while(temp.next !=None):
            temp = temp.next
        newnode = event(data)
        temp.next = newnode
        print(Fore.GREEN+f"{newnode.data} event is added to the queue")
        return
            
    #method to process the event
    def process(self):
        if(self.head.data == None):
            print(Fore.RED+"No Event to process...")
            return
        process = self.head.data
        self.head = self.head.next
        print(Fore.GREEN+f"event {process} has been porcessed")
        return
    
    #method to display all events
    def display(self):
        if(self.head.data == None):
            print(Fore.RED+"No Event to Display")
            return
        temp = self.head
        print(Fore.BLUE+"Displaying event waiting to be processed\n")
        while(temp != None):
            print(f"Event {temp.data} waiting to be processed")
            temp = temp.next
        return
    
    #method to cancle the event
    def cancel(self,data):
        if(self.head.data == None):
            print(Fore.RED+"No event present to cancle")
            return
        temp = self.head
        if(temp.data == data):
            self.head = self.head.next
            print(Fore.GREEN+f"Event {data} is cancled...")
            return
        while(data != temp.next.data and temp != None):
            temp = temp.next
        print(Fore.GREEN+f"Event {temp.next.data} is cancled...")
        temp.next = temp.next.next
        return


if __name__ == "__main__":
    ep = eventProcess()  # Create an instance of the class
    con = True

    while con:
        print(Fore.CYAN + "\n1. Add event\n2. Process event\n3. Cancel event\n4. Display events\n5. Exit the system")
        try:
            task = int(input("Enter your operation: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number from 1 to 5.")
            continue

        if task == 1:
            data = input("Enter event: ")
            ep.Addevent(data)
        elif task == 2:
            ep.process()
        elif task == 3:
            data = input("Enter event to cancel: ")
            ep.cancel(data)
        elif task == 4:
            ep.display()
        elif task == 5:
            con = False
            print(Fore.YELLOW + "Exiting the system. Goodbye!")
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")