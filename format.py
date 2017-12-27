#page23
#定义一个字符串赋值给变量x，字符串中间加了个格式化字符10

x = "There are %d types of people." % 10
#定义一个字符串binrary并赋值给binary
binary = "binary"
#定义一个字符串don't并赋值给do_not
do_not = "don't"
#定义一个字符串，并赋值给变量y，字符串中插入了两个变量，binary和do_not
y = "Those who konw %s and those who %s." % (binary, do_not)
#打印变量x的值
print (x)
#打印变量y的值
print (y)
#打印并输出格式化字符串，%r用来debug最好，而其他格式符则是用来向用户显示输出的
print ("I said: %r." % x)
#打印并输出格式化字符串
print ("I also said: '%s'." % y)
#定义变量hilarious并初始化为false
hilarious = False
#定义并初始化变量joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

#打印并输出格式化字符串
print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."
#打印并输出格式化字符串
print (w + e)
