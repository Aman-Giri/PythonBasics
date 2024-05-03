it = 10

while it > 1:
    if it == 9:
        it = it-1
        continue # Continue will stop the current Iteration in program and starts from next Iteration from start
    if it == 3:
        break
    print(it)
    it = it-1

print("While Loop Execution is done")