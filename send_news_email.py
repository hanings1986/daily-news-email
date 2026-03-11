#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新闻摘要邮件发送脚本

使用说明：
1. 首先需要配置QQ邮箱的SMTP授权码
2. 将email_sender.py中的sender_password替换为实际授权码
3. 运行此脚本发送新闻摘要
"""

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime

def send_news_email():
    """发送新闻摘要邮件"""
    
    # 收件人邮箱
    recipient_email = "289574795@qq.com"
    
    # 查找最新的新闻摘要文件
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        print("❌ 报告目录不存在")
        return False
    
    files = [f for f in os.listdir(reports_dir) if f.endswith('.md') and '新闻摘要' in f]
    if not files:
        print("❌ 未找到新闻摘要文件")
        return False
    
    # 按修改时间排序，获取最新的文件
    files.sort(key=lambda x: os.path.getmtime(os.path.join(reports_dir, x)), reverse=True)
    latest_report = os.path.join(reports_dir, files[0])
    
    print(f"📧 正在发送新闻摘要: {latest_report}")
    
    try:
        # 读取新闻摘要内容
        with open(latest_report, 'r', encoding='utf-8') as file:
            report_content = file.read()
        
        # 提取标题和摘要信息用于邮件正文
        lines = report_content.split('\n')
        title = ""
        summary = ""
        for line in lines:
            if line.startswith('# ') and not title:
                title = line.replace('# ', '').strip()
            elif line.startswith('**生成时间**') and not summary:
                summary = line.replace('**生成时间**: ', '').strip()
                break
        
        # 邮件配置 - 已配置
        smtp_server = "smtp.qq.com"
        smtp_port = 587
        sender_email = "289574795@qq.com"  # 发送邮箱
        sender_password = "cboygbinfhtxcbbh"  # QQ邮箱授权码
        
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"📰 今日国际新闻摘要 - {datetime.now().strftime('%Y-%m-%d')}"
        
        # 邮件正文
        body = f"""
亲爱的用户：

这是您订阅的今日国际新闻摘要报告，请查收附件。

📊 报告概览：
- 报告标题: {title}
- 生成时间: {summary}
- 包含15条重点新闻分析

报告内容涵盖：
🌍 国际政治局势分析
💰 财经市场动态  
🔬 科技前沿进展
⚡ 风险提示和趋势预测

📎 附件包含完整的Markdown格式报告，可使用任何文本编辑器查看。

如有任何问题，请随时联系我们。

---
国际新闻摘要系统
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 添加附件
        with open(latest_report, 'rb') as file:
            attachment = MIMEApplication(file.read(), _subtype="md")
            attachment.add_header('Content-Disposition', 'attachment', 
                                filename=f"今日新闻摘要_{datetime.now().strftime('%Y%m%d')}.md")
            msg.attach(attachment)
        
        # 发送邮件
        print("🔗 正在连接邮件服务器...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        print("🔐 正在登录邮箱...")
        server.login(sender_email, sender_password)
        print("📤 正在发送邮件...")
        server.send_message(msg)
        server.quit()
        
        print(f"✅ 新闻摘要已成功发送到 {recipient_email}")
        return True
        
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        print("\n💡 配置说明：")
        print("1. 请确保已配置正确的QQ邮箱SMTP信息")
        print("2. 需要获取QQ邮箱的授权码而非登录密码")
        print("3. 授权码获取方法：QQ邮箱设置 → 账户 → POP3/SMTP服务 → 开启")
        return False

def create_config_guide():
    """创建配置指南文件"""
    guide_content = """# 📧 新闻摘要邮件发送配置指南

## 配置步骤

### 1. 获取QQ邮箱授权码
1. 登录QQ邮箱 (mail.qq.com)
2. 进入"设置" → "账户"
3. 找到"POP3/IMAP/SMTP服务"
4. 开启"POP3/SMTP服务"
5. 按照提示获取16位授权码

### 2. 修改邮件配置
在 `send_news_email.py` 文件中修改以下配置：

```python
# 邮件配置
smtp_server = "smtp.qq.com"
smtp_port = 587
sender_email = "你的QQ邮箱@qq.com"  # 替换为你的QQ邮箱
sender_password = "你的授权码"      # 替换为获取的授权码
```

### 3. 运行发送脚本
```bash
python send_news_email.py
```

## 安全提醒
- 授权码不同于登录密码
- 不要将授权码提交到代码仓库
- 建议使用环境变量存储敏感信息

## 自动发送设置
如需定时自动发送，可配置系统定时任务：

**Windows任务计划程序**：
1. 创建基本任务
2. 设置触发器为每天7:00
3. 操作为启动程序：`python send_news_email.py`

**Linux crontab**：
```bash
0 7 * * * cd /path/to/project && python send_news_email.py
```
"""
    
    with open("邮件发送配置指南.md", "w", encoding="utf-8") as f:
        f.write(guide_content)
    
    print("📖 已创建配置指南文件: 邮件发送配置指南.md")

if __name__ == "__main__":
    print("📰 新闻摘要邮件发送工具")
    print("=" * 50)
    
    # 检查是否需要配置指南
    if len(sys.argv) > 1 and sys.argv[1] == "--guide":
        create_config_guide()
    else:
        # 尝试发送邮件
        success = send_news_email()
        
        if not success:
            print("\n💡 运行以下命令获取详细配置指南：")
            print("python send_news_email.py --guide")