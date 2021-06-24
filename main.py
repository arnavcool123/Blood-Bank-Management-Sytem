import csv
from datetime import date

print(
    '                     ----------------------------WELCOME to Blood Bank Database ------------------------------------------------------------    \n')



def needblood():
    grp = input(' Enter needed Blood Group : ')
    print()
    grp = grp.upper()
    if grp not in ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'):
        grp = input(' Enter a valid Blood Group: ')
        print()
        grp = grp.upper()
    f = open('Blood Donor Data.csv', 'r+')
    list1 = []
    reader = csv.reader(f)
    found = False
    print(' Here is the list to find your Required Blood Type. \n')
    print(' Blood is Always present in 2 bottles of 470 ml \n')
    print(" Blood Group  \t Name \t Address \t Blood Donation Date \t Donor Contact No.")
    print()
    for i in reader:
        list1.append(i)
    for j in list1:
        if grp in j:
            print(j[0]+'\t'+j[1]+'\t'+j[2]+'\t'+j[3]+'\t'+j[4])
            f.close()
            found = True
    if found == False:
        print('Sorry no Match Found.\n ')
        reg = input('Do You want to Register your Details so that we can contact you later? (yes/no): \n')
        reg = reg.lower()
        if reg in ('yes', ' yes', 'yes ', ' yes '):
            append_file = open('Blood Recipient data.csv', 'a+', newline="")
            writer = csv.writer(append_file, delimiter=',')
            b = input('Enter Blood Need Priority from 1-5 , 1 having highest priority :')
            c = input('Enter Your Full Name: ')
            d = input('Enter your Address: ')
            e = input('Enter your Phone Number:')
            today = date.today()
            f = today.strftime("%d/%m/%y")
            st = [b, grp, c, d, f, e]
            writer.writerow(st)
            append_file.close()
            print('Entry Succesfully Saved! You will be Notified. \n')
            print('Thanks for Visiting! \n')
        if reg in ('no', ' no', 'no ', ' no '):
            print('Okay No Problem all your Personal Data is Deleted.\n')
            print('Thanks for Visiting! \n')
    else:
        print()
        print('We are Glad that you could find your Blood Type. \n')
        print('Thanks for Visiting! \n')

def enterblood():
    grp = input('Enter Donor Blood Group: ')
    grp = grp.upper()
    if grp not in ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'):
        grp = input('Enter a valid Blood Group: ')
        grp = grp.upper()
    nam = input("Enter Donor's Name: ")
    add = input("Enter Donor's Address: ")
    ph = input("Enter Donor's Phone Number: ")
    today1 = date.today()
    f1 = today1.strftime("%d/%m/%y")
    donor_file = open('Blood Donor Data.csv', 'a+', newline="")
    writer2 = csv.writer(donor_file, delimiter=',')
    io = [grp, nam, add, f1, ph]
    writer2.writerow(io)
    donor_file.close()
    print('Entry Succesfully Saved! Thankyou for Donating Blood. \n')
    files = open('Blood Recipient data.csv', 'r+')
    readers = csv.reader(files)
    names = []
    list1s = []
    for i in readers:
        list1s.append(i)
    lis = []
    for i in list1s:
        if grp in i:
            lis.append(i)
    if len(lis) > 0:
        print('Currently the following People are on a waitlist for ', grp, ' Blood Group. Please Contact Them.\n')
    for p in lis:
        print(p[0]+'\t'+p[1]+'\t'+p[2]+'\t'+p[3]+'\t'+p[4]+'\t'+p[5])
    if len(lis) > 0:
        print('Thanks for Visiting! \n')
    if len(lis) == 0:
        print('Currently the no one is on a waitlist for ', grp, ' Blood Group. Thanks for Visiting.\n')
    files.close()
