---
layout: post
title: 求封闭曲线面积多种思路
tags: mathematica

---

数学中多个方向不同的推演往往会在某个具体问题上统一起来。本文将就封闭曲线面积，分别用行列式、向量和复数来探寻。

## 公式
我们首先套用格林公式给出一个很常见的封闭曲线面积公式，即\\(S=\frac{1}{2}\oint_C(xdy-ydx)\\)，后文将用更加多种基础途径推导出等价结果。

首先，由格林公式：
\\[\iint\limits_{D}(\frac{\partial Q}{\partial x} -\frac{\partial P}{\partial y})dxdy=\oint_{L^{+}}(Pdx+Qdy)\\]
我们要求的面积即\\(S=\iint\limits_Ddxdy\\)，故只需要取\\(\frac{\partial Q}{\partial x} -\frac{\partial P}{\partial y}=1\\)即可，最简单的取法便是取
\\[Q=\frac{1}{2}x, P=-\frac{1}{2}y\\]
带入格林公式得
\\[S=\frac{1}{2}\oint_{L^+}xdy-ydx\\]
即常见的面积公式

### 利用行列式进行的推导
此部分是阅读《高观点下的初等数学II：几何》得到的，书中从一维到三维举例并对行列式的几何意义归纳推广，此处我们只考虑二维平面内发生的事情。

平面内任意不共线三点\\(A(x_1,y_1),B(x_2,y_2),C(x_3,y_3)\\)所成的三角形面积为：
\\[
S=\frac{1}{2}
\begin{vmatrix}
x_1 & y_1 & 1\\\
x_2 & y_2 & 1\\\
x_3 & y_3 & 1
\end{vmatrix}
\\]

公式证明可以利用行列式与向量叉乘的关系，正如后文将要进行的那样，此处略去。**注意：**此处面积为有向面积，ABC成逆时针排列时为正，顺时针排列为负，如下图：

![figure 1]({{ site.url }}/images/posts/Area_of_a_closed_loop/Area_of_a_closed_loop_1.jpg)

我们不妨采用一种简便的记号，用有序点组\\((A,B,C)\\)表示上述行列式的值。

在\\(\triangle ABC\\)内任取一点\\(O\\)，则\\(\triangle ABC\\)的面积即可拆分为\\(\triangle OAB,\triangle OBC,\triangle OCA\\)三个部分，上述记号表述即：
\\[(A,B,C)=(O,A,B)+(O,B,C)+(O,C,A)\\]
其中右边三个有序点组依然分别为顺时针，如图：

![figure 2]({{ site.url }}/images/posts/Area_of_a_closed_loop/Area_of_a_closed_loop_2.jpg)

有趣的是，考虑有向面积的特性，即将逆时针的有序点组视为负，则\\(O\\)点在\\(\triangle ABC\\)外部时，上式依然成立，如图：

![figure 3]({{ site.url }}/images/posts/Area_of_a_closed_loop/Area_of_a_closed_loop_3.jpg)

三角形外的部分由于重叠，自动被抵消了。（这反映了图形的面积具有平移不变性，即取值与坐标架无关）

我们更喜欢这种具有普适性的公式（比如不依赖取绝对值，类似的还有平面内点到直线距离公式，如果式中不加绝对值，则可以有其他妙用，这是我在高中时的一个发现，以后有时间会在博客中总结高中时的一些原创思路），因为这样的公式是连续的，可以进行微分等操作而不用分类讨论。

同时利用上式，通过分解成三角形相加，我们可以求出任意四边形\\(ABCD\\)的面积：
\\[(A,B,C,D)=(O,A,B)+(O,B,C)+(O,C,D)+(O,D,A)\\]
以及任意n边形\\(A_1A_2...A_n\\)的面积：
\\[(A_1,A_2,...,A_n)=(O,A_1,A_2)+(O,A_2,A_3)+...+(O,A_{n-1},A_n)\\]

**现在只要知道了n个点的坐标，我们就可以求出由n个点连线所组成的n边形的面积。**

下面我们考虑\\(n\rightarrow\infty\\)的情况：

现已知一光滑封闭曲线\\(C\\)，求其围成的区域的面积。

