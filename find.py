import cocotb
import os

# 1. 找到 cocotb 的安装路径
cocotb_path = os.path.dirname(cocotb.__file__)

# 2. simulator.so 的位置 (Python 调用的)
print("Simulator 模块:", os.path.join(cocotb_path, "simulator.so")) 
# (Windows 下是 simulator.cp310-win_amd64.pyd 这种格式)

# 3. 其他支持库和仿真器插件的位置
libs_path = os.path.join(cocotb_path, "libs")
print("库文件夹内容:", os.listdir(libs_path))