def deleterecord():
    o = input('Do you want to delete record from Donor List or Recipient List  (donor/recipient):   ')
    o = o.lower()
    if o in ('donor', ' donor', 'donor ', ' donor '):
        file1 = open('Blood Donor Data.csv', 'r+')
        string1 = input("Enter name of Patient to remove: ")
        found = False
        reader = csv.reader(file1)
        list1 = []
        for j in reader:
            list1.append(j)
        for i in list1:
            if i[1] == string1:
                list1.remove(i)
                found = True
        file1.close()
        file1s = open('Blood Donor Data.csv', 'w+', newline="")
        writer = csv.writer(file1s)
        
        for i in list1:
            writer.writerow(i)
        file1s.close()
        if found == True:
            print(' Patient ', string1, ' found.\n')
            print(string1 + " has been Officially Removed from our Blood Bank Database. \n")
        if found == False:
            print(' Patient ', string1, ' not in our DataBase. \n')
    if o in ('recipient', ' recipient', 'recipient ', ' recipient '):
        file2 = open('Blood Recipient data.csv', 'r+')
        string2 = input("Enter name of Patient to remove: ")
        found2 = False
        line2 = ''
        for j2 in file2:
            if string2 in j2:
                line2 = j2[:-1]
                found2 = True
        file2.seek(0)
        text2 = file2.read()
        start2 = text2.index(line2)+5
        end2 = start2+len(line2)
        length2 = len(line2)
        file2.seek(start2)
        write2 = csv.writer(file2)
        b2 = ''
        write2.writerow(b2)
        file2.close()
        if found2 == True:
            print(' Patient ', string2, ' found.\n')
            print(string2 + " has been Officially Removed from our Blood Bank Database. \n")
        if found2 == False:
            print(' Patient ', string2, ' not in our DataBase. \n')
def modify():
    data = input('Do you want to delete record from Donor List or Recipient List  (donor/recipient):   ')
    print()
    name = input(' Enter Name of patient you want to modify: ')
    print()
    data = data.lower()
    if data in ('donor', ' donor', 'donor ', ' donor '):
        field = input(' What do you want to modify? (Blood Group/Address/Last Donation Date/Phone Number): ')
        print()
        if field in ('Blood Group', 'blood group', 'bloodgroup'):
            f = open('Blood Donor Data.csv', 'r+')
            new = input(' Enter new Blood Group: ')
            reader = csv.reader(f)
            l1 = []
            for i in reader:
                l1.append(i)
            for j in l1:
                if j[1] == name:
                    j[0] = new
            f.close()
            fs = open('Blood Donor Data.csv', 'w+', newline="")
            writer = csv.writer(fs)
            for k in l1:
                writer.writerow(k)
            fs.close()
            print(field, 'of ', name, 'has been updated and set to', new, '\n')
        if field in ('Address', 'address'):
            f = open('Blood Donor Data.csv', 'r+')
            new = input(' Enter new Address: ')
            reader = csv.reader(f)
            l1 = []
            for i in reader:
                l1.append(i)
            for j in l1:
                if j[1] == name:
                    j[2] = new
            f.close()
            fs = open('Blood Donor Data.csv', 'w+', newline="")
            writer = csv.writer(fs)
            for k in l1:
                writer.writerow(k)
            fs.close()
            print(field, 'of ', name, 'has been updated and set to', new, '\n')
        if field in ('Last Donation Date', 'last donation date', 'lastdonationdate'):
            f = open('Blood Donor Data.csv', 'r+')
            new = input(' Enter new Donation Date: ')
            reader = csv.reader(f)
            l1 = []
            for i in reader:
                l1.append(i)
            for j in l1:
                if j[1] == name:
                    j[3] = new
            f.close()
            fs = open('Blood Donor Data.csv', 'w+', newline="")
            writer = csv.writer(fs)
            for k in l1:
                writer.writerow(k)
            fs.close()
            print(field, 'of ', name, 'has been updated and set to', new, '\n')
        if field in ('Phone Number', 'phone number', 'phonenumber'):
            f = open('Blood Donor Data.csv', 'r+')
            new = input(' Enter new Phone Number Date: ')
            reader = csv.reader(f)
            l1 = []
            for i in reader:
                l1.append(i)
            for j in l1:
                if j[1] == name:
                    j[4] = new
            f.close()
            fs = open('Blood Donor Data.csv', 'w+', newline="")
            writer = csv.writer(fs)
            for k in l1:
                writer.writerow(k)
            fs.close()
            print(field, 'of ', name, 'has been updated and set to', new, '\n')
    if data in ('recipient', ' recipient', 'recipient ', ' recipient '):
        field = input(' What do you want to modify? (Blood Group/Address/Registration Date/Phone Number): ')
        if field in ('Blood Group', 'blood group', 'bloodgroup'):
            f = open('Blood Recipient data.csv', 'r+')
            new = input(' Enter new Blood Group: ')
            reader = csv.reader(f)
            l1 = []
            for i in reader:
                l1.append(i)
            for j in l1:
                if j[2] == name:
                    j[1] = new
            f.close()
            fs = open('Blood Recipient data.csv', 'w+', newline="")
            writer = csv.writer(fs)
            for k in l1:
                writer.writerow(k)
            fs.close()
            print(field, 'of ', name, 'has been updated and set to', new, '\n')
        if field in ('Address', 'address'):
            f = open('Blood Recipient data.csv', 'r+')
            new = input(' Enter new Address: ')
            reader = csv.reader(f)
            l1 = []
            for i in reader:
                l1.append(i)
            for j in l1:
                if j[2] == name:
                    j[3] = new
            f.close()
            fs = open('Blood Recipient data.csv', 'w+', newline="")
            writer = csv.writer(fs)
            for k in l1:
                writer.writerow(k)
            fs.close()
            print(field, 'of ', name, 'has been updated and set to', new, '\n')
        if field in ('Registration Date', 'registration date', 'registrationdate'):
            f = open('Blood Recipient data.csv', 'r+')
            new = input(' Enter Registration Date Address: ')
            reader = csv.reader(f)
            l1 = []
            for i in reader:
                l1.append(i)
            for j in l1:
                if j[2] == name:
                    j[4] = new
            f.close()
            fs = open('Blood Recipient data.csv', 'w+', newline="")
            writer = csv.writer(fs)
            for k in l1:
                writer.writerow(k)
            fs.close()
            print(field, 'of ', name, 'has been updated and set to', new, '\n')
        if field in ('Phone Number', 'phone number', 'phonenumber'):
            f = open('Blood Recipient data.csv', 'r+')
            new = input(' Enter New Contact Number Date Address: ')
            reader = csv.reader(f)
            l1 = []
            for i in reader:
                l1.append(i)
            for j in l1:
                if j[2] == name:
                    j[5] = new
            f.close()
            fs = open('Blood Recipient data.csv', 'w+', newline="")
            writer = csv.writer(fs)
            for k in l1:
                writer.writerow(k)
            fs.close()
            print(field, 'of ', name, 'has been updated and set to', new, '\n')


