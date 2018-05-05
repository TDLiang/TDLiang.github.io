---
layout: post
tags: physics
title: 定义法解微分方程与Time-ordering算符
---

在处理哈密顿量含时的时间演化算符时，往往会引入Time-ordering算符\\(\hat{T}\\)：
\\[\hat{U}(t_b,t_a)=\hat{T}\exp(-\frac{i}{\bar{h}}\int_{t_a}^{t_b}\hat{H}(t)dt)\\]
然而大多书上只是给出这个式子，却没有具体解释，以致于让人以为这一步骤是十分显然的。但是我对此步骤却一直十分不解，\\(\hat{T}\\)究竟如何作用？积分本来就是对\\(t\\)从小到大积分，又为何要重新排列？


今天终于在《Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets》中看到了比较详细的推导，但依然不够直观。故在此用我自己的想法重新解释。


### 从定义法解微分方程开始


考虑一个十分基础的微分方程\\(\frac{dy}{dx}=P(x)y\\)，可以用分离变量口算出来。但是如果希望用微分和积分的定义来解这个微分方程，就需要一些转化步骤。这些转化步骤，正是理解Time-ordering算符的关键。


设方程的解为\\(y=y(x)\\)，有初值条件\\(y(x_a)=y_a\\)，我们希望求出任意\\(x=x_b\\)时的\\(y=y(x_b)=y_b\\)。


首先将区间\\((x_a,x_b)\\)分成\\(N\\)个等长小区间：\\((x_a,x_1],(x_1,x_2],...,(x_{N-2},x_{N-1}],(x_{N-1},x_b),x_N=x_b\\)，记\\(\Delta x=x_{i+1}-x_i=\frac{x_b-x_a}{\Delta x}\\)，则\\(x_n=x_a+n\Delta x\\)。根据定义，\\(N\rightarrow\infty\\)时，\\(x_n\\)处的导数为
\\[y’(x_n)=\frac{y_{n+1}-y_n}{\Delta x}\\]
带入方程得，
\\[\frac{y_{n+1}-y_n}{\Delta x}=P(x_n)y_n\\]
于是有，
\\[y_{n+1}=(1+P(x_n)\Delta x)y_n=(1+P(x_n)\frac{x_b-x_a}{N})y_n\\]
递推得，
\\[y_b=(1+P(x_N)\Delta x)(1+P(x_{N-1})\Delta x)\cdots(1+P(x_1)\Delta x)(1+P(x_a)\Delta x)y_a \tag{1}\\]
如果\\(P(x)=C\\)为常函数，那么显然
\\[y_b=\lim_{N\rightarrow\infty}(1+C\frac{x_b-x_a}{N})^Ny_a=e^{C(x_b-x_a)}y_a\\]
故解为
\\[y(x)=e^{C(x-x_a)}y_a\\]


可是\\(P(x)\\)不为常函数时，我们只有\\((1)\\)式，这时候指数形式就不那么显然了。\\(N\rightarrow\infty\\)时，\\((1)\\)式将有无穷项相乘，我们尝试将\\((1)\\)式按\\(\Delta x\\)升幂展开，观察形式。（注意展开的过程并没有用到乘法交换率，所以此展开可用于non-abelian情况）


\\[
\begin{eqnarray}
\nonumber y_b=\\\{1&+&[P(x_N)\Delta x+P(x_{N-1})\Delta x+\cdots+P(x_a)\Delta x]\\\
\nonumber &+&[P(x_N)\Delta x(P(x_{N-1})\Delta x+\cdots+P(x_a)\Delta x)\\\
\nonumber &+&P(x_{N-1})\Delta x(P(x_{N-2})\Delta x+\cdots+P(x_a)\Delta x)\\\
\nonumber &+&\cdots\\\
\nonumber &+&P(x_1)\Delta x P(x_a)\Delta x]\\\
\nonumber &+&\cdots\\\}y_a
\end{eqnarray}
\tag{2}
\\]


\\((2)\\)式只展开到了\\(\Delta x\\)的二阶项，我们先对此观察。容易发现一阶项就是对\\(P(x)\\)从\\(x_a\\)到\\(x_b\\)的积分；而二阶项每一项后面的括号里，都是对\\(P(x)\\)从\\(x_a\\)到某\\(x_n\\)的积分。


于是可以将\\((2)\\)式改写为
\\[
\begin{eqnarray}
\nonumber \frac{y_b}{y_a}=1&+&[\int_{x_a}^{x_b}P(x)dx]\\\
\nonumber &+&[P(x_N)\Delta x\int_{x_a}^{x_N}P(x)dx\\\
\nonumber &+&P(x_{N-1})\Delta x\int_{x_a}^{x_{N-1}}P(x)dx\\\
\nonumber &+&\cdots\\\
\nonumber &+&P(x_1)\Delta x\int_{x_a}^{x_1}P(x)dx]\\\
\nonumber &+&\cdots
\end{eqnarray}
\\]


