---
title: Notes on Complex Analysis(II)
tags: mathematica
layout: post
---
It's been a long while since the update of *Notes on Complex Analysis(I)*. And another long period is predictable for the update of *Following the Traces of Masters* series. I'll get these done step by step. This article is about the chapter 2 of *Visual Complex Analysis*.



### Complex Functions

A complex function is a function whose independent and dependent variables are both complex, namely a mapping \\(f: \mathbb{C}\rightarrow\mathbb{C}\\). Usually the \\(w\\) is used for the dependent variable and \\(z\\) for the independent variable. A complex function can therefore be seen as a transform: \\(z\mapsto w=f(z)\\).





A complex number can be expressed in either a Cartesian coordinate or a polar coordinate. Therefore, two ways are usually used to express a complex function:

- Cartesian Coordinate System:

  \\(z=x+iy,w=f(x+iy)=u+iv\\), where \\(u=u(x,y)\\) and \\(v=v(x,y)\\) are both binary functions of \\(x,y\\).

- Polar Coordinate System:

  \\(z=re^{i\theta},w=f(re^{i\theta})=Re^{i\phi}\\), where \\(R=R(r,\theta)\\) and \\(\phi=\phi(r,\theta)\\) are both binary functions of \\(r,\theta\\).



### The Visualization of Complex Functions

The best way to know about the properties of a function is, of course, to plot it. We can 'draw' a real function in a two-dimention plane. However, things are getting difficult under the complex situation, since four dimentions (\\(x,y,u,v\\)) are needed to 'draw' a complex one, which obviously cannot be done. Even so, we still have several ways to visualize it.





Firstly, by using the Cartesian coordinate system, \\(u(x,y)\\) and \\(v(x,y)\\) can be drawn independently as two graphs, which is the first option *wolfram alpha* is using for plotting a complex funciton.





Another common option is to introduce the concept of *image plane* (or \\(w\\)-plane) —— the plane with \\(u,v\\) axis. This gives us the ablity to show a complex function dynamically: when \\(z\\) goes along a curve in the \\(x,y\\) plane, \\(w\\) will go along a corresponding curve. It is very helpful to trace the movement of \\(w\\), which is especially important when dealing with multifunctions. And we can setup the grids in the \\(z\\)-plane, and see how the grids are curved in the \\(w\\)-plane. One interesting topic to mention is that the curved grids remain orthogonal if the function is analytic. This is the second way *wolfram alpha* would use to plot a complex function.





There are some other ways to plot a complex function like plotting \\(\lvert f(z)\rvert\\) in a 3-D coordinate. However, it cannot give us all the information of the function.





The concept of *Riemann Sphere* is also worth being mentioned, which will be introduced in later chapters. It helps to show a function at infinity.



### Positive Integer Powers

We are going to discuss about several basic elementary functions. And let's start with positive integer powers, which have only one value for each \\(z\\).





Consider the mapping\\(z\mapsto w=z^n, n\in \mathbb{N}\\). It's easier for us to calculate \\(w\\) by using polar coordinate, since Cartesian coordinate systems are more useful when dealing with addtion while polar coordinate systems are so with multiplication. 





If \\(z=re^{i\theta}\\), then \\(w=z^n=r^ne^{in\theta}\\), which has already told us all we need to know about positive integer powers. The modulus becomes \\(r^n\\), and the argument becomes \\(n\theta\\). If \\(z\\) goes along a circle of radius of \\(r\\) with the angular velocity of \\(\omega\\), then \\(w\\) will go along the circle of \\(r^n\\) with \\(n\omega\\), which is \\(n\\) times faster than \\(z\\). Therefore, It should be noticed that when \\(z\\) completes a whole circle, \\(w\\) has already completed it for \\(n\\) times. So on a complete circle, \\(n\\) choices of \\(z\\) can lead to a same \\(w\\). This won't cause any problem now, however, when we do it backwards —— \\(z=w^{1/n}\\), we get \\(n\\) values. We'll take care of this in later parts.



### The Exponential Function & Cosine and Sine

The book talks about power series first and use it to help describing the exponential function. But I want to write in my own order, which I think is easier to accept. 





Two ways to define the complex exponential function are talked about in the book. One is to use power series and the other is using a limitation: \\(e^z:=\lim_{n\rightarrow\infty}(1+\frac{z}{n})^n\\). However, a more common way you may find in other books about complex analysis to define \\(e^z\\) is by using cosine and sine: \\(e^z:=\cos z+i\sin z\\).So there are in total three ways to define \\(e^z\\). We'll compare the last two here.





