# HackThisSite 部分攻略

[Hack This Site](https://www.hackthissite.org/)提供了很多在线的关卡，包含了网络安全领域各方面的基础知识。

在此记录部分攻略用于学习交流。首次任务建议独立思考完成。

## Basic Missions

### Mission 7 --2017.11.4

问题描述：
Level 7

This time Network Security sam has saved the unencrypted level7 password in an obscurely named file saved in this very directory.

In other unrelated news, Sam has set up a script that returns the output from the UNIX cal command. Here is the script:

下方给出了一个输入窗：
Enter the year you wish to view and hit 'view'.

---

根据提示，这个窗口在服务端运行的是cal命令，会将用户提交的数据作为cal的参数，将输出流中的结果显示在网页上。

也就是说，我们可以通过控制输出流来找到我们想要查看的信息。

Linux中多条命令可以用 ; 隔开，写在一行中，所以我们用“2017 ;”可以终止当前语句，并执行下一个命令。

我们希望找到该网页目录下的密码文件，于是可以输入：
```
2017 ; ls .
```
最后那一个点代表当前目录。
于是得到当前目录下的文件：
```
.
..

cal.pl
index.php
k1kh31b1n55h.php
level7.php
```

显然```k1kh31b1n55h.php```是我们要找的文件

下面我们只需要进入
```
https://www.hackthissite.org/missions/basic/7/k1kh31b1n55h.php
```

即可查看到密码。

Mission Completed.

### 将会持续更新