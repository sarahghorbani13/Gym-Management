class halls :
    def __init__ (self) :
        self.halls_list = []
        # self.add ("red", "10", "dumbbell , mat")
        # self.add ("green", "15", "mat, treadmill")
        # self.add ("blue", "20", "yoga block, mat")
            
    def add (self, name, capacity, equipment) : # افزودن سالن
        for hall in self.halls_list :
            if (hall['name'] == name) :
                print ("\nthis hall already exists!\n")
                return
        if (capacity.isdigit() and int(capacity) >= 0) : 
            new_hall = {"name":name, "capacity":capacity, "equipment":equipment, "status":True}
            self.halls_list.append (new_hall)
            # print (f"\n{name} added!\n")
        else:
            print ("\ninvalid type of capacity!\n")        

    def edit (self) : # ویرایش سالن
        flag = False
        if not self.halls_list :
            print ("\nno halls!\n")
        else:
            editname = input ("\nname of hall to edit : ")
            for hall in self.halls_list :
                if hall['name'] == editname :
                    flag = True
                    newcapacity = input ("\nnew capacity : ")
                    if (newcapacity.isdigit() and int(newcapacity) >=0 ) :
                        newequipment = input ("\nnew equipment : ")
                        hall['capacity'] = newcapacity
                        hall['equipment'] = newequipment
                        break
                    else :
                        print ("\ninvalid type of capacity!\n")
            if not flag :
                print(f"\n{editname} is not in halls\n")
    
    def view (self) : # مشاهده سالن ها
        if not self.halls_list :
            print ("\nno halls!\n")
        else:
            for hall in self.halls_list :
                print(f"\nname:{hall['name']}\ncapacity:{hall['capacity']}\nequipment:{hall['equipment']}\nstatus:{hall['status']}\n")    

    def halls_status (self) : # فعال و غیر فعال کردن سالن
        flag = False
        if not self.halls_list :
            print ("\nno halls!\n")
        else:
            nametoendis = input ("\nwhich hall do you want to enable/disable? ")
            for hall in self.halls_list :
                if (hall['name'] == nametoendis) :
                    flag = True
                    hall['status'] = not hall['status']
                    if hall['status'] :
                        text = "Enabled"
                    else :
                        text = "Disabled"
                    print (f"\n{hall['name']} is {text}\n")
                    break
            if not flag :
                print(f"\n{nametoendis} is not in halls\n")

    def enable_halls (self) : # برگرداندن لیست سالن های فعال
        enable_list = []
        for hall in self.halls_list :
            if hall['status'] :
                enable_list.append (hall['name'])
        return (enable_list)

result = halls()
# result.add ("red", "10", "dumbbell , mat")
# result.add ("green", "15", "mat, treadmill")
# result.add ("blue", "20", "yoga block, mat")
if __name__ == "__main__" :
    while True :
        menu = ("1. add hall\n"
                "2. editing hall\n"
                "3. view halls\n"
                "4. enabled or disabled the hall\n"
                "5. exit")
        num = input(menu+"\n\nplease select one item : ")
        if (num=="1") :
            name = input("\nenter name : ")
            capacity = input("\nenter capacity : ")
            equipment = input("\nenter equipment : ")
            result.add (name, capacity, equipment)
        elif (num=="2") :
            result.edit()
        elif (num=="3") :
            result.view()
        elif (num=="4") :
            result.halls_status()
        elif (num=="5") :
            print("\nbye!\n")
            break
        else :
            print ("\ninvalid choice!\n")
