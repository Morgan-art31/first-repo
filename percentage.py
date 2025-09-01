def percentage(x, y):
    result = (x / y ) * 1000
    return result

mark = int(input("Mark: "))
total = int(input("Out of: "))

out_come = percentage(mark, total)
print(f"You got {out_come} percent.")
