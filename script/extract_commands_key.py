import os
import json

# 用于递归提取commands字段下所有key的函数
def extract_keys(data, result=None):
    if result is None:
        result = set()  # 使用set来避免重复
    
    if isinstance(data, dict):  # 如果是字典类型
        for key, value in data.items():
            result.add(key)
            # 递归遍历嵌套的字典
            extract_keys(value, result)
    elif isinstance(data, list):  # 如果是列表类型
        for item in data:
            extract_keys(item, result)
    
    return result

def main():
    result = set()
    
    # 遍历当前目录下所有JSON文件
    for filename in os.listdir('.'):
        if filename.endswith('.json'):
            with open(filename, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    # 提取commands字段下的键
                    if 'commands' in data:
                        result.update(extract_keys(data['commands']))
                except json.JSONDecodeError:
                    print(f"无法解析文件 {filename}")
    
    # 将结果排序后逐行打印
    for key in sorted(result):
        print(key)

if __name__ == '__main__':
    main()
