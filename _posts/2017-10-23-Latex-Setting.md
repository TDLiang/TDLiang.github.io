---
layout: post
title: 在jekyll下使用Latex
tags: Computer-Settings

---

## 更换Markdown解析器
可以看到昨天的博客中有不少数学公式，Latex是一种很常用的公式书写格式，然而在Markdown编辑器中预览得很好的公式，在网页中却并没有显示应有的效果。

jekyll默认使用Maruku作为Markdown解析器，官网上说Maruku可以支持Latex，但是Maruku貌似已经无人维护了，很多相关的链接都无法打开，于是只好另寻出路。jekyll还支持另外两种解析器以及自己写的解析器，考察后发现还是Kramdown更为靠谱，于是决定使用Kramdown。

## 安装Kramdown

#### Step 1
在终端运行下面命令：(for Linux & Mac OS X)
	`sudo gem install kramdown`
#### Step 2
编辑jekyll项目目录下的**_config.yml**文件，增加一行：
	`markdown: kramdown`
#### Step 3
编辑_layout目录下的模板，在需要显示公式的模板下加入如下代码
```
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>  
```

参考：

[https://stackoverflow.com/questions/26275645/how-to-supported-latex-in-github-pages](https://stackoverflow.com/questions/26275645/how-to-supported-latex-in-github-pages)

[https://kramdown.gettalong.org/installation.html](https://kramdown.gettalong.org/installation.html)

[http://jekyll.com.cn/docs/extras/](http://jekyll.com.cn/docs/extras/)

---
接下来就可以使用Latex了，但要注意和普通的Kramdown下公式插入方式与Maruku不同，并不支持`${...}$`和`$$${...}$$$`作为行内和行间公式，仅支持`$${...}$$`作为行内公式。但这种写法容易混淆，不如使用`\\(...\\)`作为行内公式，`\\[\\]`作为行间公式。
```
$$\zeta(s) = \sum_{n = 1}^\infty\frac{1}{n^s}$$
或者
\\[\zeta(s) = \sum_{n = 1}^\infty\frac{1}{n^s}\\]
```
显示效果如下：
\\[\zeta(s) = \sum_{n = 1}^\infty\frac{1}{n^s}\\]
（从今年暑假开始对黎曼猜想很有兴趣，关于黎曼Zeta函数\\(\zeta(s)\\)后续会有文章介绍。）

# EOF
附上花了好大劲敲出来的柯西积分公式～
```
\\[f(z)=\frac{1}{2\pi i}\oint_C\frac{f(\xi)}{\xi-z}d\xi\\]
```
\\[f(z)=\frac{1}{2\pi i}\oint_C\frac{f(\xi)}{\xi-z}d\xi\\]