import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        month = int(input())
        if month in (1, 2, 12):
            print("Winter")
        
        if month in (3, 4, 5):
            print("Spring")
        
        if month in (6, 7, 8):
            print("Summer")
        
        if month in (9, 10, 11):
            print("Autumn")
        
        if month > 12:
            print("Error")

        if month < 1:
            print("Error")
    except EOFError:
        break