二阶项依然不易观察。但若令\\(Q(x)=P(x)\int_{x_a}^xP(x’)dx’\\)，二阶项即可改写为
\\[
\begin{eqnarray}
\nonumber &&Q(x_N)\Delta x+Q(x_{N-1})\Delta x+\cdots+Q(x_1)\Delta x\\\
\nonumber &=&\int_{x_a}^{x_b}Q(x)dx\\\
\nonumber &=&\int_{x_a}^{x_b}P(x)\int_{x_a}^xP(x’)dx’dx\\\
\nonumber &=&\int_{x_a}^{x_b}\int_{x_a}^x P(x)P(x’)dx’dx
\end{eqnarray}
\\]


注意这里\\(x,x’\\)都只是形式参数，最后定积分结果只是个数，所以正如\\(\int_a^bf(x)dx=\int_a^bf(t)dt\\)，我们可以把所有的\\(x\\)一起换成其他任意我们喜欢的字母。因此我们也可以把所有的\\(x\\)换成\\(x’\\)，\\(x’\\)换成\\(x\\)，而并不影响结果。于是有
\\[\int_{x_a}^{x_b}\int_{x_a}^x P(x)P(x’)dx’dx=\int_{x_a}^{x_b}\int_{x_a}^{x’} P(x’)P(x)dxdx’\\]
对等式右边调换积分顺序，于是有
\\[\int_{x_a}^{x_b}\int_{x_a}^{x’} P(x’)P(x)dxdx’=\int_{x_a}^{x_b}\int_x^{x_b}P(x’)P(x)dx’dx\\]


因为这里\\(P(x)\\)和\\(P(x’)\\)都是数字，所以显然
\\[P(x’)P(x)=P(x)P(x’) \tag{3}\\]
但是算符并不一定有交换律，导致了Time-ordering算符的出现。


于是有
\\[
\begin{eqnarray}
\nonumber &&\int_{x_a}^{x_b}\int_{x_a}^x P(x)P(x’)dx’dx+\int_{x_a}^{x_b}\int_x^{x_b}P(x’)P(x)dx’dx\\\
\nonumber &=&\int_{x_a}^{x_b}\int_{x_a}^{x_b} P(x)P(x’)dx’dx\\\
\nonumber &=&\int_{x_a}^{x_b}P(x)dx\int_{x_a}^{x_b}P(x’)dx’\\\
\nonumber &=&(\int_{x_a}^{x_b}P(x)dx)^2
\end{eqnarray}\\\
\int_{x_a}^{x_b}\int_{x_a}^x P(x)P(x’)dx’dx=\int_{x_a}^{x_b}\int_x^{x_b}P(x’)P(x)dx’dx=\frac{1}{2}(\int_{x_a}^{x_b}P(x)dx)^2\\\
\\]


所以最后\\((2)\\)式中的二阶项可以被改写为
\\[\frac{1}{2}(\int_{x_a}^{x_b}P(x)dx)^2\\]


用类似的原理可以得到三阶项为
\\[\frac{1}{3!}(\int_{x_a}^{x_b}P(x)dx)^3\\]


于是归纳出
\\[
\begin{eqnarray}
\nonumber y_b&=&[1+\int_{x_a}^{x_b}P(x)dx+\frac{1}{2}(\int_{x_a}^{x_b}P(x)dx)^2+...]y_a\\\
\nonumber &=&\exp(\int_{x_a}^{x_b}P(x)dx)y_a
\end{eqnarray}
\\]


即原方程解为
\\[y(x)=\exp(\int_{x_a}^x P(x’)dx’)y_a\\]


### Neumann-Liouville 展开与Time-Ordering算符


现在考虑Schrödinger Equation，和此前考虑的微分方程形式非常相似：
\\[i\hbar\frac{\partial}{\partial t}\rvert\psi(t)\rangle=\hat{H}(t)\rvert\psi(t)\rangle\\]
于是我们希望用与此前类似的方式来求时间演化算符\\(\hat{U}(t_b,t_a):\rvert\psi(t_b)\rangle=\hat{U}(t_b,t_a)\rvert\psi(t_a)\rangle\\)。


用同样方法将区间\\((t_a,t_b)\\)分割成等长的\\(N\\)，于是
\\[\hat{U}(t_b,t_a)=(1+\hat{H}(t_N)\Delta t)(1+\hat{H}(t_{N-1})\Delta t)\cdots(1+\hat{H}(t_1)\Delta t)(1+\hat{H}(t_a)\Delta t)\\]


