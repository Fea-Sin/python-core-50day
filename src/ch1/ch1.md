
## python 语言元素基础

### python 语言元素之变量

不同类型的变量可以相互转换，这一点可以通过python的内置函数来实现

- `int()`：将一个数值或字符串转换成整数，可以指定进制
- `float()`：将一个字符串转换成浮点数
- `str()`：将指定的对象转换成对应的字符串形式，可以指定编码
- `chr()`：将整数转换成该编码对应的字符串（一个字符）
- `ord()`：将字符串（一个字符）转换成对应的编码（整数）

[实例1](./pya.py)

### python 语言元素之运算符

| 运算        | 描述       |
| ---------- | --------- |
| `[]` `[:]` | 下标，切片  |
| `**`  | 指数 |
| `~` `+` `-` | 按位取反 正负号 |
| `*` `/` `%` `//` | 乘 除 模 整除 |
| `+` `-` | 加减 |
| `>>` `<<` | 右移 左移 |
| `&` | 按位与 |
| `^` `|` | 按位异或 按位或 |
| `<=` `<` `>` `>=` | 小于等于 小于 大于 大于等于 |
| `==` `!=` | 等于 不等于 |
| `is` `is not` | 身份运算符 |
| `in` `not in` | 成员运算符 |
|`not` `or` `and` | 逻辑运算符 |
| `=` `+=` `-=` `*=` `/=` `%=` `//=` `**=`  | 赋值运算符 |

> 上面这个表格实际上是按照运算符的优先级从上到下列出了各种运算符。

[实例2](./pyb.py)

### 分支结构

在python中要构造分支结构可以使用`if`、`elif`、`else`关键字，不同于C++、Java等编程
语言python中没有用花括号来构造代码快，而是使用了缩进的方式来表示代码层次结构，如果`if`
条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了。

如果要构造出更多的分支，可以使用`if...elif...else`结构或者嵌套`if...else...`结构
在python之禅中有这么一句**Flat is better than nested**，使用扁平化结构就不要使用  
嵌套结构，扁平化使代码更具可读性。

[实例3](./pyc.py)

### 循环结构

循环结构是程序控制某条或某些指令重复执行的结构，在python中构造循环结构有两种做法，一是
`for-in`循环，如果明确知道循环执行的次数，我们推荐使用`for-in`循环，二是`while`循环
如果不知道具体循环次数，我们推荐使用`while`循环

[实例4](./pyd.py)

[实例5](./pye.py)

### 分支循环的应用

[寻找水仙花](./pyg.py)

[正整数反转](./pyh.py)

[百钱百鸡问题](./pyi.py)

[花旗骰](./pyj.py)




