mush = []
for i in range(10):
    mush.append(int(input()))

ans = 0
i = 0 
for i in range(10):
    ans += mush[i]
    if ans > 100:
        break

if i == 9:
    print(ans)

else:
    pre = -(ans - mush[i] - 100)
    next_ = ans - 100

    if pre >= next_:
        print(ans)
    else:
        print(ans - mush[i])