for primo in range(2, 101):
    for div in range(2, primo):
        if primo % div == 0:
            break
    else:
        print(primo)