#!/bin/sh

class Board:

    def __init__(self, 
                board_size=None):

        self.board = []
        self.board_size = board_size
        for row in range(self.board_size):
            current_row = []
            for col in range(self.board_size):
                current_row.append(' ')
            self.board.append(current_row)

    def print_lines(self):

        for i in range(6):
            print '-',
        print "\n"
        return

    def print_board(self):

        for row in range(self.board_size):
            for col in range(self.board_size):
                print self.board[row][col], '|',
            print "\n"
            self.print_lines()

    def check(self):
    
        for row in range(self.board_size):
            count = 0
            first = self.board[row][0]
            for col in range(self.board_size):
                if self.board[row][col] != ' ' and self.board[row][col]  == first:
                    count += 1
            if count == self.board_size:
                return True

        for col in range(self.board_size):
            count = 0
            first = self.board[0][col]
            for row in range(self.board_size):
                if self.board[row][col] != ' ' and self.board[row][col] == first:
                    count += 1
            if count == self.board_size:
                return True

        first = self.board[0][0]
        count = 0
        for cell in range(self.board_size):
            if self.board[cell][cell] != ' ' and self.board[cell][cell] == first:
                count += 1
        if count == self.board_size:
            return True
        return False

    def set_cell(self, row, column, char):
        print char
        self.board[row][column] = char
        self.print_board()

if __name__ == "__main__":
    size = input()
    b = Board(size)
    b.print_board()
    flag = False
    while flag != True:
        row = input()
        column = input()
        c = raw_input()
        b.set_cell(int(row), int(column), c)
        flag = b.check()
        print flag
