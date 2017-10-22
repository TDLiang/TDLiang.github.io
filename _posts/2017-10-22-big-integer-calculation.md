---
layout: post
title: 大数计算——高精度算法
tags: Algorithms

---
## 为何学习算法
此前因个人兴趣了解过不少算法，但从未系统学习过，也没自己写过，现在终于有机会每天抽出一部分时间来钻研算法。其实只是开发应用软件而言，基本不需要对算法了解很深，各大开发框架早就提供了各种库，再复杂的算法也只需要懂得如何调用函数就行。但是探求本源永远不需要多么直接的理由，研究东西就要往下钻。

目前我的算法学习主要有三个方向：
- 信息学竞赛算法、《算法导论》
- 《深入理解计算机系统》
- 初步了解机械学习算法

第一部分更偏重于数学，是各类算法的原理及代码实现（主要用C++）;第二部分是类Unix系统下的计算机基础原理的介绍，此书被称为计算机界的“龙书”（主要用C）;第三部分是未来的方向，先做初步了解（主要用Python）。

---

下面从最基础的算法开始写起：

## 为何需要高精度算法
C及C++中的常用整数数据类型为int，一个int类型的变量的取值范围是有限的，一旦运算超过了其范围，就会发生溢出（Overflow），会引起程序错误，很多系统漏洞都源于Overflow。下面列出常见整型变量的字节数（以64位机器为例）：

| 变量类型        | 字节长 | min                        | max                       |
| :------------ | :---: | -------------------------: | ------------------------: |
| int           | 4     | -2 147 483 648             | 2 147 483 647             |
| unsigned int  | 4     | 0                          | 4 294 967 295             |
| short int     | 2     | -32 768                    | 32 767                    |
| long int      | 8     | -9 223 372 036 854 775 808 | 9 223 372 036 854 775 807 |
| char          | 1     | -128                       | 127                       |

占一个字节（比如char）的变量的取值范围区间长度为$$2^8$$（因为一个字节包含8个二进制位），无符号时，区间长度不变，最小值为0即可。

由此可见，整型变量是有最大值的，一旦超出范围就会发生溢出，具体的溢出方式会在《深入理解计算机系统》部分写到。一个int变量的最大取值为10位数，那么若我们要对几百位的大数进行操作时，就无法使用现有的数据类型了，这是就需要用到被称为“高精度”的算法。

## 基本思路
高进度算法简单来说就是用数组来储存每一位的数值。

我们先来分析一下一个数的组成： 一个数就是各位数值×权值再求和。写成公式即：
$$x = (a_na_{n-1}...a_1a_0)_{(k)} = \sum_{i=0}^na_ik^i$$，表示k进制下的整数x，$$a_i$$为从右往左第i + 1位的数值，而$$k^i$$代表了k进制下第i + 1位的权值。

$$(1234)_{(10)} = 4×10^0+3×10^1+2×10^2+1×10^3$$

$$(1010011010)_{(2)} = 0 × 2^0+1×2^1+0×2^2+1×2^3+1×2^4+0×2^5+0×2^6+1×2^7+0×2^8+1×2^9 = (666)_{(10)} = 6×10^0+6×10^1+6×10^2$$

于是上式的$$a_i$$便形成了一个数组，编写一个算法使得这些数组之间能够加减乘除便是高精度算法的基础任务。

---
##### 那么该选择多少进制来表示呢？

有很多参考资料上高精度算法用的是一个int数组表示10进制的数字，然后让数组长度很长即可。但我觉得这样的算法实属鸡肋，unsigned int的取值范围能达到4 294 967 295，在数组里却只用到了0 ~ 9十种可能，实在浪费了太多资源。

为了不浪费资源，有两种思路可取：
- 用二进制配合bool类型变量，这样丝毫不会浪费资源，因为每一位只有0与1两种可能
- 采用一种很大的进制，如下面采用$$10^8$$进制，尽可能利用int的范围，减少浪费。

第一种方法虽然丝毫不浪费，但是一个在10进制下已经很长的数字，二进制下的长度更是不可想象，这种方法不利于编写也不利于实际操作。

第二种方法会浪费小部分可能性，但是十分利于编写。而且下面会看到采用$$10^n$$形式的进制有很大好处。

---
##### 数字分段处理
数字分段处理这个名词是我自己创的，但应该十分贴切。

首先回想二进制、十六进制之间的快速转换技巧，如：

