# HomeAssistant SmartIR Configuration Generator

[中文](README.zh.md) | **English**

A plugin to simplify SmartIR configuration file generation, automating IR code learning through Broadlink devices.

<img width="1191" alt="image" src="https://github.com/user-attachments/assets/5f016d83-4216-4b31-9082-cb0032fd2560" />

<img width="616" alt="image" src="https://github.com/user-attachments/assets/4bc2f01e-ab18-4f2b-a6db-5029106fe102" />


## Features

- 🎯 **Device Support**: Climate, TV, Fan and other device types
- 📁 **Template System**: Pre-built templates & custom template support
- 🌡️ **Climate Control**: Customizable temperature range (16-32℃)
- 📶 **IR Learning**: Direct IR code acquisition via Broadlink devices
- 🧪 **Command Validation**: Post-learning command verification
- 🚀 **Auto-generation**: SmartIR-compatible JSON configuration output

## Installation

### Method 1: Via HACS (Recommended)
1. **Install HACS**  
   Follow [official guide](https://hacs.xyz/docs/setup/download) if not installed

2. **Add Custom Repository**
   - Open HACS ➡️ **Integrations**
   - Click `⋮` ➡️ **Custom repositories**
   - Add repository URL: `https://github.com/Seifon/smartir_learn`
   - Category: **Integration**

3. **Install Plugin**
   - Search "SmartIR Learn" in HACS Integrations
   - Click **Download**
   - Restart HomeAssistant after installation

### Method 2: Manual Installation
1. Copy `smartir_learn` folder to `custom_components` directory
2. Restart HomeAssistant

### Initial Setup
1. Navigate to **Configuration ➡️ Devices & Services ➡️ Integrations**
2. Click **+ Add Integration**
3. Search and select "SmartIR Learn"

![Setup Process](https://github.com/user-attachments/assets/7815a7c0-244d-48cd-ad4f-03964f571843)

## Configuration Guide

### Step 1: Device Connection
<img width="415" alt="Device Scanning" src="https://github.com/user-attachments/assets/7815a7c0-244d-48cd-ad4f-03964f571843" />

- Connection methods:
  - `Auto Scan`: Discover Broadlink devices in local network
  - `Manual Input`: Direct IP entry

### Step 2: Device Configuration
<img width="409" alt="Device Selection" src="https://github.com/user-attachments/assets/c377c521-2995-4969-b0f7-f63f9d2d0c43" />

```yaml
Sample Configuration:
device_type: climate
manufacturer: Midea
supported_models: MS-05A1
temperature_range: 16-30℃
```

### Step 3: IR Learning
<img width="408" alt="Command Learning" src="https://github.com/user-attachments/assets/b4a25fa8-5fb8-4874-ba29-93c4ccbf3386" />

1. Select commands from template
2. Follow on-screen instructions to send IR signals
3. Automatically save learned codes

### Step 4: Generate Configuration
Example output path:
```bash
/config/custom_components/smartir/codes/climate/202503091445.json
```

## Usage

1. Place generated JSON in SmartIR codes directory:
   ```bash
   cp 202503091445.json /config/custom_components/smartir/codes/climate/
   ```
2. Configure SmartIR entity:
   ```yaml
   climate:
     - platform: smartir
       name: Living Room AC
       unique_id: living_ac
       device_code: 202503091445
       controller_data: broadlink_remote_entity_id
   ```

## Important Notes

⚠️ **Prerequisites**:
- Broadlink device must be in same network as HA
- Disable 'Device Lock' in Broadlink APP
- SmartIR plugin must be pre-installed

🔧 **Troubleshooting**:
```python
Common solutions:
1. Connection timeout → Verify device IP and network
2. Learning failure → Ensure remote is <5cm from device
3. File save error → Check directory permissions
```

🔄 **Template Development**:
Sample template structure:
```json
{
  "manufacturer": "Manufacturer Name",
  "supportedModels": ["Model A", "Model B"],
  "commands": {
    "power": "JgASKE5MTk..."
  }
}
```

## Support

When reporting issues, please include:
1. HomeAssistant version
2. Broadlink device model
3. Error logs snippet
4. Relevant config files (sanitized)

---

✅ Tested Version: HomeAssistant 2025.2.0  
📜 License: MIT License
