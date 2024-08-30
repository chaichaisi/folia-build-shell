
<div align="center">

# Folia-build-shell
_✨ 高效，快速的Folia核心端编译脚本！ ✨_


<a href="https://github.com/chaichaisi/folia-build-shell/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/chaichaisi/folia-build-shell?color=%09%2300BFFF&style=flat-square">
</a>
<a href="https://github.com/chaichaisi/folia-build-shell/issues">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/chaichaisi/folia-build-shell?color=Emerald%20green&style=flat-square">
</a>
<a href="https://github.com/chaichaisi/folia-build-shell/network">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/chaichaisi/folia-build-shell?color=%2300BFFF&style=flat-square">
</a>

</div>

## Folia-build-shell  
这是一个半自动一键编译多线程优化的我的世界Folia服务端的编译脚本  
This is a semi-automatic, one-click compilation script for the multi-threaded optimized Minecraft Folia server  
## Use  
Need Bash!!!!!!  
For Google Cloud Shell  
考虑到国内网络环境，脚本只适用于于谷歌云命令行云编译！请自行准备霍格沃兹魔法环境和谷歌账号以及Github用户名和邮箱！  

相对于自行本地电脑编译，时间漫长（普遍在4个小时左右编译好）不说，还会扰乱了系统环境（东一个java西一个java），考虑到大家并不是人人都有一台屌炸天的电脑和稳定的霍格沃兹魔法环境，使用本地编译大多是不幸的！  

但是我还是~~写了~~  

~~给个Star吧，谢谢了~~  

至于为何不用tx云命令行和al云命令行，也是因为网络环境问题，我们无法的解决这个棘手的问题，所以再三考虑使用了 [谷歌云命令行终端](https://shell.cloud.google.com/?hl=zh_CN&fromcloudshell=true&show=terminal) 它远在国外，自带稳定的魔法环境，免费，编译时间也仅需10分钟左右！  

目前本脚本只提供最新版本编译，可根据最后的编译产物的名称得到版本！  

自行编译可以体验完整版Folia核心带来的趣味和性能提升！  

同时也避免了使用夹带私货的，缺胳膊少腿的核心带来的一系列问题（亲身感受过）！  

这也是一个Minecraft Java腐竹需要学习的不可缺少的技术！  

本程序不会保存您的个人信息！  

## Only On Google Cloud Shell
First  
首先新标签页打开这个 [谷歌云命令行终端](https://shell.cloud.google.com/?hl=zh_CN&fromcloudshell=true&show=terminal) 登陆你的谷歌账号进入终端并输入以下命令回车  
```
sudo -i
```
Then  
然后黏贴以下代码回车即可开始编译，需要按照提示输入Github用户名和邮箱  
```
cd /
git clone https://github.com/chaichaisi/folia-build-shell.git
cd folia-build-shell
chmod +x build.sh
./build.sh
```
等待编译完成即可！有任何问题欢迎携带完整日志提交issus或前往b站教程视频评论区寻求帮助！  
~~我们是学生党，没时间修哇qaq~~
教程视频：  
[《我的世界》Folia最新版服务端编译教程](https://www.bilibili.com/video/BV1b4sgeaEtx/?share_source=copy_web&vd_source=3f9242217329b941ef581c85067e158f)  
## On Windows???
当然，如果你确定要在自己的电脑上运行编译脚本，我们也会提供，当然脚本将不会更新的迅速，出现的问题提交issus不会优先解决  
~~需要一定的Python基础~~  
确保你有非常完美的魔法环境，否则会变的不幸！！！
确保你有非常完美的魔法环境，否则会变的不幸！！！
确保你有非常完美的魔法环境，否则会变的不幸！！！  
首先  
确保您的windows系统拥有安装了[python3](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)（单击下载安装，只需要留意安装路径，没有需求直接一路Next安装），需要安装依赖库：  
```
pip3 install colorama subprocess
```
安装
然后  [点我下载Git](https://github.com/git-for-windows/git/releases/download/v2.46.0.windows.1/Git-2.46.0-64-bit.exe) （安装时只需留意安装目录，如果不需要更改的话可以全部点击Next）  
打开资源管理器，在你喜欢的位置按住Shift + 鼠标右键，单击Open Git Bash Here  
在终端中输入：
```
git clone https://github.com/chaichaisi/folia-build-shell.git
cd folia-build-shell
python3 build.py
```
最后  
按照提示输入你的Github用户名和邮箱即可，期间会安装Java 21，安装时只需留意安装目录，如果不需要更改的话可以全部点击Next  
不出意外的话会编译成功，可在当前文件夹下看到Folia产物，一般为80mb左右的.jar文件
这个方法啊没有教程哦，并且不推荐捏！~~Python脚本是机翻的捏，炸乐和我没关系哦！！！~~
