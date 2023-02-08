# abd-helper

## aobi-java
fake 某个辅助的验证码请求.

## aobi-python
自动钓鱼  

### 环境配置
1. Python3 
2. openvc(pip install opencv-contrib-python)
3. 修改 adb.py 文件 第10行 ADB_ROOT 路径(该文件夹的绝对路径即可)
4. 修改 雷电模拟器 的分辨率为 1920*1080
5. 在 aobi-python 文件下执行 adb.exe connect 127.0.0.1:7555
6. 在 aobi-python 文件下执行 python adb.py 查看是否环境是否正确
7. 将连点器脚本(掉到鱼王使用)传到模拟器中 adb.exe push tap.mks /storage/emulated/0/data (备注: /storage/emulated/0为内部存储设备路径, adb.exe 和 tap.mks是在相同目录, 所以直接使用)


### 使用
1. 在 aobi-python 文件下执行 adb.exe connect 127.0.0.1:7555
2. 可重复执行, 直至显示 `already connected to 127.0.0.1:7555` 即可.
2. 在 aobi-python 文件下执行 python aobi.py

### 钓鱼位置
41行 click(1400, 669) 奥比森林下面钓鱼, 山顶钓鱼  
40行 click(541, 332) 奥比森森林水车那个位置钓鱼


### 延迟
延迟调整参数
