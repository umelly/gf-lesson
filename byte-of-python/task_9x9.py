# -*- coding:utf-8 -*-

"""
列*行=列行

1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=0
...
"""
for i in range(1,10):#行
    for j in range(1,10):#列
        if i>=j:
            print '%s*%s=%s' % (j,i,i*j),
    print

print "\n\n", "="*80 ,"\n"

print "".join([
            '%s*%s=%s%s' % (
                j, i, i*j, 
                "\n" if i==j else "\t"
            )
            for i in range(1,10)
        for j in range(1,10)
            if i>=j
    ])