while True:
    func = input(
        " Type 'find' if you need to find Blood or \n Type 'delete' if you want to delete any record or \n Type 'enter'  if you want to register Blood Donor Information or \n Type 'modify' if you want to change any information regarding the patients or \n Type 'quit' if you want to quit : ")
    func = func.lower()
    print()
    if func in ('find ', ' find ', ' find', 'find'):
        needblood()
    elif func in ('enter', ' enter', 'enter ', ' enter '):
        enterblood()
    elif func in ('delete', ' delete', 'delete ', ' delete '):
        deleterecord()
    elif func in ('quit', ' quit', ' quit ', 'quit '):
        print(' Program Closed ')
        break
    elif func in ('modify', ' modify', 'modify ', ' modify '):
        modify()
    else:
        print('Invalid Choice. Please enter a valid Response.')
        fun = input(
            'Type "Find" if you need to find Blood or Type "Delete" if you want to delete any record or Type "Enter"  if you want to register Blood Donor Information or \n Type "modify" if you want to change any information regarding the patients or \n Type "Quit" if you want to quit :\n ')
        fun = fun.lower()
        print()
        if fun in ('find ', ' find ', ' find', 'find'):
            needblood()
        elif fun in ('enter', ' enter', 'enter ', ' enter '):
            enterblood()
        elif fun in ('delete', ' delete', 'delete ', ' delete '):
            deleterecord()
        elif fun in ('modify', ' modify', 'modify ', ' modify '):
            modify()
        elif func in ('quit', ' quit', ' quit ', 'quit ', 'exit'):
            print(' Program Closed ')
            break

    
