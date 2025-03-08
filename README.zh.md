
# HomeAssistant SmartIR 配置生成插件

**中文** | [English](README.md)

本插件用于简化SmartIR配置文件的生成流程，通过博联（Broadlink）设备学习红外指令并自动生成兼容SmartIR的JSON配置文件。

<img width="1206" alt="image" src="https://github.com/user-attachments/assets/466b3252-edea-4cac-b28e-cbb9f3840397" />

<img width="616" alt="image" src="https://github.com/user-attachments/assets/4bc2f01e-ab18-4f2b-a6db-5029106fe102" />


## 功能特性

- 🎯 **设备支持**：支持空调（climate）、电视（TV）、风扇（fan）等设备类型
- 📁 **模板系统**：提供预置模板文件，支持自定义模板导入
- 🌡️ **温度控制**：空调设备支持自定义温度范围（16-32℃）
- 📶 **红外学习**：通过博联设备直接学习红外指令
- 🧪 **指令测试**：支持学习后指令验证功能
- 🚀 **一键生成**：自动生成符合SmartIR标准的配置文件

## 安装步骤

### 方式一：通过 HACS 安装（推荐）
1. **安装 HACS**  
   如果尚未安装 HACS，请先参考[官方文档](https://hacs.xyz/docs/setup/download)进行安装

2. **添加自定义仓库**
   - 进入 HACS 页面
   - 点击右上角 `⋮` ➡️ **自定义仓库**
   - 输入仓库 URL：`https://github.com/Seifon/smartir_learn`
   - 分类选择 **集成**

3. **安装插件**
   - 在 HACS 的 **集成** 页面搜索 "SmartIR学码"
   - 点击进入插件页面 ➡️ **下载**
   - 等待下载完成后重启 HomeAssistant

### 方式二：手动安装
1. 将插件文件夹 `smartir_learn` 复制到 HomeAssistant 的 `custom_components` 目录
2. 重启 HomeAssistant 服务

### 初始化配置
1. 进入 **配置 -> 设备与服务 -> 集成**
2. 点击右下角 "+添加集成"
3. 搜索选择 "SmartIR Learn"


## 配置指南

### 第一步：设备连接
<img width="415" alt="image" src="https://github.com/user-attachments/assets/7815a7c0-244d-48cd-ad4f-03964f571843" />

- 选择设备发现方式：
  - `自动扫描`：自动搜索局域网内博联设备
  - `手动输入`：直接输入设备IP地址

### 第二步：点击配置按钮，进入设备选择
<img width="409" alt="image" src="https://github.com/user-attachments/assets/c377c521-2995-4969-b0f7-f63f9d2d0c43" />

<img width="403" alt="image" src="https://github.com/user-attachments/assets/b19309d6-d21d-4049-abdd-003c3d7a7419" />


### 第三步：指令学习
<img width="408" alt="image" src="https://github.com/user-attachments/assets/b4a25fa8-5fb8-4874-ba29-93c4ccbf3386" />

1. 从模板选择要学习的指令
2. 按提示使用遥控器发送红外信号
3. 自动保存学习到的指令代码

### 第四步：配置文件生成
生成的文件路径示例：
```bash
/config/custom_components/smartir/codes/climate/202503091445.json
```

## 使用方法

2. 配置SmartIR实体：
   ```yaml
   climate:
     - platform: smartir
       name: Living Room AC
       unique_id: living_ac
       device_code: 202503091445
       controller_data: broadlink_remote_entity_id
   ```

## 注意事项

⚠️ **设备准备**：
- 确保博联设备与HomeAssistant在同一局域网
- 在博联APP中关闭"设备锁定"功能
- 提前安装好SmartIR插件

🔧 **故障排查**：
```python
常见错误处理：
1. 连接超时 → 检查设备IP和网络连接
2. 学习失败 → 确保遥控器对准设备（距离<5cm）
3. 文件保存失败 → 验证目录写入权限
```

🔄 **模板开发**：
支持自定义模板开发，存放到template目录的对应设备类型下，模板文件结构示例：
```json
{
  "manufacturer": "Manufacturer Name",
  "supportedModels": ["Model A", "Model B"],
  "commands": {
    "power": "JgASKE5MTk..."
  }
}
```

## 技术支持

如遇使用问题，请提供以下信息：
1. HomeAssistant 版本
2. 博联设备型号
3. 错误日志片段
4. 相关配置文件（脱敏后）

---

✅ 测试版本：HomeAssistant 2025.2.0
📜 许可证：MIT License