我们将\\(C\\)视为一个无穷边形，每条边\\(A_nA_{n+1}\\)都无穷短。平面内任取一坐标原点\\(O\\)，则三角形\\(\triangle OA_nA_{n+1}\\)的面积有：（\\(O,A_n,A_{n+1}\\)按顺时针排列）
\\[dS=(O,A_n,A_{n+1})=\frac{1}{2}
\begin{vmatrix}
0    & 0    & 1\\\
x    & y    & 1\\\
x+dx & y+dy & 1
\end{vmatrix}
=\frac{1}{2}(xdy-ydx)\\]
![figure 4]({{ site.url }}/images/posts/Area_of_a_closed_loop/Area_of_a_closed_loop_4.jpg)

于是将这些小三角形求和即得
\\[S=(O,A_n,A_1)+\sum\limits_{i=1}^\infty (O,A_i,A_{i+1})=\frac{1}{2}\oint_Cxdy-ydx\\]

也就是一开始我们希望求解的面积公式。

### 利用向量进行的推导
向量的叉乘大小对应了面积，而叉乘又具有行列式的形式，这也暗示了其内在的联系。其实这部分内容是在完成第三部分（**利用复数进行的推导**）才想到的，但是逻辑上应该将这部分放在前面写，便于叙述。

####首先我们对向量之间的叉乘重新进行定义：
因为本文中讨论的全部是二维平面内的内容，所以无法精准的使用叉乘的意义，我们不妨在本文中**暂时将向量叉乘的结果视为标量**，其大小与原结果的大小相同，若方向延z轴正方向则为正，反之为负。

如此，我们再一次看到了有向面积：对于向量\\(\vec{a}=\vec{OA},\vec{b}=\vec{OB}\\)，\\(\vec{a}\times\vec{b}\\)的结果代表了\\(\triangle OAB\\)的有向面积，同样的，逆时针为正，顺时针为负。也因此有\\(\vec{a}\times\vec{b}=-\vec{b}\times\vec{a}\\)。

那么下面考虑位置向量\\(\vec{r}=\vec{OP}\\)，\\(P\\)为封闭曲线\\(C\\)上动点，从一点出发，逆时针跑遍\\(C\\)上所有的点并回到初始位置。

对于每一次微位移\\(d\vec{r}\\)，由\\(\vec{r},\vec{r}+d\vec{r}\\)所形成的三角形面积即为
\\[dS=\frac{1}{2}\vec{r}\times(\vec{r}+d\vec{r})=\frac{1}{2}(\vec{r}\times\vec{r}+\vec{r}\times d\vec{r})=\frac{1}{2}(0+\vec{r}\times d\vec{r})=\frac{1}{2}\vec{r}\times d\vec{r}\\]
由此可得
\\[S=\frac{1}{2}\oint_C\vec{r}\times d\vec{r}\\]

其实这个式子亦可看成一个长为r，宽为dr的长方形面积的一半

我们先暂时保留这个结果，不继续下去。最后与第三部分给出的形式一起进行变换。

### 利用复数进行的推导
这部分是受《复分析：可视化方法》的启发，不得不说，这的确是一本宝书，网上甚至有评价这是复分析领域最好的书。

首先利用上面对向量叉乘的重新定义，我们得到入如下公式：
\\[\bar{a}b=\vec{a}\cdot\vec{b}+i(\vec{a}\times\vec{b})\\]
其中对于\\(a,b\in C\\)，\\(\bar{a}\\)为\\(a\\)的共轭复数，\\(\vec{a},\vec{b}\\)分别为\\(a,b\\)对应的向量。

上式的证明是很容易的：

设\\(a=|a|e^{i\alpha},b=|b|e^{i\beta},\theta=\beta-\alpha\\)为\\(\vec{a}\\)转到\\(\vec{b}\\)的角度，则
\\[\bar{a}b=|a||b|e^{i(\beta-\alpha)}=|a||b|e^{i\theta}=|a||b|\cos\theta+i|a||b|\sin\theta=\vec{a}\cdot\vec{b}+i(\vec{a}\times\vec{b})\\]
因此
\\[\vec{a}\times\vec{b}=\mathrm{Im}(\bar{a}b)=\frac{\bar{a}b-\bar{b}a}{2i}\\]
于是书中给出了以复数\\(a_1,a_2,...,a_n\\)对应点为顶点的n边形面积公式：
\\[S=\frac{1}{2}\mathrm{Im}(\bar{a_1}a_2+\bar{a_2}a_3+...+\bar{a_{n-1}}a_n+\bar{a_n}a_1)\\]
书中，作者至此便满足地切换到了下一个话题--克莱因与欧式变换。但是受到《高观点》（碰巧又是克莱因）的启发，我继续向下走，看看能得到什么：

