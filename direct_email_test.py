#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接邮件测试 - 简化版本
"""

import smtplib
from email.mime.text import MIMEText

def send_direct_email():
    """直接发送测试邮件"""
    
    # 使用您提供的授权码
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    sender_email = "289574795@qq.com"
    sender_password = "mwrihbpgxzeacbbg"  # 您提供的新授权码
    recipient_email = "289574795@qq.com"
    
    try:
        print("🔄 尝试发送测试邮件...")
        
        # 创建简单邮件
        msg = MIMEText("这是一封测试邮件，用于验证邮件发送功能。", 'plain', 'utf-8')
        msg['Subject'] = '测试邮件 - 请确认收到'
        msg['From'] = sender_email
        msg['To'] = recipient_email
        
        # 连接并发送
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        print("✅ 邮件发送完成！")
        print("📬 请检查您的QQ邮箱收件箱")
        print("💡 如果没看到，请检查垃圾邮件文件夹")
        return True
        
    except Exception as e:
        print(f"❌ 发送失败: {e}")
        
        # 提供具体解决方案
        if "Authentication" in str(e):
            print("\n🔧 解决方案：")
            print("1. 登录QQ邮箱 → 设置 → 账户")
            print("2. 找到'POP3/IMAP/SMTP服务'")
            print("3. 确认已开启该服务")
            print("4. 如果未开启，请开启并获取新授权码")
            print("5. 如果已开启，可能需要重新获取授权码")
        
        return False

if __name__ == "__main__":
    print("📧 直接邮件测试")
    print("=" * 50)
    
    success = send_direct_email()
    
    if not success:
        print("\n💡 建议操作：")
        print("1. 确认SMTP服务已正确开启")
        print("2. 重新获取授权码")
        print("3. 或者使用桌面版文件（已生成）")