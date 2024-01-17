#x+y = a => y = a - x
#4x+2y = b
# 4x + 2a - 2x = b
# 2x = b - 2a
# x = (b - 2a)/2
# y = a-x
def solve(heads, legs):
    return [int((legs - heads * 2) / 2), int((heads - (legs - heads * 2) / 2))]

def main():
    print(*solve(int(input()), int(input())))

if __name__ == "__main__":
    main()