# testing file for inputter classes
from inputter import *
# from inputter-func import *
# masterpiece = Piece()
# print(masterpiece)
# print(masterpiece.get_measure(1))

# some testing for the new get_input method of the Piece class
def user_input():
    print('Hello welcome my dude! You are composing music now.')
    new_piece = Piece(int(input('how many measures would you like?')), \
                    int(input('And how many beats?')))
    print("Great! Now let's start composing")
    count_measure = 1
    new_piece.get_input()
    return new_piece

user_piece = user_input()
print (user_piece)