The definition using limitation doesn't need anthing more than positive integer powers, just a situation with \\(n\rightarrow \infty\\). However, what the definition doesn't tell us is how to calculate directly. Apparently we don't want to use a limit for each time we see \\(e^z\\). So here comes the other definition:\\(e^z=e^x(\cos y+i\sin y)\\), which directly tells you how to calculate it out.





Everything seems fine here. Problems  usually show up in the following parts of a book of complex analysis: They use \\(e^z\\) to define \\(\sin z\\) and \\(\cos z\\):
\\[
\sin z:=\frac{e^{iz}-e^{-iz}}{2i}\\\
\cos z:=\frac{e^{iz}+e^{-iz}}{2}
\\]
I thought there must be something wrong when I first saw this weird definition: How could we define \\(e^z\\) with \\(\sin z\\) and \\(\cos z\\) but in turn use this newly defined \\(e^z\\) to define sine and cosine.





After a few days of being puzzled, I realized nothing is wrong here and that this definition is actually a great design. There is no circularly definition here, since we define the complex \\(e^z\\) using **real** sines and cosines, which are already defined perfectly in the 'real' world we are familar with. And in turn, we define the complex sines and cosines with this newly defined complex \\(e^z\\). And that explains why we need to split up \\(x\\) and \\(y\\) in the definition —— 'Cause \\(x\\) and \\(y\\) are both real so that we don't need to define anything new in spite of \\(i=\sqrt{-1}\\).





The book also gives us an elaborate description about the geometric way to understand these. But I'm not gonna talk over that here.



### The Logarithm Functions and Their Inverse Functions

Here we are going to deal with an essential part of the theory of complex functions, where multifunctions will be needed.





As we have seen before, one \\(w\\) as input can brings us \\(n\\) values of \\(z=w^{1/n}\\). We can see that one-valued functions cannot satisfy us now. We now take a look at the logarithm funcitons.





In the history, people cannot express the area under \\(\frac{1}{x}\\), so they define \\(\log x=\int_1^x\frac{1}{x}dx\\). Later they found out the inverse function of log, \\(e^x\\), is also very important. However, here we'll change the order of definition: We need to define \\(e^z\\) first, as we have done before, then define the logarithm function as the inverse function of \\(e^z\\).





That is to say, if \\(w=e^z\\), then in turn we say \\(z=Ln\ w\\). Here I use the capital L, which is often used to express the meaning of 'multi-valued'. It's easy to understand why it's multi-valued as \\(e^{z+2\pi i}=e^z\\). So there must be infinitely many \\(z\\) corresponding to one \\(w\\). Infinitely many values seem to give us no idea about where to start. Therefore, a **principal value** must be determined.





It's easy to prove that
\\[
Ln\ z=\ln|z|+iArg\ z,
\\]
so when \\(-\pi <Arg\ z\le \pi\\), we denote \\(\arg z\\) as the principal value of \\(Arg\ z\\) and \\(\ln z=\ln|z|+i\arg z\\) as the principal value of \\(Ln\ z\\).





The exponential function is so closely bounded to the trigonometric functions, so their inverse must also have some relation. Thus, It's possible for us to write \\(Arcsin\\) and \\(Arccos\\) in terms of \\(Ln\\).





\\(e^{iz}=\cos z+i\sin z=\sqrt{1-\sin^2z}+i\sin z\\), where the square root function is **two-valued** now. And then
\\[
iz=Arcsin(\sin z)=Ln(\sqrt{1-\sin^2z}+i\sin z),
\\]
so take \\(\sin z\\) as \\(s\\), yields
\\[
Arcsin(s)=-i\ Ln(\sqrt{1-s^2}+is)
\\]
And similarly we can get \\(Arccos\\).





And this provides us another trick to integrate \\(\frac{1}{\sqrt{1+x^2}}\\), which was developed by Euler:
\\[
I=\int\frac{dx}{\sqrt{1+x^2}}\\\
x=iy\\\
\begin{eqnarray}
\nonumber \Longrightarrow I&=&i\int\frac{dy}{\sqrt{1-y^2}}=iArcsin(y)+C\\\
&=&Ln(\sqrt{1-y^2}+iy)+C\\\
&=&Ln(\sqrt{1+x^2}+x)+C
\end{eqnarray}
\\]
But usually we only need the real result, so \\(I=\ln(\sqrt{1+x^2}+x)+C \\).





### Powers

We have dicussed about the positive integer powers, and now let's check more general conditions.In fact, we only need one step to have all problems solved:
\\[
a^b=e^{b\ Ln(a)}
\\]
And since we have known about \\(e^z\\) and \\(Ln(z)\\), this is nothing new to us.





