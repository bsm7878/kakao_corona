def diff_calc(today, yesterday):
    if today > yesterday:
        return '+' + str(today-yesterday)
    elif today < yesterday:
        return '-' + str(yesterday - today)
    else:
        return '-'



if __name__ == "__main__":
    print(diff_calc(0,0))
