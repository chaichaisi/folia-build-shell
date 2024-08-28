#!/bin/bash

# 全自动Folia客户端一键编译，只测试可用于谷歌云命令行 v0.1
# 创作者：Chaichaisi https://github.com/chaichaisi/ https://space.bilibili.com/2018774790
#         XiaoMing5442 https://github.com/XiaoMing5442 https://space.bilibili.com/455779705
# 侵权必究 未经作者允许不可转载！！！

#定义颜色变量
RED='\E[1;31m'     #红2
GREEN='\E[1;32m'    # 绿
YELLOW='\E[1;33m'    # 黄
BLUE='\E[1;34m'     # 蓝
PINK='\E[1;35m'     # 粉红
RES='\E[0m'         # 清除颜色
#用echo -e来调用
#echo -e "${RED} this is red color ${RES}"

filepath=$(cd "$(dirname "$0")"; pwd)
cd /

sudo rm -rf /tmp/jdk-21_linux-x64_bin.deb*
sudo rm -rf Folia
sudo rm -rf ~/Folia
sudo rm -rf /Folia
sudo rm -rf ~/.gradle/
rm -rf ~/.gradle/

echo -e "${BLUE}------------------------------------------------------------------------------------------${RES}"
echo -e "Folia 是 Paper 的一个分支,由 Minecraft 优化 BOSS Spottedleaf 开发。有多线程优化"
echo -e "${GREEN}这是一个半自动Folia核心编译脚本，只提供最新版本编译，编译期间不要关闭您的shell窗口，注意窗口保持连接！${RES}"
echo -e "作者：Chai https://github.com/chaichaisi/ https://space.bilibili.com/2018774790"
echo -e "作者：XiaoMing5442 https://github.com/XiaoMing5442 https://space.bilibili.com/455779705"
echo -e "侵权必究 未经作者允许不可转载！！！"
echo -e "${RED}如果你中途输入错误，请使用 Ctrl + c 重新运行脚本！编译过程中不可轻易结束进程！会变得不幸！！！${RES}"
echo -e "即将开始编译，请准备Github中的用户名以及邮箱，注意大小写和中文与英文字符！[Y/n]:"
read setupmode
if [ "$setupmode" = 'n' ] || [ "$setupmode" = 'N' ]; then
    echo -e "用户拒绝，正在退出，请重新运行脚本，执行到上一步时请输入y或者Y同意运行！"
    sleep 3
    exit 0
fi
echo -e "${RED}你${RES}${GREEN}真${RES}${PINK}的${RES}${YELLOW}准${RES}${BLUE}备${RES}${RED}好${RES}${BLUE}了${RES}${PINK}吗${RES}？[Y/n]:"
read setupmode_realy
if [ "$setupmode" = 'n' ] || [ "$setupmode" = 'N' ]; then
    echo -e "用户拒绝，正在退出，请重新运行脚本，执行到上一步时请输入y或者Y同意运行！"
    sleep 3
    exit 0
fi
echo -e "[STEP 1/4]配置Git 请输入Github的用户名(username):"
read username
echo -e "[STEP 2/4]配置Git 请输入Github的邮箱(email):"
read email
sudo git config --global user.name "${username}"
sudo git config --global user.email "${email}"
echo -e "${GREEN}[STEP 3/4]开始编译Folia最新核心，请耐心等待！${RES}"
echo -e "读取用户名 : ${username}"
echo -e "读取邮箱 : ${email}"
sleep 5
sudo apt remove openjdk-11* -y
sudo apt remove openjdk-17* -y
cd /tmp
sudo wget https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.deb
sudo dpkg -i jdk-21_linux-x64_bin.deb
sudo rm -rf jdk-21_linux-x64_bin.deb
cd $filepath
JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64/
sudo git clone https://github.com/PaperMC/Folia.git
cd Folia/
sudo chmod 777 * -R
sudo ./gradlew applyPatches
sudo ./gradlew createMojmapBundlerJar
if ls ./build/libs/*.jar >/dev/null 2>&1; then
    echo "文件夹中有 .jar 文件。真棒！它没问题！"
    echo -e "${GREEN}[STEP 4/4]恭喜，如果看到绿色字体SUCCESSFUL，代表着编译Folia核心是成功的！如果没有，请重试从我们的b站视频或前往我们的项目提交${RES}${RED}携带完整日志issus来帮助我们解决您的问题${RES}"
else
    echo -e "有问题！文件夹中没有 .jar 文件。请重试从我们的b站视频或前往我们的项目提交${RED}携带完整日志issus来帮助我们解决您的问题${RES}"
    echo "项目地址 https://github.com/chaichaisi/folia-build-shell "
    echo -e "${RED}Error.${RES}"
    echo -e ":("
    exit 1
fi
echo -e "自动为您切换到编译完产物目录，我们会为您全部移动到主目录！目录为/home"
sudo cp ./build/libs/*.jar /home/
echo '大获全胜！已经结束，请单击右上角三点选择下载，展开/home的文件，选择您编译的Folia核心文件并下载，届时您可以享受原汁原味的Folia核心带来的性能提升！'
echo "项目地址 https://github.com/chaichaisi/folia-build-shell 能给个Star嘛"
sleep 1
echo 'Done！ :)'
echo "Folia更多详情咨询：https://papermc.io/software/folia"
echo "https://yizhan.wiki/NitWikit/Java/advance/folia/"
cd /home
sudo ls -luah /home
exit 0