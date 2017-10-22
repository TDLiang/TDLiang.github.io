---
layout: post
title: jekyll搭建本站的过程
tags: Computer-Settings
---

从早上起来就开始着手搭建博客了，一直到这个点，终于基本配置完成了，在此把本站建立的过程记录下来。

# 挑选博客平台
有很多类似CDSN的平台都提供了博客功能，但是总觉得不够'geek'，于是开始寻找各类博客平台。最终把目标锁定在[jekyll](http://jekyll.com.cn/) + [Github Pages](https://pages.github.com/)。

作为个人博客，配置的自由度一定是要保证的。jekyll基于ruby开发，完全开源，可以自己开发或者使用其他人开源的插件及主题（比如我暂时用的这款），这就让博客具有了无限可能性。Github Pages平台最好的一点就是免费提供1G的储存，这对一个博客已经足够了。

在反复斟酌各类平台时，突然搜到了这篇博文：http://baixin.io/2016/10/jekyll_tutorials1/ ，瞬间被这个博客的风格吸引，并暂时借用了他开源的主题。了解后发现jekyll时基于Ruby开发的，我此前学习Metasploit的时候略微了解过一些Ruby语法，觉得日后自己写主题和插件应该会轻松些，于是决定采用jekyll框架。

# 搭建过程
#### 系统：Linux Mint 18.2, 基于Ubuntu (OS X过程与此类似)
（不建议在Windows下使用jekyll）

---
先在此列出参考的博文，并向博主们表示感谢：

http://baixin.io/2016/10/jekyll_tutorials1/

https://ytf513.github.io/2015/08/21/Install-jekyll-Error-Handler.html


以及官方文档（用在建立jekyll目录时参考）：

https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/

## 0.准备
确认机器已安装：

    1.Ruby
    2.RubyGems

本系统自带了Ruby，以及RubyGems，此处就不叙述了。

## 1.安装jekyll
终端运行：

    sudo gem install jekyll -V

-V用于输出安装过程具体信息，因为这个过程可能比较慢，甚至无法连接，至少如此能看到大概进程。


上述速度慢可以通过更改源解决：

    gem sources --remove https://rubygems.org/
    gem sources -a http://ruby.taobao.org/
    gem sources -l
    gem sources -u
    
下面安装bundle（否则会报错）：

    gem install bundler
    bundler install

接下来理论上来说就已经可以建立自己的博客了，只不过是空白模板。

终端进入到储存博客配置的目录，运行：

    jekyll new myBlog
    cd myBlog
    jekyll serve
至此jekyll服务已经打开，打开浏览器，进入 http://localhost:4000即可看到空白模板效果。


## 2.配置主题
我希望使用baixin开发的主题[leopard](https://github.com/leopardpan/leopardpan.github.io/)（本站暂用主题），所以删去了上面建立的myBlog文件夹。我首先 folk了baixin 的 leopard repository，并clone到了本地，删去_posts目录下的全部文件以及根目录的CNAME文件，并重新配置了 _config.yml文件。

这时候新建一个自己的repository，命名为：username.github.io（username必须为github账号，否则无法使用Github Pages服务）。我将clone的文件夹改名后，git push三部曲将leopard push到自己的repository下：

在repository根目录下：
    
    git add -all
    git commit -m 'comment' #初次使用会要求配置github账号信息等
    git push -u origin master 
若日后在github网页上更改了文件（不推荐）而未同步到本地，此时push会提示错误，只需要在master前加上+，强制push即可：

    git push -u origin +master

此时打开浏览器，进入 username.github.io，赏心悦目的界面就出现了。

## 3.发布文章
文章全部保存在_posts目录下，我使用Markdown（md）格式编写（有道云笔记自带Markdown编辑器）。注意jekyll对文件名严格要求。具体参考官网指南：http://jekyll.com.cn/docs/posts/

暂时尚未学习如何上传图片（本文一张图都没有的原因...），但瞥了一眼教程觉得不复杂，以后的文章中会附加图片。

我在有道云笔记中编辑好md文件后，下载并存入_post目录，再一次git push三部曲，等待一会后即可看到博客中的文章了。

## 4.域名配置(Optional)
域名上挂着 github.io，就总觉得不够自己的牌子，于是决定自定域名。

可以使用DNSPod平台购买及配置域名（配置免费，我事先不知道DNSPod，所以在GoDaddy上买下了此域名，价格一样）。具体过程在 http://blog.csdn.net/yuan3065/article/details/51594454 中很详尽。我花120买了两年的freezingsummer.com域名，平均一个月五块钱，不算贵，到期可以续费。

注意此处并不需要用到Github Repository Settings中提供的Customed Domain功能，DNSPod可以完成域名转换的功能。

文中说需要经历漫长的等待，但是配置完成后，只过了半小时多的时间就发现域名已经可以使用了。

# Done
第一篇正文就此结束啦，一整天绕了不少弯路，此处记录下精炼后的步骤，还有很多配置没有完成，毕竟完善博客是一个漫长的过程，我慢慢写，你慢慢看。
