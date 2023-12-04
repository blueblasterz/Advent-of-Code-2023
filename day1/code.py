import re

if __name__ == '__main__':
    with open("input.txt","r") as file:
        lines = file.readlines()
    
#     lines = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".split("\n")

    if False: # part 1
        reg = re.compile("^[^0-9]*([0-9]).*([0-9])[^0-9]*$")
        reg_2 = re.compile("([0-9])")


        s = 0
        for line in lines:
            if not line: continue
            val = reg.findall(line)
            if val:
                val = int(f"{val[0][0]}{val[0][1]}")
            else:
                val = int(reg_2.findall(line)[0] * 2)
            print(val)
            s += val
        print(s)
    else:
        numbers = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        numbers.update({f"{i}": i for i in range(1,10)})
        reg_first_num = re.compile("([0-9]|one|two|three|four|five|six|seven|eight|nine)")
        reg_last_num = re.compile(".*([0-9]|one|two|three|four|five|six|seven|eight|nine)")
        
        sum = 0
        for line in lines:
            first_num = reg_first_num.findall(line)[0]
            last_num = reg_last_num.findall(line)[0]

            first_num = numbers.get(first_num)
            last_num = numbers.get(last_num)
            sum += first_num*10 + last_num
        print(sum)