首先确定一个书中未提及的运算：\\(\bar{dz}\\)是否等于\\(d\bar{z}\\)？

求共轭并非线性运算，所以不能直接断定二者相等，于是进行下述过程验证：

记\\(z=x+iy\\)，对其全微分得\\(dz=dx+idy\\)，故\\(\bar{dz}=dx-idy\\)，而\\(\bar{z}=x-iy\\)，同样全微分得\\(d\bar{z}=dx-idy\\)。于是很幸运地，\\(\bar{dz}=d\bar{z}\\)成立，这使得我们能够继续操作。

现令\\(z\\)为封闭曲线\\(L\\)上的点对应复数，记为\\(z\in L\\)，则\\(L\\)上两个无限接近的点\\(z\\)和\\(z+dz\\)与原点形成的小三角形的面积为：
\\[dS=\frac{1}{2}\mathrm{Im}(\bar{z}(z+dz))\\]
由于\\(\bar{z}z=|z|^2\\)必定为实数，所以上式继续化为：
\\[dS=\frac{1}{2}\mathrm{Im}(\bar{z}dz)=\frac{1}{2}\frac{\bar{z}dz-zd\bar{z}}{2i}\\]
于是初步得到
\\[S=\oint_L\frac{1}{2}\mathrm{Im}(\bar{z}dz)=\oint_C\frac{\bar{z}dz-zd\bar{z}}{4i}\\]
至此其实已经得到了我们想要的公式，但在带入实例验算时，我发现上述公式还可以形式上继续化简：

求\\(\mathrm{Im}(\bar{z}dz)\\)时总是会顺带求出\\(\mathrm{Re}(\bar{z}dz)\\)，那不妨将\\(\mathrm{Re}(\bar{z}dz)\\)也进行考虑，设\\(z=x+iy\\)，则\\(\bar{z}dz=(x-iy)(dx+idy)=(xdx+ydy)+i(xdy-ydx)\\)

于是惊喜地发现\\(\bar{z}dz\\)的实部不依赖y与x的关系即可化简，\\(xdx+ydy=\frac{d(x^2+y^2)}{2}=\frac{d(|z|^2)}{2}\\)，由于我们进行的是环路积分，所以\\(|z|^2\\)的初值和终值一定相等，故这一项积分一定为0，即：
\\[\oint_L\mathrm{Re}(\bar{z}dz)\equiv0\\]

那么与此前结果合起来即可得
\\[S=\oint_L\frac{\mathrm{Re}(\bar{z}dz)+i\mathrm{Im}(\bar{z}dz)}{2i}=\frac{1}{2i}\oint_L\bar{z}dz\\]
于是得到了一个形式十分简单精致的结果。

此外，观察\\(\bar{z}dz\\)的虚部即可发现，我们其实也已经证明了此式与文章一开始给出的公式是等价的，我们在下一部分讨论这个问题。

### 几种思路的关联

总结上述，我们得到了三个表示闭合回路的公式：

\\((1).S=\frac{1}{2}\oint_Cxdy-ydx\\)

\\((3).S=\frac{1}{2}\oint_C\vec{r}\times d\vec{r}\\)

\\((4).S=\frac{1}{2i}\oint_C\bar{z}dz\\)

在此没有标上2的序号是因为下面将会用另一个公式填充进去，以更好地看出四个公式的关联：

#### 极坐标下的封闭曲线面积公式

现在考虑一极坐标下的封闭曲线\\(C:\\)\\(\rho=\rho(\theta)\\)，\\(C\\)上动点\\(P\\)与原点连线\\(PO\\)，在\\(\theta\\)变成\\(\theta+d\theta\\)的过程中，扫过的小扇形面积为\\(\frac{1}{2}\rho^2d\theta\\)，规定\\(\theta\\)顺时针为正。

则\\(C\\)围成的面积为：
\\[(2).S=\frac{1}{2}\int_0^{2\pi}\rho^2d\theta\\]

