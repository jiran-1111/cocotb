import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_only_timer(dut):
    print("--- [Test] Start! Waiting for 5ns... ---")
    
    # 核心测试：如果这个 await 能回来，说明注入成功了
    await Timer(5, unit="ns")
    
    print("--- [Test] Successfully resumed after Timer! ---")

