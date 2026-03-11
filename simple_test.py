#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单邮件测试脚本
"""

import smtplib
from email.mime.text import MIMEText

def test_simple_email():
    """发送最简单的测试邮件"""
    try:
        # 邮件配置
        smtp_server = "smtp.qq.com"
        smtp_port = 587
        sender_email = "289574795@qq.com"
        sender_password = "cboygbinfhtxcbbh"
        recipient_email = "289574795@qq.com"
        
        print("🔗 连接SMTP服务器...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        
        print("🔐 启动TLS加密...")
        server.starttls()
        
        print("🔑 登录邮箱...")
        server.login(sender_email, sender_password)
        
        print("📝 创建邮件内容...")
        subject = "简单测试邮件"
        body = "这是一封简单的测试邮件，用于验证邮件发送功能。"
        
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        
        print("📤 发送邮件...")
        server.sendmail(sender_email, recipient_email, msg.as_string())
        
        print("🔚 断开连接...")
        server.quit()
        
        print("✅ 邮件发送成功！")
        return True
        
    except Exception as e:
        print(f"❌ 发送失败: {type(e).__name__}: {e}")
        return False

if __name__ == "__main__":
    print("📧 简单邮件测试")
    print("=" * 50)
    test_simple_email()