#### 由(3).(4)对(1).(2)的推导
（1）与（2）的公式十分常见，但（3）与（4）是我昨天自己写出来的式子，虽然估计早有先人写出。实际上，（3）和（4）每一个独自推导，都既能得到（1）又能得到（2），我更喜欢这种更具普适性的公式。

#### (3)-->(1)&(2)
设x，y方向单位向量为\\(\hat{x},\hat{y}\\)，令\\(\vec{r}=x\hat{x}+y\hat{y}\\)，对\\(\hat{r}\\)全微分得\\(d\vec{r}=dx\hat{x}+dy\hat{y}\\)，于是\\(\vec{r}\times d\vec{r}=xdy-ydx\\)，从而推得（1）式。

记\\(d\vec{r}=\vec{v}\cdot dt=\vec{w}\times\vec{r}\cdot dt\\)，将叉乘结果看成标量，则\\(\vec{r}\times d\vec{r}=wr^2dt=r^2d\theta\\)，从而推得（2）式。

#### (4)-->(1)&(2)
上一版块中，我们已经得到了，设\\(z=x+iy\\)，则\\(\bar{z}dz=(x-iy)(dx+idy)=(xdx+ydy)+i(xdy-ydx)\\)，故只取虚部，便已经推出了（1）式，下面重点来看（2）。

复数有一大特点就是在于既可以用直角坐标表示成\\(x+iy\\)，又可以方便地用极坐标表示\\(\rho e^{i\theta}\\)，这使得两者的灵活选择可以简化很多证明。

于是此处我们取\\(z=\rho e^{i\theta}\\)，对其求全微分，则\\(dz=e^{i\theta}d\rho+\rho ie^{i\theta}d\theta\\)，\\(\bar{z}dz=\rho d\rho+\rho^2id\theta\\)，与此前类似，第一项环路积分一定为0，则
\\[S=\frac{1}{2i}\oint_C\bar{z}dz=\frac{1}{2i}\oint_C\rho d\rho+\rho^2id\theta=\frac{1}{2}\int_0^{2\pi}\rho^2d\theta\\]
完成了对（2）式的推导。

### （4）式的举例应用

求螺旋线\\(\rho=\theta(\theta:0\rightarrow \pi)\\)与横轴形成的封闭曲线的面积。（如图）

![figure 5]({{ site.url }}/images/posts/Area_of_a_closed_loop/Area_of_a_closed_loop_5.jpg)

这个问题用（2）式求解十分容易，但现在我们从（4）式出发。虽然在这个问题中无法得到简化，但是或许在有些问题中（4）式会是一个非常好的处理办法。

我们将\\(C\\)曲线分为\\(C_1,C_2\\)两段，其中\\(C_1:z=\theta e^{i\theta}(\theta:0\rightarrow\pi),C_2:z=\rho(\rho:-\pi\rightarrow0)\\)，则有
\\[S=\frac{1}{2i}\oint_C\bar{z}dz=\frac{1}{2i}(\int_{C_1}+\int_{C_2})(\bar{z}dz)\\]
\\(C_1:\bar{z}=\theta e^{-i\theta},dz=(e^{i\theta}+i\theta e^{i\theta})d\theta\Longrightarrow\\)
\\[\int_{C_1}\bar{z}dz=\int_0^\pi(\theta+i\theta^2)d\theta=\frac{\pi^2}{2}+\frac{i\pi^3}{3}\\]
\\(C_2:\bar{z}=z=\rho,dz=d\rho\Longrightarrow\\)
\\[\int_{C_2}\bar{z}dz=\int_{-\pi}^0\rho d\rho=-\frac{\pi^2}{2}\\]
\\[\Longrightarrow S=\frac{1}{2i}(\frac{\pi^2}{2}+\frac{i\pi^3}{3}-\frac{\pi^2}{2})=\frac{\pi^3}{6}\\]

# EOF
昨天晚上在写《复分析：可视化方法》的课后题，卡在一道看似十分简单的题后，我深感自己对复数的基础运算不够熟练，于是返回去重新细看一遍重点部分，突然发现求四边形面积的过程与《高观点》中的相似，于是便做了类似的推广，最终得到了（4）式，本文便是为了（4）式而写的，后来过程中偶然发现了（3）式。

看这些数学物理书的时候，果然是需要把每一步都仔细想透才行。