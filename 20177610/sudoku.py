#!/usr/bin/python
#coding=utf-8

class sodoku(object):
    def __init__(self,board):
        self.b = board

    def check(self,x,y,value):#检查模块
        for row_item in self.b[x]:
            if row_item == value:# 检查行中是否有重复数字
                return False
        for row_all in self.b:
            if row_all[y] == value:# 检查列中是否有重复数字
                return False

            row,col=x/3*3,y/3*3
            row3col3 = self.b[row][col:col + 3] + self.b[row + 1][col:col + 3] + self.b[row + 2][col:col + 3]  # 以下是检查宫格内是否有重复数字
            for row3col3_item in row3col3:
                if row3col3_item == value:
                    return False

        return True

    def get_next(self,x,y):#定位模块
        for next_solu in range(y+1,9):
            if self.b[x][next_solu] == 0:
                return x,next_solu
        for row_n in range(x+1,9):
            for col_n in range(0,9):
                if self.b[row_n][col_n] == 0:
                    return row_n,col_n
        return -1,-1  #若无下一个未填项，返回-1

    def solution(self,x,y):#主模块
        if self.b[x][y] == 0:
            for i in range(1,10):
                if self.check(x,y,i):
                    self.b[x][y]=i
                    next_x,next_y=self.get_next(x,y)
                    if next_x == -1:
                        return True
                    else:
                        end=self.solution(next_x,next_y)
                        if not end:
                            self.b[x][y] = 0    #回朔到上一层继续
                        else:
                            return True

    def start(self):#起始模块

        if self.b[0][0] == 0:
            self.solution(0,0)
        else:
            x,y=self.get_next(0,0)
            self.solution(x,y)
        for i in self.b:
            print i

        return
