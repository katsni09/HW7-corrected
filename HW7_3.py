def sum(beginning, end):
    if beginning > end:
        return 0
    else:
        return beginning + sum(beginning + 1, end)


beginning = int(input("От: "))
end = int(input("До: "))

result = sum(beginning, end)
print(f"{result}")
