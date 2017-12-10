---
title: 各类傅立叶变换
tags: mathematica
layout: post
---

//本周组会内容是傅立叶变换，所以复分析第二章的笔记要到下周才能发布。

最近物理中学到傅立叶奇数，线代中学到FFT，突然间出现了各类有关傅立叶的名词。在此将其串在一起进行总结，大概思路如下：

\\[FS\rightarrow FT\rightarrow DFT\rightarrow FFT \rightarrow QFT\\]

### FS(Fourier Series)
在此前文章[线性空间](http://freezingsummer.com/2017/11/linearSpace/)中，提到了傅里叶展开就是将函数投影到三角函数张成的无穷维空间上。

但是傅里叶展开有一点十分令人不满----第一项要写成\\(\frac{1}{2}a_0\\)，或者\\(a_0\\)的公式要单独列出。这种违和是让人十分心塞的。下面我们换一种形式，让傅里叶变换的系数公式统一起来，十分简洁。

首先把展开公式照搬过来：

考虑周期为\\(T\\)的函数\\(f(t)\\)，其一个周期为\\([-\frac{T}{2},\frac{T}{2}]\\)，我们可以将其展开为：
\\[f(t)=\frac{1}{2}a_0+a_1\cos \omega_0t+b_1\sin\omega_0t+a_2\cos  2\omega_0t+b_2\sin 2\omega_0t+...\\]
其中\\[\omega_0=\frac{2\pi}{T},a_n=\int_{-\frac{T}{2}}^{\frac{T}{2}}f(t)\cos n\omega_0tdt,b_n=\int_{-\frac{T}{2}}^{\frac{T}{2}}f(t)\sin n\omega_0tdt\\]

如果想统一\\(sin,cos\\)，最好的办法就是用复数，这样三角函数就是指数函数了。

我们用欧拉公式：\\(e^{ix}=\cos x+i\sin x\\)，将上式改写：
\begin{eqnarray}
\nonumber f(t)&=&\frac{a_0}{2}+\sum_{n=1}^{+\infty}(a_n\cos n\omega_0t+b_n\sin n\omega_0t)\\
\nonumber &=&\frac{a_0}{2}+\sum_{n=1}^{+\infty}(a_n\frac{e^{in\omega_0t}+e^{-in\omega_0t}}{2}+b_n\frac{e^{in\omega_0t}-e^{-in\omega_0t}}{2i})\\
\nonumber &=&\frac{a_0}{2}+\sum_{n=1}^{+\infty}(\frac{a_n-ib_n}{2}e^{in\omega_0t}+\frac{a_n+ib_n}{2}e^{-in\omega_0t})
\end{eqnarray}
下面为了得到统一形式，我们取\\(c_0=\frac{a_0}{2},c_n=\frac{a_n-ib_n}{2},c_{-n}=\frac{a_n+ib_n}{2}\\)，上式可以继续化简：
\begin{eqnarray}
\nonumber f(t)&=&c_0+\sum_{n=1}^{+\infty}c_ne^{in\omega_0t}+\sum_{n=1}^{+\infty}c_{-n}e^{-in\omega_0t}\\
\nonumber &=&c_0+\sum_{n=1}^{+\infty}c_ne^{in\omega_0t}+\sum_{n=-1}^{-\infty}c_ne^{in\omega_0t}\\
\nonumber &=&\sum_{n=-\infty}^{+\infty}c_ne^{in\omega_0t}
\end{eqnarray}

不仅展开式如此得到了简化，现在无论\\(n\\)是正是负还是零，都具有了一样的表达式：
\\[c_n=\frac{1}{T}\int_{-\frac{T}{2}}^{\frac{T}{2}}f(t)e^{-in\omega_0t}dt\\]
这个式子的证明类似求\\(a_n,b_n\\)的过程，在此不多叙述。

### FT(Fourier Transform)
傅里叶级数只能展开周期函数，这也是其一个缺点，那么很自然地会想到，如果我们取周期\\(T\\)无穷大，不就可以开非周期函数了？但是这样作为展开的意义并不大，因为\\(T\\)无穷大时，\\(\omega_0\\)会变得无穷小，让具体的每一项看起来意义不大。但人们发现了这样做的另一种意义：此时的系数\\(c_n\\)的意义。

\\(T\rightarrow \infty, \omega_0=\frac{2\pi}{T}\rightarrow 0\\)，但同时\\(n\\)从\\(-\infty\\)到\\(+\infty\\)取便所有整数，所以\\(\omega=n\omega_0\\)可以作为连续变量来看待，其取值为\\(-\infty\\)到\\(+\infty\\)。同时\\(\omega\\)对应的微元就是\\(d\omega=\omega_0=\frac{2\pi}{T}\\)。

于是傅里叶系数\\(c_n\\)就变成了\\[\frac{d\omega}{2\pi}\int_{-\infty}^{+\infty}f(t)e^{-i\omega t}dt=\frac{1}{2\pi}F(\omega)d\omega\\]
其中\\(F(\omega)=\mathcal{F}[f(t)]=\int_{-\infty}^{+\infty}f(t)e^{-i\omega t}dt\\)给出了\\(f(t)\\)的傅里叶变换。

同时我们得出
\\[f(t)=\sum_{n=-\infty}^{+\infty}c_ne^{in\omega_0t}=\frac{1}{2\pi}\int_{-\infty}^{+\infty}F(\omega)e^{i\omega t}d\omega=\mathcal{F}^{-1}[F(\omega)]\\]
给出了傅里叶变换的逆变换。

回看\\(c_n\\)的表达式\\(\frac{1}{2\pi}F(\omega)d\omega\\)，而\\(f(t)\\)是对\\(c_ne^{in\omega_0t}=\frac{1}{2\pi}F(\omega)e^{i\omega t}d\omega\\)的求和，可以看出\\(F(\omega)\\)其实代表了一种权重，对\\(\omega\\)处的\\(d\omega\\)赋予权值，再进行求和。

傅里叶级数告诉我们函数\\(f(t)\\)可以写成系统无数个简正模式的叠加，其傅里叶系数标记了各简正模式的振幅。那么傅里叶变换中的傅里叶系数\\(c_n\\)也代表了各简正模式的叠加，只不过此时的简正模式的频率不再是离散变量\\(\omega_0,2\omega_0,3\omega_0,...\\)，而是连续变量\\(\omega=n\omega_0=nd\omega\\)。\\(F(\omega)\\)给出了频率为\\(\omega\\)的振动的振幅，再将其叠加（积分），就可以复原这个非周期的函数（信号）。

时域上\\(f(t)\\)代表了\\(t\\)时刻的信号大小，频域上\\(F(\omega)\\)代表了\\(\omega\\)频率代表的比重。因此我们常常听见“傅里叶变换就是把函数从时域变换到频域”这么一种说法。

---

####傅里叶变换的应用
工程上应用此处不提。

数学上，和拉普拉斯变换一样，都可以用来快速地求解\\(n\\)阶线性微分方程，其他应用在此也不举例了。

但还有一些有趣的应用，其中一例可以参考[科学空间的一篇文章](http://spaces.ac.cn/archives/3108/)，用傅里叶变换求解阶乘的通项公式(\\(\Gamma\\)函数表达式)。

---

### DFT(Discrete Fourier Transform)

#### DTFT

讲离散傅里叶变换DFT之前，先要讲到DTFT(Discrete-Time Fourier Transform，离散时间傅里叶变换)。

首先回到第一部分--FS部分，用变换的角度来看看发生了什么：
\\[f(t)=\sum_{n=-\infty}^{+\infty}c_ne^{in\omega_0t}\\]

此前我们站在已知\\(f(t)\\)的角度，来求出\\(c_n\\)。但是直接观察这个式子，更容易想到的其实是我们输入了一个数列\\(c_n(n\in Z)\\)，得到了一个连续的周期函数。

也就是已知关于频率的离散序列，我们得到了时间的连续周期函数。那么反过来，更常发生的是，我们知道在一些时刻对应的个函数值\\(f(t_n)\\)，是否能将其改写成频率的周期函数。这有点作为傅里叶级数的逆变换的感觉，但是不一样。

于是引出了离散时间傅里叶变换DTFT：
\\[F(\omega)=\sum_{n=-\infty}^{+\infty}f(t_n)e^{-in\omega}\\]

这样通过离散的点的采样得到了这个信号的频率信息，即该频率对应的振幅，因此\\(F(\omega)\\)被称为这若干个离散值形成的序列的**频谱**。

一种更加常见的写法是这样：
\\[X(e^{i\omega})=\sum_{n=-\infty}^{+\infty}x(n)e^{-in\omega}\\]
其中\\(x(n),n\in Z\\)为一个离散的数列。写成这种形式是因为DTFT是Z变换的一种特例。

---

Z变换：```（此部分内容要求略有复分析基础，其他童鞋可以跳过）```
\\[F(z)=\sum_{n=-\infty}^{+\infty}f(n)z^{-n}\\]
其中\\(f(n)\\)为一个数列，\\(n\in Z\\)。其实Z变换也就是一个特殊的洛朗级数。

类似傅里叶变换可以求解微分方程，Z变换可以用来解数列递推公式，在此不过多展开，日后复分析系列笔记中会有。

值得注意的如果在单位圆上取\\(z\\)的值（单位根），即得到了DTFT。也就是说DTFT是Z变换在单位圆上的特殊形式。

---

但是实践中是不可能实现DTFT的，因为我们不能对无穷多个时间点取样，因此得不到连续的频谱函数\\(F(\omega)\\)，于是又引入了DFT。

#### DFT
如果不取无穷个点，而只取\\(N\\)个点，我们就可以得到一个周期离散序列：
\\[X(k)=\sum_{n=0}^{N-1}x(n)e^{-in\frac{2\pi}{N}k}\\]
也就是将原来的连续变量\\(\omega=n\omega_0=n\frac{2\pi}{T}\\)变成了离散变量\\(\frac{2\pi k}{N}\\)。

由于指数项具有周期性，如此变换的序列\\(X(k)\\)也就有周期性，其周期为\\(N\\)。(因为\\(e^{-in\frac{2\pi}{N}(k+N)}=e^{-in\frac{2\pi}{N}k-i2\pi n}=e^{-in\frac{2\pi}{N}k}\\))

也就是说\\(k\\)的取值只有\\(N\\)个是有意义的，其余的都是周期重复，那不妨取\\(k=0,1,...,N-1\\)，于是得到了同样长度为\\(N\\)的离散序列\\(X(k)\\)。

回顾这个过程，我们输入了长度为\\(N\\)的离散序列\\(x(n)\\)，得到了长度为\\(N\\)的离散序列\\(X(k)\\)。

---

#### DFT的应用

同样我们不谈工程上的应用，来看看DFT在数学上的应用--DFT可以将一个多项式由系数表示变为点值表示。

考虑一个\\(N-1\\)次多项式\\(f(x)=a_0+a_1x+a_2x^2+\cdots+a_{N-1}x^{N-1}\\)，其可以用一个向量\\(a=[a_0,a_1,...,a_{N-1}]^T\\)来表示。这种表示被称为多项式的系数表示。

多项式还可用点值表示--在多项式上取\\(N\\)个不同的点\\((x_1,y_1),(x_2,y_2),...,(x_{N-1},y_{N-1})\\)表示。因为由\\(N\\)个点可以确定一个\\(N\\)次多项式，只需要解一个\\(N\\)元一次方程组：

\\[
\begin{bmatrix}
\nonumber 1 & x_1 & x_1^2 & \cdots & x_1^{N-1} \\\
\nonumber 1 & x_2 & x_2^2 & \cdots & x_2^{N-1} \\\
\nonumber \vdots & & & & \vdots \\\
\nonumber 1 & x_{N} & x_N^2 & \cdots & x_N^{N-1}
\end{bmatrix}
\begin{bmatrix}
\nonumber a_0 \\\
\nonumber a_1 \\\
\nonumber \vdots \\\
\nonumber a_{N-1}
\end{bmatrix} =
\begin{bmatrix}
\nonumber y_1 \\\
\nonumber y_2 \\\
\nonumber \vdots \\\
\nonumber y_N
\end{bmatrix}
\\]

就可以确定\\(a\\)向量。

上式用矩阵写成\\(Xa=y\\)，其中\\(X\\)是一个范德蒙德行列式的转置。

那么假如我们事先约定好一组\\(x_k\\)，只需要一个向量\\(y=[y_1,y_2,...,y_N]^T\\)，就可以唯一地确定一个多项式。

我们不妨选定\\(N\\)次单位根为这一组自变量，即\\(x_k=e^{i\frac{2\pi}{N}k}\\)，正好有\\(N\\)个单位根。

如此，\\(y_k=\sum_{n=0}^{N-1}a_ne^{i\frac{2\pi}{N}kn}\\)，这正好是DFT的形式！(其实并不完全一样--指数上的系数一正一负。指数上的系数时而正时而负很让人迷惑，但实际这并没有那么重要。所有的推导对正或对负都是同样适用的，只是对于一个变换，其逆变换指数上的系数一定相反。此处为了符合多项式，选系数为正。)

当选取单位根是，范德蒙德行列式的转置\\(X\\)就成了傅里叶矩阵\\(F\\)：
\begin{equation}
\nonumber F=
\begin{bmatrix}
\nonumber 1 & 1 & 1 & \cdots & 1 \\\
\nonumber 1 & \omega & \omega^2 & \cdots & \omega^{N-1}\\\
\nonumber \vdots & & & & \vdots \\\
\nonumber 1 & \omega^{N-1} & \omega^{2(N-1)} & \cdots & \omega^{(N-1)^2}
\end{bmatrix}
\end{equation}
其中\\(\omega\\)是第一个单位根\\(e^{\frac{2\pi i}{N}}\\)。

于是我们输入系数向量\\(a\\)作为一组离散点，经过DFT变换得到了函数值向量\\(y\\)同样也是一组离散点。DFT将一个多项式由系数表示变换成了点值表示。

DFT有什么优势呢？DFT的逆变换十分简单：
\\[x(n)=\frac{1}{N}\sum_{k=0}^{N-1}X(k)e^{in\frac{2\pi}{N}k}\\]

注意此处指数上符号相反，得到
\\[a_n=\frac{1}{N}\sum_{k=0}^{N-1}y_ke^{-in\frac{2\pi}{N}k}\\]

这也可以从\\(F\\)的逆矩阵\\(F^{-1}\\)看出：
\\[F^{-1}=\frac{F^*}{N}\\]

\\(F^*\\)为\\(F\\)的共轭矩阵（即每个元素取共轭复数）。

扯了这么多，点值表示到底有啥好处呢？

对大多数情况来说，系数表示更好，因为对这个多项式是全知的，但是在进行多项式乘法时，点值表示更简便：

有两个多项式
\\[f(x)=a_0+a_1x+...+a_Nx^N\\]
\\[g(x)=b_0+b_1x+...+b_Nx^N\\]

现在要求出两者乘积\\(h(x)=f(x)g(x)=c_0+c_1x+...+c_{2N}x^{2N}\\)。如果直接处理，需要将\\(a_i\\)和\\(b_i\\)两两相乘，复杂度为\\(O(N^2)\\)。

但是如果用点值处理，分别得到\\(f(x)\\)和\\(g(x)\\)上的\\(2N+1\\)个点\\((x_1,f(x_1))\cdots(x_{2N+1},f(x_{2N+1})), (x_1,g(x_1))\cdots(x_{2N+1},g(x_{2N+1}))\\)

只需要进行\\(N\\)次相乘，就可以得到\\(h(x)\\)的\\(2N+1\\)个点\\((x_1,f(x_1)g(x_1))\cdots(x_{2N+1},f(x_{2N+1})g(x_{2N+1}))\\)，作为点值表示。

那么假如将系数表示变为点值表示的复杂度不超过\\(O(N^2)\\)，那么就可以加速多项式乘法。

但是直接进行DFT的复杂度依然是\\(O(N^2)\\)，这是因为我们还没有用到单位根的性质。利用单位根的形式可以迅速进行DFT，这就需要引入FFT：

---

### FFT(Fast Fourier Transform)
FFT实际上是一个分治算法。

将多项式\\(f(x)=a_0+a_1x+...+a_{2^n-1}x^{2^n-1}\\)的奇次和偶次分开（如果系数不到\\(2^n\\)，后面的用零补齐）：
\\[f(x)=(a_0+a_2x^2+...+a_{2^n-2}x^{2^n-2})+x(a_1+a_3x^2+...+a_{2^n-1}x^{2^n-1})\\]

于是得到了关于\\(x^2\\)两个多项式。而单位根有一个十分好用的性质，即第\\(n\\)个单位根\\(w_n^2=w_{\frac{n}{2}}\\)。

再重复上述操作，直到最后变成两个一次函数。

此过程计算复杂度有递推公式\\(T(N)=2T(\frac{N}{2})+O(N)\\)，于是推出\\(T(N)=O(NlogN) < O(N^2)\\)

因此FFT可以加速多项式乘法。

当然其应用远不止于此。

### QFT(Quantum Fourier Transform)

量子傅里叶变换QFT和FFT很类似，限于篇幅，在此不详细解释，此后写到Shor算法时，会有详细介绍。

# EOF
这篇写下来好累啊，最后一部分有点赶进度了。在网上查傅里叶变换的资料，总是一堆工程上的应用，于是自己写了这一篇主要从数学角度来看的各类傅里叶变换。不得不说傅里叶分析的确是十分powerful的工具。