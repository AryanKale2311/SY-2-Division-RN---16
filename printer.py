class Printer:     
    __instance = None      
    def __new__(cls):         
        if cls.__instance is None:             
            cls.__instance = super(Printer, cls).__new__(cls)             
            print("Printer object created.")         
            return cls.__instance      
    def print_document(self, user, document):         
        print(f"{user} is printing: {document}")  
        printer1 = Printer() 
        printer2 = Printer() 
        printer3 = Printer()  
        printer1.print_document("User1", "Project Report") 
        printer2.print_document("User2", "Assignment") 
        printer3.print_document("User3", "Resume") 
        print("\nObject IDs:") 
        print(id(printer1)) 
        print(id(printer2)) 
        print(id(printer3))  
        if printer1 is printer2 is printer3:     
            print("\nOnly one Printer object exists (Singleton verified).") 
        else:     
            print("\nMultiple Printer objects exist.") 