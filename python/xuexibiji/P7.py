#二进制与字符编码

#UTF-8规定 中文用3个字节表示，英文用1个字节表示
#unicode规定无论是中文还是英文全部都使用2个字节表示
#unicode是一张表规定了那一个字符去使用那一个数字去表示

print(chr(0b100111001011000))#二进制要加上0b
print(chr(20056))
print(ord('乘'))
#一个字符会对应一个整数，这个整数可以使用十六进制，十进制，八进制，二进制，最终计算机都会转为二进制