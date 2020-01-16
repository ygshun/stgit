"""
    游戏2048核心算法
    1. 叙述出程序执行流程
        向左移动 --> 获取二维列表每行数据 --> 零元素后移 --> 进行合并处理
        向右移动 --> 反向切片 --> 执行向左移动逻辑--> 还原数据
        上下移动 --> 方阵转置 --> 执行向左向右移动逻辑--> 方阵再次转置
    2. 叙述出优势
        结构清晰 --> 函数与函数高内聚 --> 复用性强 --> 维护性强
        降维思想 --> 将二维问题转换为一维问题
"""
# list_merge = [4, 4, 4, 4]
list_merge = None

map = [
    [2, 0, 0, 2],
    [2, 4, 0, 4],
    [0, 4, 2, 0],
    [4, 0, 4, 2],
]


# 1. 定义函数，将零元素移动到末尾
# [2,0,0,2] --> [2,2,0,0]
# [0,2,0,2] --> [2,2,0,0]
# [0,0,0,2] --> [2,0,0,0]
def zero_to_end():
    # 思路：从后往前判断,如果是零元素则删除,再追加零元素.
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 测试：
# zero_to_end()
# print(list_merge)

# 2. 定义函数，将相同元素合并
# [4,4,2,2] --> [8,4,0,0]
# [2,0,0,2] --> [2,2,0,0] -->  [4,0,0,0]
# [2,2,2,2] --> [4,4,0,0]
# [0,0,0,2] --> [2,0,0,0]
def merge():
    # 思想：将相邻且相同元素进行合并
    zero_to_end()  # [2,0,0,2] --> [2,2,0,0]
    for i in range(len(list_merge) - 1):  # [4,0,0,0]
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# merge()
# print(list_merge)

# 定义函数,将二维列表所有元素向左移动
# 思想：获取每行,赋值给list_merge,通过merge函数进行合并.
def move_left():
    global list_merge
    for line in map:
        list_merge = line
        merge()


# move_left()
# print(map)

# 定义函数,将二维列表所有元素向右移动
# 思想：获取每行反转后，赋值给list_merge,
#      通过merge函数进行合并.
#      list_merge还给map
def move_right():
    global list_merge
    for line in map:
        # 反向切片会创建新列表
        list_merge = line[::-1]
        # 操作的是新列表
        merge()
        # list_merge还给map
        line[::-1] = list_merge


# move_right()
# print(map)

# 定义函数,将二维列表所有元素向上移动
# 思想： 矩阵转置
#       调用向左移动
#       矩阵转置
def move_up():
    square_matrix_transposition()
    move_left()
    square_matrix_transposition()


# 定义函数,将二维列表所有元素向下移动
# 思想： 矩阵转置
#       调用向右移动
#       矩阵转置
def move_down():
    square_matrix_transposition()
    move_right()
    square_matrix_transposition()


def square_matrix_transposition():
    """
    # map[1][0]   map[0][1]
    # map[2][0]   map[0][2]
    # map[3][0]   map[0][3]
    for r in range(1,4):
        # map[r][0]   map[0][r]
        pass
    # map[2][1]  map[1][2]
    # map[3][1]  map[1][3]
    for r in range(2,4):
        # map[r][1]  map[1][r]
        pass

    # map[3][2]  map[2][3]
    for r in range(3,4):
        # map[r][2]  map[2][r]
        pass

    # for c in range(1,4):
    #     for r in range(c, 4):
    #         # map[r][c-1]  map[c-1][r]
    #         pass
    """
    for c in range(1, len(map)):
        for r in range(c, len(map)):
            map[r][c - 1], map[c - 1][r] = map[c - 1][r], map[r][c - 1]


move_up()
print(map)
