import sys

sys.stdin = open('input1.txt', 'r')
sys.stdout = open('output1.txt', 'w')

while True:
    try:
        C, H, O = input().split()
        C = int(C)
        H = int(H)
        O = int(O)
        print(min(C // 2, H // 6, O // 1))
    except EOFError:
        break
        
