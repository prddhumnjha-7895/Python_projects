hf="history.txt"

def show_history():
    f=open(hf,"r")
    lines  = f.readlines()
    if len(lines) ==0:
        print("no history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    f.close()

def cleat_history():
    file = open(hf,"w")
    file.close()
    print("history cleared")

def save_history(equation,result):
    file1 = open(hf,"a")
    file1.write(equation + "=" + str(result) + "\n")
    file1.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts)!=3:
        print("invalid")
        return
    
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])

    if op == "+":
        result = num1+num2
    elif op == "-":
        result = num1-num2
    elif op == "*":
        result = num1*num2
    elif op == "/":
        if num2 == 0:
            print("cannot ")
            return
        result = num1/num2
    else:
        print("invalid operator")
        return
    if int(result) == result:
        result = int(result)
    print('result:',result)
    save_history(user_input,result)
    
def main():
    print("-----simple calculator (type history,clear or exit)-------")
    while True:
        user_input= input("enter calculation or above commands: ")
        if user_input == "exit":
            print("Good bye")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            cleat_history()
        else:
            calculate(user_input)

main()






