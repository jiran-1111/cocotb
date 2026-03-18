## comopy的接口说明

### 赋值

定义位置: comopy/hdl/signal.py 中 Signal.__itruediv__

使用：Signal.assign(value)  或 /=

### 取值

定义位置: comopy/hdl/signal.py  中 Signal.data_bits

使用：

signal.data_bits_unsigned()获取整数

signal.data_bits.bin() 获取二进制字符串

### 获取信号位宽

定义位置: comopy/hdl/signal.py 中 Signal.nbits 

使用：Signal.nbits 

### 获取I/O方向

定义位置: comopy/hdl/signal.py 中 Signal.direction

使用：Signal.direction

### 仿真器入口

定义位置：comopy/sim/xxx_simulator.py

使用：Simulator.start()

### 仿真器退出

使用：Simulator.stop()

### 组合逻辑计算

定义位置: comopy/sim/event_simulator.py 中 evaluate()

使用: 每次 cocotb 修改信号值后，必须调用 sim.evaluate() 才能看到输出信号的变化

### 时序推进

定义位置: comopy/sim/event_simulator.py 中 tick()

使用：Simulator.tick()

### 遍历所有信号

定义位置：comopy/hdl/raw_module.py 中 RawModule.all_ports()

使用：RawModule.all_ports()


