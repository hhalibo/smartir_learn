import os
import json
import re

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

# 检查是否是有效的指令，去掉前后空格后排除纯数字和小数
def is_valid_key(key):
    key = key.strip()  # 去掉前后空格
    
    # 排除纯数字和小数（包括负数）
    if re.match(r'^-?\d+(\.\d+)?$', key):  # 匹配数字或小数
        return False
    
    # 确保有字母字符
    if not re.search(r'[a-zA-Z]', key):
        return False
    
    return True

# 合并类似position 1, position 2为position，并忽略大小写
def merge_similar_keys(keys):
    merged_keys = set()
    for key in keys:
        # 使用正则表达式提取单词部分，去掉尾部的数字部分，并转换为小写
        base_key = re.sub(r'\s*\d+$', '', key).strip().lower()
        merged_keys.add(base_key)
    return merged_keys

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
    
    # 排除无效的指令（去掉前后空格后，排除数字和小数）
    filtered_result = [key for key in result if is_valid_key(key)]
    
    # 合并类似position 1, position 2为position，并忽略大小写
    merged_result = merge_similar_keys(filtered_result)
    
    # 将结果排序后逐行打印
    for key in sorted(merged_result):
        print(key)

if __name__ == '__main__':
    main()
