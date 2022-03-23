"""
 * Project name(项目名称)：Python_startswith方法和endswith方法
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:18
 * Version(版本): 1.0
 * Description(描述)： startswith()方法
startswith() 方法用于检索字符串是否以指定字符串开头，如果是返回 True；反之返回 False。
str.startswith(sub[,start[,end]])
str：表示原字符串；
sub：要检索的子串；
start：指定检索开始的起始位置索引，如果不指定，则默认从头开始检索；
end：指定检索的结束位置索引，如果不指定，则默认一直检索在结束。
 """

if __name__ == '__main__':
    str1 = "https://github.com/maomao124/"
    print(str1.startswith("https://"))
    print(str1.startswith("https:"))
    print(str1.startswith("https"))
    print(str1.startswith("http"))

    str1 = "http://github.com/maomao124/"
    print(str1.startswith("https://"))
    print(str1.startswith("https:"))
    print(str1.startswith("https"))
    print(str1.startswith("http"))

    input()
