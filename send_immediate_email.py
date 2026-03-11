#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
立即发送邮件 - 使用新授权码
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

def send_immediate_email():
    """立即发送邮件"""
    
    # 邮件配置 - 使用新授权码
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    sender_email = "289574795@qq.com"
    sender_password = "mwrihbpgxzeacbbg"  # 新授权码
    recipient_email = "289574795@qq.com"
    
    try:
        print("📧 开始发送邮件...")
        print("🔗 连接SMTP服务器...")
        
        # 连接服务器
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        
        print("🔐 启动TLS加密...")
        server.starttls()
        
        print("🔑 登录邮箱...")
        server.login(sender_email, sender_password)
        print("✅ 登录成功！")
        
        # 创建邮件
        print("📝 创建邮件内容...")
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"🎉 邮件测试成功 - {datetime.now().strftime('%H:%M:%S')}"
        
        # 邮件正文
        body = f"""
🎊 恭喜！邮件配置测试成功！

📧 邮件信息：
- 发件人：{sender_email}
- 收件人：{recipient_email}
- 发送时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

✅ 这封邮件证明：
- SMTP服务配置正确
- 授权码验证通过
- 邮件发送功能正常

📰 新闻摘要系统功能：
- 每天7:00自动收集国际新闻
- 生成分类摘要报告
- 自动发送到您的邮箱
- 支持多种新闻源整合

🔔 后续服务：
从明天开始，您将每天7:00收到最新的国际新闻摘要！

---
国际新闻摘要系统
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 发送邮件
        print("📤 发送邮件...")
        server.send_message(msg)
        
        print("🔚 断开连接...")
        server.quit()
        
        print("\n🎉 邮件发送成功！")
        print("📬 请立即检查您的QQ邮箱")
        print("💡 如果没看到邮件，请检查：")
        print("   - 收件箱")
        print("   - 垃圾邮件文件夹")
        print("   - 其他文件夹")
        
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"\n❌ 邮箱认证失败: {e}")
        print("\n🔧 可能的原因：")
        print("1. 授权码错误")
        print("2. SMTP服务未正确开启")
        print("3. 需要重新获取授权码")
        
    except Exception as e:
        print(f"\n❌ 发送失败: {type(e).__name__}: {e}")
    
    return False

if __name__ == "__main__":
    print("📧 立即邮件发送测试")
    print("=" * 50)
    
    print("使用新授权码：mwrihbpgxzeacbbg")
    print("\n开始发送测试邮件...")
    
    success = send_immediate_email()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ 邮件系统配置完成！")
        print("📰 新闻摘要服务已就绪")
        print("⏰ 明天7:00将自动发送最新新闻摘要")
    else:
        print("\n" + "=" * 50)
        print("❌ 需要重新配置SMTP服务")
        print("💡 请确认SMTP服务已正确开启")