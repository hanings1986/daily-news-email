#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用SSL端口配置发送邮件
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_ssl_email():
    """使用SSL端口发送邮件"""
    
    # 邮件配置 - 使用SSL端口
    smtp_server = "smtp.qq.com"
    smtp_port = 465  # SSL端口
    sender_email = "289574795@qq.com"
    sender_password = "mwrihbpgxzeacbbg"
    recipient_email = "289574795@qq.com"
    
    try:
        print("🔐 使用SSL端口发送邮件...")
        print(f"服务器: {smtp_server}:{smtp_port}")
        
        # 创建SSL上下文
        context = ssl.create_default_context()
        
        # 使用SSL连接
        print("🔗 建立SSL连接...")
        server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context, timeout=10)
        
        print("🔑 登录邮箱...")
        server.login(sender_email, sender_password)
        print("✅ 登录成功！")
        
        # 创建邮件
        print("📝 创建邮件内容...")
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"🔐 SSL测试邮件 - {datetime.now().strftime('%H:%M:%S')}"
        
        # 邮件正文
        body = f"""
🔐 SSL端口配置测试成功！

📋 连接信息：
- 服务器：smtp.qq.com:465 (SSL)
- 发送时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 加密方式：SSL/TLS

✅ 这证明：
- SSL端口配置正确
- 第三方客户端设置验证通过
- 邮件系统完全正常

📰 新闻摘要系统确认：
使用正确的第三方客户端配置，系统可以：
- 每天7:00自动发送新闻摘要
- 使用SSL加密确保安全
- 稳定可靠地提供服务

💡 配置说明（供参考）：
发送服务器：smtp.qq.com
端口：465 (SSL) 或 587 (STARTTLS)
用户名：289574795@qq.com
密码：授权码（不是QQ密码）

---
国际新闻摘要系统
SSL连接测试成功
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 发送邮件
        print("📤 发送邮件...")
        server.send_message(msg)
        
        print("🔚 断开连接...")
        server.quit()
        
        print("\n🎉 SSL邮件发送成功！")
        print("📬 请检查QQ邮箱")
        print("💡 邮件主题：'🔐 SSL测试邮件 - 当前时间'")
        
        return True
        
    except Exception as e:
        print(f"❌ SSL发送失败: {e}")
        
        # 尝试使用587端口（STARTTLS）
        print("\n🔄 尝试使用587端口（STARTTLS）...")
        return try_587_port()

def try_587_port():
    """尝试使用587端口（STARTTLS）"""
    
    smtp_server = "smtp.qq.com"
    smtp_port = 587  # STARTTLS端口
    sender_email = "289574795@qq.com"
    sender_password = "mwrihbpgxzeacbbg"
    recipient_email = "289574795@qq.com"
    
    try:
        print(f"尝试端口: {smtp_port} (STARTTLS)")
        
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        server.starttls()
        server.login(sender_email, sender_password)
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"🔐 STARTTLS测试邮件 - {datetime.now().strftime('%H:%M:%S')}"
        
        body = f"""
🔐 STARTTLS端口配置测试成功！

使用端口587 (STARTTLS) 发送的测试邮件。

发送时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---
国际新闻摘要系统
STARTTLS连接测试成功
"""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        server.send_message(msg)
        server.quit()
        
        print("✅ STARTTLS邮件发送成功！")
        return True
        
    except Exception as e:
        print(f"❌ STARTTLS发送失败: {e}")
        return False

if __name__ == "__main__":
    print("🔐 SSL端口邮件测试")
    print("=" * 50)
    
    print("配置信息：")
    print("用户名: 289574795@qq.com")
    print("密码: 授权码")
    print("服务器: smtp.qq.com")
    print("端口: 465 (SSL) 或 587 (STARTTLS)")
    print("\n开始测试...")
    
    success = send_ssl_email()
    
    if success:
        print("\n🎉 邮件发送成功！")
        print("📋 请检查邮箱并确认收到")
    else:
        print("\n❌ 所有端口测试失败")
        print("💡 可能需要检查SMTP服务状态")