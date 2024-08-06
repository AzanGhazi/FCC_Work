def arithmetic_arranger(problems, show_answers=False):
    final_string = ""
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    top_nums = []
    sec_nums = []
    opperators = []
    spaces = []
    divider = "      "
    dividers = "    "
    print(len(problems))
    if len(problems) > 5:
        #print(problems)
        return 'Error: Too many problems.'



    for problem in problems:
        str_arr = problem.split(" ")
        #print(str_arr[1] == "+")
        if str_arr[1] == "+" or str_arr[1] == "-":
            top_nums.append(str_arr[0])
            sec_nums.append(str_arr[2])
            opperators.append(str_arr[1])
            if not (str_arr[0].isdigit() and str_arr[2].isdigit()):
                return "Error: Numbers must only contain digits."
            space = max(len(str_arr[0]), len(str_arr[2]))
            print(space)
            if space > 4:
                return "Error: Numbers cannot be more than four digits."
            spaces.append(2+space)
            print(spaces)
        else:
            return "Error: Operator must be '+' or '-'."
    #Construct First Line
    for i in range(len(top_nums)):
        first_line +=" "*(spaces[i] - len(top_nums[i]))
        if (i+1 == len(top_nums)):
            first_line += top_nums[i] 
        else: 
            first_line += top_nums[i] + dividers;
    #Construct Second Line
    for i in range(len(sec_nums)):
        second_line += opperators[i]
        second_line +=" "*(spaces[i] - len(sec_nums[i])-1)
        if (i+1 == len(sec_nums)):
            second_line += sec_nums[i] 
        else: 
            second_line += sec_nums[i] + dividers;
        #Construct Dashes Line
    
    for i in range(len(sec_nums)):
        third_line +="-"*(spaces[i])
        if (i+1 < len(sec_nums)):
            third_line += dividers;
    final_string = first_line + '\n' + second_line +'\n' + third_line;
    #print(final_string)
    if show_answers:
        #Construct solutions. 
        solutions = []
        for i in range(len(sec_nums)):
            a = int(top_nums[i])
            b = int(sec_nums[i])
            if (opperators[i] == "+"):
                solutions.append(str(a + b))
            else:
                solutions.append(str(a - b))
        #Create forth Line using solutions
        for i in range(len(top_nums)):
            fourth_line +=" "*(spaces[i] - len(solutions[i]))
            if (i+1 == len(top_nums)):
                fourth_line += solutions[i] 
            else: 
                fourth_line += solutions[i] + dividers;
        final_string += '\n'+fourth_line
    return final_string


print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')


