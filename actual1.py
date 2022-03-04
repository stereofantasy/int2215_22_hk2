import re
def arithmetic_arranger(problems, trigger=False):
    effector1 = []
    operator = []
    effector2 = []

    if len(problems) > 5:#Error: Too many problems.
        return "Error: Too many problems."

    for problem in problems:#adds to the lists
        elements = problem.split()
        if len(elements) == 3:
            effector1.append(elements[0])
            operator.append(elements[1])
            effector2.append(elements[2])
        else:
            problem=(repr(' '.join(segment for segment in re.split(r'([0-9]+\.?[0-9]*)', problem)if segment))).strip("'")
            elements = problem.split()
            effector1.append(elements[0])
            operator.append(elements[1])
            effector2.append(elements[2])

    for opr in range(len(problems)):#Error: Operator must be '+' or '-'.
        if operator[opr] != "+" and operator[opr] != "-": 
            return "Error: Operator must be '+' or '-'."

    for i in range(len(problems)):#Error: Numbers must only contain digits.
        if effector1[i].isdigit()==False:
            return "Error: Numbers must only contain digits."
        elif effector2[i].isdigit()==False:
            return "Error: Numbers must only contain digits."

    for i in range(len(problems)):#Error: Numbers cannot be more than four digits.
        if len(effector1[i]) > 4 or len(effector2[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    line1 = []
    line2 = []
    line3 = []
    line4 = []
    sum=[]
    diff=[]
    su=-1
    di=-1

    for i in range(len(problems)):#just some location stuffs
        if len(effector1[i]) >= len(effector2[i]):
            line1.append(' '*2 + effector1[i])    
        else:
            line1.append(' '*(2 + len(effector2[i]) - len(effector1[i])) + effector1[i])

    for i in range(len(problems)):#just some location stuffs
        if len(effector2[i]) >= len(effector1[i]):
            line2.append(operator[i] + ' ' + effector2[i])
        else:
            line2.append(operator[i] + ' '*(len(effector1[i]) - len(effector2[i]) + 1) + effector2[i])
    
    for i in range(len(problems)):#design '-----' for line3 and calculate, add sums and differents to line 4
        line3.append('-'*max(len(line1[i]),len(line2[i])))
        if operator[i] == '+':
            su=su+1
            sum.append(str(int(effector1[i])+int(effector2[i])))
            line4.append(' '*(max(len(line1[i]),len(line2[i]))-len(sum[su]))+sum[su])
        else:
            di=di+1
            diff.append(str(int(effector1[i])-int(effector2[i])))
            line4.append(' '*(max(len(line1[i]),len(line2[i]))-len(diff[di]))+diff[di])
    
    if trigger:
        arranged_problems= "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3) + "\n" + "    ".join(line4)
    else:
        arranged_problems= "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
    return arranged_problems
