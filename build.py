import os
import time
import shutil
import subprocess
from colorama import init, Fore, Style

# 初始化 colorama
init(autoreset=True)

# 定义颜色变量
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
PINK = Fore.MAGENTA
RES = Style.RESET_ALL

filepath = os.path.dirname(os.path.realpath(__file__))

def run_command(command):
    result = subprocess.run(command, shell=True, text=True)
    return result

# 删除不需要的文件和文件夹
def remove_if_exists(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

def main():
    mynameis = os.getlogin()

    # 删除之前的文件
    remove_if_exists(os.path.join(filepath, 'jdk-21_windows-x64_bin.zip'))
    remove_if_exists(os.path.join(filepath, 'Folia'))
    remove_if_exists(os.path.join(filepath, 'gradle'))
    
    print(f"{BLUE}------------------------------------------------------------------------------------------{RES}")
    print("Folia 是 Paper 的一个分支,由 Minecraft 优化 BOSS Spottedleaf 开发。有多线程优化")
    print(f"{GREEN}这是一个半自动Folia核心编译脚本，只提供最新版本编译，编译期间不要关闭您的命令行窗口，注意窗口保持连接！{RES}")
    print("作者：Chai https://github.com/chaichaisi/ https://space.bilibili.com/2018774790")
    print("作者：XiaoMing5442 https://github.com/XiaoMing5442/ https://space.bilibili.com/455779705")
    print(f"{RED}如果你中途输入错误，请使用 Ctrl + C 重新运行脚本！编译过程中不可轻易结束进程！会变得不幸！！！{RES}")
    setupmode = input("即将开始编译，请准备Github中的用户名以及邮箱，注意大小写和中文与英文字符！[Y/n]: ")
    
    if setupmode.lower() in ['n', 'no']:
        print("用户拒绝，正在退出，请重新运行脚本，执行到上一步时请输入y或者Y同意运行！")
        time.sleep(3)
        return
    
    setupmode_realy = input(f"{RED}你{RES}{GREEN}真{RES}{PINK}的{RES}{YELLOW}准{RES}{BLUE}备{RES}{RED}好{RES}{BLUE}了{RES}{PINK}吗{RES}？[Y/n]: ")
    
    if setupmode_realy.lower() in ['n', 'no']:
        print("用户拒绝，正在退出，请重新运行脚本，执行到上一步时请输入y或者Y同意运行！")
        time.sleep(3)
        return
    
    username = input("[STEP 1/4]配置Git 请输入Github的用户名(username): ")
    email = input("[STEP 2/4]配置Git 请输入Github的邮箱(email): ")

    run_command(f'git config --global user.name "{username}"')
    run_command(f'git config --global user.email "{email}"')
    
    print(f"{GREEN}[STEP 3/4]开始编译Folia最新核心，请耐心等待！{RES}")
    print(f"读取用户名 : {username}")
    print(f"读取邮箱 : {email}")
    time.sleep(5)
    
    # 从 Oracle 下载 JDK 并解压
    jdk_url = "https://download.oracle.com/java/21/latest/jdk-21_windows-x64_bin.zip"
    jdk_zip_path = os.path.join(filepath, 'jdk-21_windows-x64_bin.zip')
    run_command(f'curl -o "{jdk_zip_path}" {jdk_url}')
    run_command(f'powershell -command "Expand-Archive -Path {jdk_zip_path} -DestinationPath {filepath}\\jdk-21"')
    
    # 设置 JAVA_HOME 环境变量
    java_home = os.path.join(filepath, 'jdk-21')
    os.environ["JAVA_HOME"] = java_home
    os.environ["PATH"] = f"{java_home}\\bin;" + os.environ["PATH"]

    # 克隆 Folia 源码并编译
    run_command(f'git clone https://github.com/PaperMC/Folia.git "{os.path.join(filepath, "Folia")}"')
    os.chdir(os.path.join(filepath, "Folia"))
    run_command('.\gradlew applyPatches')
    run_command('.\gradlew createMojmapBundlerJar')
    
    jar_files = [f for f in os.listdir(os.path.join(filepath, 'Folia', 'build', 'libs')) if f.endswith('.jar')]
    if jar_files:
        print(f"{GREEN}[STEP 4/4]恭喜，如果看到绿色字体SUCCESSFUL，代表着编译Folia核心是成功的！{RES}")
        for jar_file in jar_files:
            shutil.move(os.path.join(filepath, 'Folia', 'build', 'libs', jar_file), os.path.join(filepath, jar_file))
    else:
        print(f"{RED}有问题！文件夹中没有 .jar 文件。请重试或者提交完整日志给我们来帮助解决您的问题。{RES}")
        return
    
    print(f"自动为您切换到编译完产物目录，我们会为您全部移动到当前目录下！")
    print('大获全胜！已经结束，您可以找到您编译的Folia核心文件并使用它们。')
    print(f"项目地址 https://github.com/chaichaisi/folia-build-shell 能给个Star嘛")
    time.sleep(1)
    print('Done！ :)')
    print("Folia更多详情咨询：https://papermc.io/software/folia")
    print("https://yizhan.wiki/NitWikit/Java/advance/folia/")
    os.chdir(filepath)
    for f in os.listdir(filepath):
        print(f)

if __name__ == "__main__":
    main()
