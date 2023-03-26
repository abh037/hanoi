
#Algorithm:
#solve n-1 from start to intermediate
#move bottomm layer from start to end
#solve n-1 from intermediate to end

def hanoi(num, start = 'A', intermediate = 'B', end = 'C'):
    if num == 1:
        return [start + ' to ' + end]
    else:
        step1 = hanoi(num - 1, start, end, intermediate)
        step2 = hanoi(1, start, intermediate, end)
        step3 = hanoi(num - 1, intermediate, start, end)
        return step1 + step2 + step3
        
for step in hanoi(int(input("Layers: "))): print(step)
