#find who is elder
def find_elder(age1, age2):
    if age1 > age2:
        return "First brother is elder"
    elif age2 > age1:
        return "Second brother is elder"
    else:
        return "Both are of the same age"

# Example
print(find_elder(18, 21))