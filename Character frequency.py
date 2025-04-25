s=input().lower()
set_a=set(s)
set_a.discard(" ")
for i in sorted(set_a):
    count=s.count(i)
    print("{}: {}".format(i,count))
