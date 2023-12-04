
if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
    
#     lines = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".split("\n")

    matrix = [ list(line.strip()) for line in lines ]
    # print(matrix)

    w,h = len(matrix[0]), len(matrix)

    accu = ""
    star_coord = None
    is_a_part=False
    parts_per_star = {} # keys : coordinate of the *. value : list of engine values
    for y in range(h):
        for x in range(w):
            c = matrix[y][x]
            if c not in "0123456789":
                if accu and is_a_part:
                    parts_per_star[star_coord] = parts_per_star.get(star_coord,[]) + [int(accu)]
                accu = ""
                is_a_part = False
            else:
                accu += c
                # check if part with star
                if not is_a_part:
                    for (dx,dy) in [(-1,-1), (0,-1), (1,-1),
                                    (-1,0),          (1,0),
                                    (-1,1),  (0,1),  (1,1)]:
                        if x+dx >= 0 and x+dx < w and y+dy >= 0 and y+dy < h:
                            if matrix[y+dy][x+dx] == "*":
                                is_a_part = True
                                star_coord = (x+dx, y+dy)
                                break
        if accu and is_a_part:
            parts_per_star[star_coord] = parts_per_star.get(star_coord,[]) + [int(accu)]
        accu = ""
        is_a_part = False
    if accu and is_a_part:
        parts_per_star[star_coord] = parts_per_star.get(star_coord,[]) + [int(accu)]

    # print(parts_per_star)

    sum = 0
    for _, v in parts_per_star.items():
        if len(v) == 2:
            sum += v[0]*v[1]
    
    print(sum)
                