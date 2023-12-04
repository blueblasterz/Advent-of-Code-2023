import re



if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
    
    # reg_id = 

    # 12 red, 13 green, 14 blue
    values = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    sum_id = 0
    for line in lines:
        min_val = {
            "red"  : 0,
            "green": 0,
            "blue" : 0
        }
        tmp = line.strip().split(": ")
        # print(tmp, tmp[0][5:])
        id = int(tmp[0][5:])
        infos = tmp[1].split("; ")
        game_ok = True
        for info in infos:
            # print(info)
            for verif in info.split(", "):
                num, col = verif.strip().split(" ")
                # print("  ", num, col, int(num) > values[col])
                # if int(num) > values[col]:
                #     game_ok = False
                #     break
                min_val[col] = max(min_val[col], int(num))
        #     if not game_ok:
        #         break
        # if game_ok:
        #     sum_id += id
        #     print(f"game {id} ok")
        # else:
        #     print(f"game {id} not ok")
        sum_id += min_val["red"]*min_val["green"]*min_val["blue"]
    print(sum_id)