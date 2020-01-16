"""
    数据模型
"""

#       元组               位置
# 元组[0]  元组[1]    位置.r   位置.c

class Location:
    """
        位置
    """

    def __init__(self, r=0, c=0):
        self.r = r
        self.c = c
