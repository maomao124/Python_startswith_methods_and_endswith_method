"""
 * Project name(项目名称)：Python_startswith方法和endswith方法
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:22
 * Version(版本): 1.0
 * Description(描述)： endswith()方法
endswith() 方法用于检索字符串是否以指定字符串结尾，如果是则返回 True；反之则返回 False。
str.endswith(sub[,start[,end]])
str：表示原字符串；
sub：表示要检索的字符串；
start：指定检索开始时的起始位置索引（字符串第一个字符对应的索引值为 0），如果不指定，默认从头开始检索。
end：指定检索的结束位置索引，如果不指定，默认一直检索到结束。
 """

if __name__ == '__main__':
    str1 = "index.jsp"
    print(str1.endswith("jsp"))
    print(str1.endswith(".jsp"))
    print(str1.endswith("html"))
    print(str1.endswith("xml"))
    print(str1.endswith("JSP"))

    input()
