class Hospital:
    all_doctors ={}
    appointments=[]

    def __init__(self, name, specialize):
        self.name = name
        self.specialize = specialize
        Hospital.all_doctors[self.name] = [self.specialize]
        Hospital.appointments.append(str(self.name))
        for i in range (3):
                Hospital.appointments.append(0)


    @classmethod
    def add_doctor(cls):
        name=str(input("enter the doctor's name"))
        specialize=str(input("enter his specializtion"))
        Hospital.all_doctors[name] = [specialize]
        Hospital.appointments.append((name,"","",""))
        print("the doctor has been added succefully")
        return

    @classmethod
    def get_all_doctors(cls):
        print(str(Hospital.all_doctors))
        return

    @classmethod
    def get_doctors_by_specialize(cls):
        d=[]
        specialize=str(input("enter the specialzation"))
        for i,z in Hospital.all_doctors.items():
            if [specialize]==z:
                d.append(i)
        print(f"the doctors who specialize at {str(specialize)} are {d}")
        return

    def __str__(self):
        print(f"{self.name} from {self.specialize}")

    @classmethod
    def view(cls):
        doctor_name=str(input("inter doctor name"))
        if doctor_name not in Hospital.appointments:
            print(f"the name {str(doctor_name)} is not found")
            return
        else:
            for i in range (len(Hospital.appointments)):
                if Hospital.appointments[i] == doctor_name:
                    print(f"{str(doctor_name)} have appointments are {Hospital.appointments[i+1]}",end="")
                    print(f"{Hospital.appointments[i+2],Hospital.appointments[i+3]}")
                    return

    @classmethod
    def book(cls):
        print(f"{Hospital.appointments}")
        name =(input("please enter doctor name"))
        z=(input("enter the patient name"))
        s=int(input("time (24 hours)"))
        print(name)
        if s >24 or s<0:
            print("you have entered a wrong time")
            return
        found = False
        for i in range(len(Hospital.appointments)):
            if Hospital.appointments[i] == name:
                if Hospital.appointments[i+3]==0:
                    Hospital.appointments.insert(i+1,[z,s])
                    print(f"{z} will have an appointment at {s} with Dr. {name}")
                    found = True
                    break
                elif Hospital.appointments[i+3] !=0:
                    print("the doctor time taple is full")

        if not found:
            print("You have entered a wrong doctor name. please try again")








doctor1 = Hospital("ahmed", "sss")
doctor2 = Hospital('ayman', "ddd")
doctor3 = Hospital("ali", "fff")
doctor4 = Hospital("mohamed", "ddd")
doctor5 = Hospital("bakry","sss")
print("welcome in our hospital \n how can we assist you today")
print("choose a munber for what you like to do : \n 1_ add a doctor")
print("2_if you want to see all of our doctors \n3_ if you want all doctors who work in a specialization")
print("4_ if you want to book\n5_if you want to view doctors plans")
while True:
    try:
        x=input()
        if x== "stop":
            break
        x=int(x)
        if x==1:
            Hospital.add_doctor()
        elif x==2:
            Hospital.get_all_doctors()
        elif x==3:
            Hospital.get_doctors_by_specialize()
        elif x==4:
            Hospital.book()
        elif x==5:
            Hospital.view()
        elif x>5:
            print("you have chosen a wrong option,please try again")
    except ValueError:
        print("you have entered a wrong option, please try again")