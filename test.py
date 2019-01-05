x = "maxborka"
sname = x+".txt"
file = open(sname, "r", encoding='utf-8')
filetxt = file.readlines()
file.close


def linefinder(x):
    return 0

def infofinder(x):
    poi_all = filetxt[linefinder(x)]
    poi_1 = poi_all.split("§")[0]
    poi_2 = poi_all.split("§")[1]
    poi_3 = poi_all.split("§")[2]
    poi_4 = poi_all.split("§")[3]

def findline(x):
    linefinder_file = open(sname, "r", encoding='utf-8')
    linefinder_list = []
    linefinder_list = linefinder_file.readlines()
    linefinder_file.close
    search_target = x
    search_found = 0
    curline = 0
    while search_found != 1:
        rootline = linefinder_list[curline]
        line_string = rootline.split("§")[0]
        curline += 1
        if line_string == search_target:
            search_found = 1
            finding = curline-1
    return finding

def find_ansatt_navn(x):
    navnrad = filetxt[findline(x)]
    return  navnrad.split("§")[0]

def find_ansatt_id(x):
    idrad = filetxt[findline(x)]
    return  navnrad.split("§")[1]

def find_ansatt_model(x):
    modelrad = filetxt[findline(x)]
    modelverdi = modelrad.split("§")[2]
    if modelverdi == "t1":
        return "Hourly Employee"
    if modelverdi == "t2":
        return "Employee"

def find_ansatt_timer(x):
    timerad = filetxt[findline(x)]
    return   timerad.split("§")[4]

def find_ansatt_lonn(x):
    lonnrad = filetxt[findline(x)]
    return  lonnrad.split("§")[3]

def employee_mainfile_string (x,y,z,q,t):
    ems_navn = x
    ems_id = y
    ems_model = z
    ems_lonn = q
    ems_timer = t
    string = (ems_navn+"§"+str(ems_id)+"§"+ems_model+"§"+str(ems_lonn)+"§"+str(ems_timer)+"§\n")
    string.encode('utf-8', 'ignore').decode('utf-8')
    return string

def add_employee(x,y,z,q,t):
    add_employee_main = open(sname, "r+", encoding='utf-8')
    add_employee_main_content = add_employee_main.read()
    updates = employee_mainfile_string(x,y,z,q,t)
    add_employee_main_content += updates
    add_employee_main.write(add_employee_main_content)
    add_employee_main.close()
