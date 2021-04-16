chart = [
    [5,0,0,6,7,0,0,8,0],
    [0,9,0,0,0,0,0,0,0],
    [0,0,2,5,0,0,3,0,0],
    [0,0,6,0,0,0,0,0,0],
    [0,0,8,0,0,3,9,2,0],
    [0,0,0,0,2,0,1,0,5],
    [0,0,0,0,5,0,0,0,0],
    [0,0,0,0,9,0,0,4,7],
    [0,3,0,0,0,4,0,0,1]
]

def solve(ch):
    find = find_empty(ch)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(ch, i, (row, col)):
            ch[row][col] = i

            if solve(ch):
                return True

            ch[row][col] = 0

    return False


def valid(ch, num, pos):
    #check row
    for i in range(len(ch[0])):
        if ch[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(ch)):
        if ch[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if ch[i][j] == num and (i,j) != pos:
                return False

    return True



def print_chart(ch):

    for i in range(len(ch)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(ch[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                    print(ch[i][j])
            else:
                    print(str(ch[i][j] )+ " ", end="")

def find_empty(ch):
    for i in range(len(ch)):
        for j in range(len(ch[0])):
            if  ch[i][j] == 0:
                return (i,j)

    return None

print_chart(chart)
solve(chart)
print()
print_chart(chart)
