#for number in range(1,21):
#    print(number)

#evennumbers = list(range(1,1000001))
#for numbers in evennumbers:
#    print(numbers)
#print(min(evennumbers))
#print(max(evennumbers))
#print(sum(evennumbers))

#jishu = list(range(1,21,2))
#for ji in jishu:
#    print(ji)

#there = list(range(3,31,3))
#for th in there:
#    print(th)

#lifang = []
#for value in range(1,11):
#    lifang.append(value**3)
#print(lifang)

lifang = [value**3 for value in range(1,11)]
print(lifang)