However, there are something to be noticed. Let's now rewrite the equation:
\\[
a^b=e^{b\ Ln(a)}=e^{b(\ln|a|+iArg(a))}=e^{b(\ln|a|+i\arg(a)+2k\pi i)}
\\]
Now \\(b(\ln|a|+i\arg(a))\\) is fully determined, so we only need to focus on \\(2bk\pi i\\). If \\(b\in \mathbb{C}\\), \\(a^b=a^{Re+iIm}=a^{Re}+a^{iIm}=a^{Re}+\cos(Im)+i\sin(Im)\\), so we only need to know about the real part of b.





There are in total three conditions:

1. \\(b\in\mathbb{Z}\\)
2. \\(b\in\mathbb{Q\setminus Z}\\)
3. \\(b\in\mathbb{R\setminus Q}\\)

The first is dicussed before as positive integer powers. And what's interesting takes places in the second and third conditions.





Condition 2: We can always find a way to write \\(b\\) as a fraction of two integers: \\(b=\frac{m}{n}\\). Now \\(2bk\pi i=\frac{2mk\pi i}{n}=2m\pi i\frac{k}{n}\\). Now when \\(k\in\{0,1,2,…,n-1\}\\), we get \\(n\\) different values. And ever since \\(k\\) is greater than \\(n\\), the values start to repeat. So it's n-valued, the same as we discovered before.





Condition 3: 	This time \\(2bk\pi i\\) can never provide repeated values, so it's infinitely-many-valued. And the best way we can write it is with the logarithm.



### Multifunctions

As talked before, the logarithms and many powers are 'many-valued'. These functions are so-called **multifuncitons**. However, it's confusing for a funciton to has more than one value at a single point, as we have no idea about what \\(f(z)\\) means, or which value it represents.





So the key problem now is how can we properly represent a multifunction?





I have mentioned, in the early parts of this post, that the method to have \\(z\\) and \\(w\\) to be in the same plane and watch how they are moving is important. Now this method shows its power. Consider a positive integer power funciton, take \\(w=f(z)=z^3\\) as an example, and imagine that when \\(z\\) is at the point \\(re^{i\theta}\\), \\(w\\) will be at \\(r^3e^{i3\theta}\\). Now, as we have done before, let \\(z\\) goes along the unit circle. And \\(w\\) will then also go along the unit circle, but at a angular speed 3 times as \\(z\\). It's easy to see that when \\(z\\) has just completed one third of the circle, let's say \\(\theta=\frac{2\pi}{3}\\), \\(w\\) has already completed the whole circle.





Now let's have a role change. If we move \\(w\\) instead of \\(z\\), we shall see that when \\(w\\) has already completed a whole circle, \\(z\\), respectively, has only completed one third. Now \\(w\\) is at \\(1\\) with \\(z\\) at \\(e^{\frac{2\pi}{3}i}\\). Remember these points. And now let \\(w\\) go along an arbitary loop, which does not contain \\(O\\). You should see that \\(z\\) will always get back to \\(e^{\frac{2\pi}{3}i}\\), where it stayed before the move. What happens if the loop contains \\(O\\), like the unit circle? The answer is quite amazing. Just like how \\(z\\) gets \\(e^{\frac{2\pi}{3}i}\\) from \\(1\\), now it gets to \\(e^{\frac{4\pi}{3}i}\\). When \\(w\\) completes another similar loop, \\(z\\) will again go back to \\(1\\).





Riemann came up with a great idea to express such a multifunction: to make it a single-valued one. To be precise, we divided the \\(\mathbb{C}\\) plane of \\(w\\) into 3 layers. Once it goes across the boundary line, \\(w\\) goes into another layer. So in this way, we have 3 different single-valued function on each layer. These layers are now so-called 'Riemann surfaces'. However, the value on that boundary line should be made clear individually.





Each single-valued function on each layer is called a *branch* of \\(f(z)\\). And in this example, the origin \\(O\\) is a special point. When the loop goes around it, the function will go on another branch. So this point is called the *branch point*. \\(w\\) goes 3 loops when \\(z\\) gets back, that's twice more than a single-valued function, so it's a *branch point of order 2*.





The example we dicussed before has finite number of layers. That does not always happen, however. When it appears to be a logarithm, you should see that it has infinitely many layers, as it has infinitely many values. This happens when dealing with logarithms or irrational powers. The branch points of finite layers are called an *algebraic branch point* and the infinitely-many-situaition with *logarithmic branch point*.



# EOF

This is the first time for me to write such a long article in English. And that's why it took so long to have an update. I'm considering to have every post a English version along with a Chinese version. But that would take even more time.





This post doesn't cover all contents of chapter 2. So in the next post, we'll be concerned about power series, covering the left part of chapter 2.