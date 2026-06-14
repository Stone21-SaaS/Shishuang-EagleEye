# 石霜鹰眼 (Shishuang EagleEye) 🦅

**内核级安全监控系统 | Kernel-Level Security Monitoring System**

---
## 🌟 项目愿景
石霜鹰眼致力于为开发者提供一个**高效、稳定、可扩展**的内核级安全监控工具。
我们相信：“让安全变得简单，让监控变得优雅。”

---
## 📦 功能特性
- **高并发异步扫描引擎**
- **优雅的信号处理（SIGTERM）**
- **双重验证（ICMP + TCP SYN）**
- **CIDR 扩展逻辑**

---
## 🛠️ 快速开始
### 依赖
- Python 3.8+
- Linux 内核 4.15+

### 安装
```bash
git clone https://github.com/Stone21-SaaS/Shishuang-EagleEye.git
cd Shishuang-EagleEye
pip install -r requirements.txt
```

### 使用
```bash
python src/main.py --target 192.168.1.0/24
```

---
## 📜 许可证
本项目采用 **GPL-3.0** 许可证。

---
## 🤝 贡献指南
欢迎提交 Issue 或 PR！请遵循我们的 [贡献指南](CONTRIBUTING.md)。
