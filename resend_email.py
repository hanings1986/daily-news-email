#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新发送邮件 - 确认版本
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def resend_confirmation_email():
    """重新发送确认邮件"""
    
    # 邮件配置
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    sender_email = "289574795@qq.com"
    sender_password = "mwrihbpgxzeacbbg"
    recipient_email = "289574795@qq.com"
    
    try:
        print("📧 重新发送确认邮件...")
        
        # 连接服务器
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"✅ 重新发送确认 - {datetime.now().strftime('%H:%M:%S')}"
        
        # 邮件正文
        body = f"""
📬 邮件重发确认

这是第二次发送的确认邮件，用于验证邮件系统是否正常工作。

📋 邮件信息：
- 发送时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 发件人：{sender_email}
- 收件人：{recipient_email}
- 状态：重新发送确认

🎯 如果收到此邮件：
✅ 邮件系统配置完全正确
✅ 授权码验证通过
✅ 可以正常接收新闻摘要

📰 系统功能确认：
从明天开始，您将每天7:00自动收到：
- 最新的国际新闻摘要
- 15条重点新闻分析
- 财经市场动态
- 科技前沿进展

🔔 请回复此邮件确认收到，或直接在此对话中告知。

---
国际新闻摘要系统
确认发送时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 发送邮件
        server.send_message(msg)
        server.quit()
        
        print("✅ 确认邮件已重新发送！")
        print("📬 请立即检查QQ邮箱")
        print("💡 邮件主题：'✅ 重新发送确认 - 当前时间'")
        
        return True
        
    except Exception as e:
        print(f"❌ 发送失败: {e}")
        return False

if __name__ == "__main__":
    print("📧 重新发送确认邮件")
    print("=" * 50)
    
    print("使用授权码：mwrihbpgxzeacbbg")
    print("目标邮箱：289574795@qq.com")
    print("\n开始发送...")
    
    success = resend_confirmation_email()
    
    if success:
        print("\n🎉 邮件已发送！请检查：")
        print("1. 收件箱")
        print("2. 垃圾邮件文件夹")
        print("3. 其他邮件文件夹")
        print("\n📋 如果收到，请在此确认")
        print("💡 如果未收到，可能是SMTP配置问题")
    else:
        print("\n❌ 发送失败，需要检查SMTP配置")