$$(1010011010)_{(2)}\to((0010)(1001)(1010))_{(16)}$$

其实上式右边已经是十六进制表示了，只不过为了方便记号，让一个数位只写一个记号，用0～F分别对应了0000到1111，于是用标准记号写成0x29A。

之所以可以如此操作，是因为$$16=2^4$$，当权值之间有次方关系时，可以直接将原来的数字分段，而看起来不改变数值的大小。

那么采用$$10^8$$进制时，只要将十进制数从右往左每八个数打包成一个数，就自动写成了$$10^8$$进制数，但我们没有必要找$$10^8$$个记号去一一代表它们，所以我们就保持用八个数字表示一个数位的形式。

此外，用十进制的高精度，完成8个数位的加法需要进行8次int变量间的操作，而$$10^8$$进制下只需要一次。十进制每一个数位都要考虑逢十进一，而现在只要逢$$10^8$$进一即可。

## 代码
此处暂时给出加法运算的实现，其他三种等日后研究透彻再增加增加分析实现的模块。

首先构建一个结构体bigInt，我更喜欢在struct构建数据类型，class构建更实际的类。
``` c++
//代码参考：《算法竞赛入门经典》
#include <iostream>
#include <vector>
using namespace std;

class bigInt {
public:
	static const int WIDTH = 8; //将大数分段，int最大为十位，两个八位相加最多为九位数，不会出现问题
	static const int BASE = 100000000; //通过 num % BASE 来获取后八位数，通过 num /= BASE来去除最后的0
	vector<int> integer;

	bigInt(long long num = 0) {
		*this = num;
	}

	bigInt operator = (long long num) {
		integer.clear();
		do {
			integer.push_back(num % BASE);
			num /= BASE;
		} while(num > 0);
		return *this;
	}

	bigInt operator = (const string& str) {//代码参考：《算法竞赛入门经典》
#include <iostream>
#include <vector>
using namespace std;

class bigInt {
public:
	static const int WIDTH = 8; //将大数分段，int最大为十位，两个八位相加最多为九位数，不会出现问题
	static const int BASE = 100000000; //通过 num % BASE 来获取后八位数，通过 num /= BASE来去除最后的0
	vector<int> integer;

	bigInt(long long num = 0) {
		*this = num;
	}

	bigInt operator = (long long num) {
		integer.clear();
		do {
			integer.push_back(num % BASE);
			num /= BASE;
		} while(num > 0);
		return *this;
	}

	bigInt operator = (const string& str) {
		integer.clear();
		int x, len = (str.length() - 1) / WIDTH + 1; //len为分片后的段数，若直接length() / 8 + 1，如果有length() = 8n，len值会为n + 1，为防止此情况，先减去1
		for (int i = 0; i < len; i++) {
			int end = str.length() - i * WIDTH;
			int start = max(0, end - WIDTH);
			sscanf(str.substr(start, end - start).c_str(), "%d", &x);
			integer.push_back(x);
		}
		return *this;
	}

	bigInt operator + (const bigInt& b) const {
		bigInt c; //返回c = *this + b作为结果
		c.integer.clear();
		for (int i = 0, j = 0;; i++) {
			if (j == 0 && i >= integer.size() && i >= b.integer.size()) break;
			int x = j;
			if (i < integer.size()) x += integer[i];
			if (i < b.integer.size()) x += b.integer[i];
			c.integer.push_back(x % BASE);
			j = x / BASE;
		}
		return c;
	}
};

ostream& operator << (ostream &out, const bigInt& x) {
		out << x.integer.back();
		for (int i = x.integer.size() - 2; i >= 0; i--) {
			char buf[20];
			sprintf(buf, "%08d", x.integer[i]);
			for (int j = 0; j < strlen(buf); j++) out << buf[j];
		}
	    return out;
	}

int main() {
	bigInt a, b;
	a = "121231231232142314123412341234923999999242342194";
	b = "11111111242343534525423553432545111";
	cout<<a + b;
}
```

	Output: 121231231232153425234654684769449423552674887305

# EOF
暂时先写到这里，后面还会有对高精度算法的减法、乘法和除法（难度依次递增）的学习记录。今天第二次学习小组会上探讨了FFT(Fast Fourier Transformation)的基础概念，FFT可用于高精度乘法中来降低时间复杂度，越来越觉得自己要学的东西还很多啊～