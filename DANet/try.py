import os

try:
    # 打印当前工作目录
    print("当前工作目录:", os.getcwd())
    
    # 创建相对路径下的目录，无需转义
    os.makedirs('./aaa', exist_ok=True)
    
    print("目录 './aaa' 创建成功！")
except Exception as e:
    print(f"创建目录失败: {e}")