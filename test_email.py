#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试邮件发送功能
简化版本，便于配置和测试
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_test_email():
    """发送测试邮件"""
    
    # 收件人邮箱（您的QQ邮箱）
    recipient_email = "289574795@qq.com"
    
    # 邮件配置 - 已配置
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    sender_email = "289574795@qq.com"  # 您的QQ邮箱
    sender_password = "cboygbinfhtxcbbh"      # 您的授权码
    
    try:
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"📧 测试邮件 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        # 邮件正文
        body = f"""
您好！

这是一封来自国际新闻摘要系统的测试邮件。

如果收到此邮件，说明邮件配置成功！

📰 系统功能：
- 每天7:00自动收集国际新闻
- 生成分类摘要报告
- 自动发送到您的邮箱

⏰ 发送时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---
国际新闻摘要系统
自动发送
"""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 发送邮件
        print("🔗 正在连接邮件服务器...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        print("🔐 正在登录邮箱...")
        server.login(sender_email, sender_password)
        print("📤 正在发送邮件...")
        server.send_message(msg)
        server.quit()
        
        print(f"✅ 测试邮件已成功发送到 {recipient_email}")
        return True
        
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        print("\n💡 配置说明：")
        print("1. 请确保已正确配置QQ邮箱SMTP信息")
        print("2. 需要获取QQ邮箱的授权码（不是登录密码）")
        print("3. 授权码获取方法：QQ邮箱设置 → 账户 → POP3/SMTP服务 → 开启")
        print("4. 修改 test_email.py 中的 sender_email 和 sender_password")
        return False

if __name__ == "__main__":
    print("📧 测试邮件发送工具")
    print("=" * 50)
    
    # 显示当前配置
    print("当前配置：")
    print(f"收件人: 289574795@qq.com")
    print(f"发送邮箱: 289574795@qq.com")
    print(f"授权码: 已配置")
    print("\n开始发送测试邮件...")
    
    # 发送测试邮件
    send_test_email()