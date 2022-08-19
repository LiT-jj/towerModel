## 塔模型
简介：因为中文输入法下输入了tmx，所以它叫塔模型。
## 怎么使用？

### 环境安装
step.1 pip install pyautogui
step.2 pip install pywin32
step.3 pip install opencv-python
step.4 pip install xlrd==1.2

### 准备就绪
安装完之后, 就可以通过```python main.py```运行脚本啦

### 自定义xls脚本
每个excel文件有多张sheet，每张sheet有多行记录
在tmx里面，一个excel对应一个项目，一个sheet对应一座塔，sheet里面的一行记录对应塔里面的一层
每个sheet里面第一行记录必须是以下格式

| step | type | comment | wait_time | content |
| ---- | ---- | ------- | --------- | ------- |

step：步骤，必须严格按1，2，3，4...来填写，指令中的 ```if```、```jump``` 严格按照step来跳转

type：指令的类型，有if、jump、moveTo等等，后面会对每个指令的详细用法进行说明

comment：单步操作的含义，可以为空

wait_tiem：单步操作完成之后，下一步指令之前等待的时间。必须为数字类型

content：相当于每个指令的参数，具体怎么填写参考指令介绍部分

### 运行自定义脚本

在main.py文件中，修改  line 22的参数，如使用自定义xls脚本 cat.xls，则修改为`xls = r'bilibili.xls'`，脚本运行期间，全局监听Esc键的触发，按下Esc后，脚本等待一定时间后停止运行。

## 指令说明

### moveTo

顾名思义，moveTo指令含义是移动到指定位置。目前它接受两种类型的参数：

第一种：```image path,0.8```，例如```image img/chromeIcon.png,0.8```。这个指令包含两个基础步骤，1. 在桌面上定位图片 2.将鼠标移动到图片中心。0.8是图片的匹配程度，大于0.8才算定位成功

第二种：```pos x,y```，例如```pos -10,180```。这个指令的含义是将鼠标移动到指定位置。



### moveBy

格式：```pos x,y```

顾名思义，moveBy 是在当前坐标的基础上横坐标移动x像素，纵坐标移动y像素



### click

**格式**：```type time```

顾名思义，这个指令的就是告诉程序在当前位置点击



type支持的格式: left、right、mid

time支持的格式：1、2

例如：```left 1```代表鼠标左键点击一次

### if

**格式**：```condition1+condition2+condition3 step1 step2```

**含义**：在tmx中，类似于传送门的机制，符合条件传送到指定位置，否则传送到指定位置。condition代表一个条件，条件通过+连接，都满足将传送到 step1的位置，否则传送到step2的位置。condition目前支持图片和坐标的判断，图片判断含义是，windows窗口内如果有区域和指定图片匹配则满足条件；坐标判断含义是，当前光标如果在指定窗口内则满足条件

**图片判断格式**：image-image_path,confidence

**坐标判断格式**：pos-left,top,right,bottom

### jump

格式：n

含义：传送到指定层数

### scroll

格式：n

含义：滚轮滑动n像素

