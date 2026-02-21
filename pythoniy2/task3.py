import math

x1, y1, r1= map(int, input().split())
x2, y2, r2 = map(int, input().split())
dx = x1 - x2
dy = y1 - y2
dist_sq = dx*dx + dy*dy
sum_r = r1 + r2
diff_r = abs(r1 - r2)

if diff_r * diff_r <= dist_sq <= sum_r * sum_r:
    print("YES")
else:
    print("NO")
