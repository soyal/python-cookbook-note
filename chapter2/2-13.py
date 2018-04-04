# 字符串对齐
text = 'hello world'
ltext = text.ljust(20)
print('ltext: {}, len: {}'.format(ltext, len(ltext)))
ctext = text.center(20)
print('ctext: {}'.format(ctext))
rtext = text.rjust(20)
print('rtext: {}'.format(rtext))

# 也可以使用format
ftext1 = format(text, '>20')
print(ftext1, 'len: ', len(ftext1))
ftext2 = format(text, '<20')
print(ftext2)
ftext3 = format(text, '^20')
print(ftext3)

# 指定非空格填充
print(format(text, '=>20'))
print(format(text, '*^20'))
print(format(text, '=<20'))

print('{:>10s}-{:<10}'.format('hello', 'world'))