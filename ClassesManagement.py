from HallsManagement import halls
hallmethod = halls()
# from Coaches import coach
# coachmethod = coach()

class classes :
    def __init__(self):
        self.classes_list = []

    def add(self, name, sport, coach, hall, day, time, capacity) : # افزودن کلاس
        for cls in self.classes_list :
            if (cls['name'] == name) :
                print ("\nthis class already exists!\n")
                return
        if hall not in hallmethod.enable_halls() :
            print (f"\n{hall} does not exist or is not enable!\n")
            return
        # if coach not in coachmethod.enable_coaches() :
        #         print (f"\n{coach} does not exist or is not enable!\n")
        #         return
        new_cls = {"name":name, "sport":sport, "coach":coach, "hall":hall, "day":day, "time":time, "capacity":int(capacity), "register":0, "status":True}
        self.classes_list.append (new_cls)
        # print (f"\n{name} added!\n")
    
    def edit (self) : # ویرایش کلاس
        flag = False
        if not self.classes_list :
            print ("\nno classes!\n")
        else:
            editname = input ("\nname of class to edit : ")
            for cls in self.classes_list :
                if cls['name'] == editname :
                    flag = True
                    newname = input ("\nnew name : ")
                    newsport = input ("\nnew sport : ")
                    newcoach = input ("\nnew coach : ")
                    # if newcoach not in coachmethod.enable_coaches() :
                    #     print (f"\n{newcoach} does not exist or is not enable!\n")
                    #     return
                    newhall = input ("\nnew hall : ")
                    if newhall not in hallmethod.enable_halls() :
                        print (f"\n{newhall} does not exist or is not enable!\n")
                        return
                    else :
                        newday = input ("\nnew day : ")
                        newtime = input ("\nnew time : ")
                        newcapacity = input ("\nnew capacity : ")
                        cls['name'] = newname
                        cls['sport'] = newsport
                        cls['coach'] = newcoach
                        cls['hall'] = newhall
                        cls['day'] = newday
                        cls['time'] = newtime
                        cls['capacity'] = int (newcapacity)
            if not flag :
                print(f"\n{editname} is not in classes\n")

    def view(self) : # مشاهده کلاس ها
        if not self.classes_list :
            print ("\nno classes!\n")
        else:
            for cls in self.classes_list :
                if cls['status'] :
                    remaincapacity = int (cls['capacity']) - int (cls['register'])
                    print(f"\nname:{cls['name']}\nsport:{cls['sport']}\ncoach:{cls['coach']}\nhall:{cls['hall']}\nday:{cls['day']}\ntime:{cls['time']}\ncapacity:{cls['capacity']}\nremaincapacity:{remaincapacity}\nstatus:{cls['status']}\n")
    
    def classes_status(self) : # فعال و غیر فعال کردن کلاس
        flag = False
        if not self.classes_list :
            print ("\nno classes!\n")
        else:
            nametoendis = input ("\nwhich class do you want to enable/disable? ")
            for cls in self.classes_list :
                if (cls['name'] == nametoendis) :
                    flag = True
                    cls['status'] = not cls['status']
                    if cls['status'] :
                        text = "Enabled"
                    else :
                        text = "Disabled"
                    print (f"\n{cls['name']} is {text}\n")
                    break
            if not flag :
                print(f"\n{nametoendis} is not in classes\n")

    def enable_classes (self) : # برگرداندن لیست کلاس های فعال
        enable_list = []
        for cls in self.classes_list :
            if cls['status'] :
                enable_list.append (cls['name'])
        return (enable_list)

result = classes()
result.add ("trx", "hard", "ali" , "red", "monday", "10:00 am", "10")
result.add ("yoga", "soft", "reza" , "green", "friday", "08:00 am", "15")
result.add ("handball", "hard", "zahra" , "blue", "sunday", "07:00 pm", "20")
if __name__ == "__main__" :
    while True :
        menu = ("1. add class\n"
                "2. editing class\n"
                "3. view class\n"
                "4. enabled or disabled the class\n"
                "5. exit")
        num = input(menu+"\n\nplease select one item : ")
        if (num=="1") :
            name = input("\nenter name : ")
            sport = input("\nenter sport : ")
            coach = input("\nenter coach : ")
            hall = input("\nenter hall : ")
            day = input("\nenter day : ")
            time = input("\nenter time : ")
            capacity = input("\nenter capacity : ")
            result.add (name, sport, coach, hall, day, time, capacity)
        elif (num=="2") :
            result.edit()
        elif (num=="3") :
            result.view()
        elif (num=="4") :
            result.classes_status()
        elif (num=="5") :
            print("\nbye!\n")
            break
        else :
            print ("\ninvalid choice!\n")