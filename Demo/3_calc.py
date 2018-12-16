# 学生成绩

stu_list = []

while True:
    cmd = input('请输入命令，add，search，exit，calc\n')
    if cmd == 'add':
        line = input('请输入成绩格式，姓名，语文，数学\n')
        elem = line.strip().split(',')
        if(len(elem) !=3):
            print('格式不对')
            continue
        stu_name = elem[0]
        chinese_score = float(elem[1])
        math_score = float(elem[2])
        stu_list.append([stu_name,chinese_score,math_score])
        print(stu_list)
    elif cmd == 'search':
        line = input('输入要查找的姓名\n')
        stu_name = line.strip()
        for i in range(0,len(stu_list)):
            if stu_name == stu_list[i][0]:
                print(stu_list[i])
                break
    elif cmd == 'exit':
        break
    elif cmd == 'calc':
        chinese_total = 0
        math_total =0
        person = len(stu_list)
        for i in range(0,person):
            chinese_total += stu_list[i][1]
            math_total += stu_list[i][2]
        print(chinese_total/person,math_total/person)
    else:
        print('命令无法识别')