按\\(\Delta t\\)升幂展开得
\\[
\begin{eqnarray}
\nonumber \hat{U}(t_b,t_a)=&1&-\frac{i}{\hbar}\int_{t_a}^{t_b}\hat{H}(t)dt\\\
\nonumber &+&(\frac{i}{\hbar})^2\int_{t_a}^{t_b}\int_{t_a}^{t}\hat{H}(t)\hat{H}(t’)dt’dt\\\
\nonumber &+&(\frac{i}{\hbar})^3\int_{t_a}^{t_b}\int_{t_a}^{t}\int_{t_a}^{t’}\hat{H}(t)\hat{H}(t’)\hat{H}(t’’)dt’’dt’dt\\\
\nonumber &+&\cdots
\end{eqnarray}
\tag{4}
\\]


\\((4)\\)式被称为*Neumann-Liouville*展开或*Dyson*级数。


同样以二阶项为例
\\[\int_{t_a}^{t_b}\int_{t_a}^{t}\hat{H}(t)\hat{H}(t’)dt’dt=\int_{t_a}^{t_b}\int_{t_a}^{t’}\hat{H}(t’)\hat{H}(t)dtdt’=\int_{t_a}^{t_b}\int_t^{t_b}\hat{H}(t’)\hat{H}(t)dt’dt \tag{5}\\]


然而问题来了，\\((3)\\)式不再一定成立，于是\\(\hat{H}(t’)\hat{H}(t)\ne \hat{H}(t)\hat{H}(t’)\\)，上式中最左边和最右边的式子无法直接相加。


但是注意到，无论是左边还是右边，靠后的哈密顿量对应的时间都是较小的，于是我们可以通过引入Time-ordering算符\\(\hat{T}:\hat{T}(\hat{H}(t^{(n)})\cdots\hat{H}(t’)\hat{H}(t))=\hat{H}(t_{\sigma_n})\cdots\hat{H}(t_{\sigma_2})\hat{H}(t_{\sigma_1})\\)，其中\\(\{t_{\sigma_i}\}\\)是\\(\{t^{(i)}\}\\)的一个置换，且\\(t_{\sigma_1}<t_{\sigma_2}<\cdots<t_{\sigma_n}\\)。


利用\\(\hat{T}\\)，\\((5)\\)式可被改写为
\\[
\begin{eqnarray}
\nonumber &&\hat{T}\int_{t_a}^{t_b}\int_{t_a}^{t}\hat{H}(t)\hat{H}(t’)dt’dt=\hat{T}\int_{t_a}^{t_b}\int_t^{t_b}\hat{H}(t)\hat{H}(t’)dt’dt\\\ 
\nonumber &=&\frac{1}{2}\hat{T}\int_{t_a}^{t_b}\int_{t_a}^{t_b}\hat{H}(t)\hat{H}(t’)dt’dt\\\
\nonumber &=&\frac{1}{2}\hat{T}(\int_{t_a}^{t_b}\hat{H}(t)dt)^2
\end{eqnarray}
\\]


推广至高阶项后，最终可得
\\[
\begin{eqnarray}
\nonumber \hat{U}(t_b,t_a)=&1&-\frac{i}{\hbar}\int_{t_a}^{t_b}\hat{H}(t)dt+\frac{1}{2!}(\frac{-i}{\hbar})^2\hat{T}(\int_{t_a}^{t_b}\hat{H}(t)dt)^2\\\
\nonumber &+&\cdots\\\
\nonumber &+&\frac{1}{n!}(\frac{-i}{\hbar})^n\hat{T}(\int_{t_a}^{t_b}\hat{H}(t)dt)^n\\\
\nonumber &+&\cdots\\\
\nonumber &=&\hat{T}\exp(-\frac{i}{\hbar}\int_{t_a}^{t_b}\hat{H}(t)dt)
\end{eqnarray}
\tag{6}
\\]


\\((6)\\)式便是经常莫名直接出现在书上的表达式了。


### EOF


关于\\(\hat{T}\\)的必要性还有一种理解方式便是
\\[
\begin{eqnarray}
\nonumber \hat{U}(t_b,t_a)&=&e^{-\frac{i}{\hbar}\hat{H}(t_N)\Delta t}e^{-\frac{i}{\hbar}\hat{H}(t_{N-1})\Delta t}\cdots e^{-\frac{i}{\hbar}\hat{H}(t_a)\Delta t}\\\
\nonumber &\ne&e^{-\frac{i}{\hbar}(\hat{H}(t_N)\Delta t+\cdots+\hat{H}(t_a)\Delta t)}\\\
\nonumber &=&e^{-\frac{i}{\hbar}\int_{t_a}^{t_b}\hat{H}(t)dt}
\end{eqnarray}
\\]
因为当\\([A,B]\ne 0\\)时，\\(e^Ae^B\ne e^{A+B}\\)。不过取绝热近似或不同时刻哈密顿量可对易时，\\(\hat{T}\\)就不再必要了。


一个书上带过的Time-ordering Operator居然要写这么长来解释……果然物理书的公式不能想当然地认为自己理解了，每一个细节都要透彻的看清本质。