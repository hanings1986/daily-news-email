#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
交互式邮件测试脚本
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

def test_email_with_input():
    """交互式邮件测试"""
    print("📧 交互式邮件测试")
    print("=" * 50)
    
    # 获取用户输入的授权码
    print("\n请输入您的QQ邮箱授权码：")
    auth_code = input("授权码: ").strip()
    
    if not auth_code:
        print("❌ 授权码不能为空")
        return False
    
    # 邮件配置
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    sender_email = "289574795@qq.com"
    sender_password = auth_code
    recipient_email = "289574795@qq.com"
    
    try:
        print("\n🔗 连接SMTP服务器...")
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
        msg['Subject'] = "✅ 邮件配置测试成功"
        
        body = """
🎉 恭喜！您的邮件配置测试成功！

这封邮件说明：
✅ SMTP服务已正确开启
✅ 授权码配置正确
✅ 邮件发送功能正常

📰 新闻摘要系统现在可以正常工作，每天7:00会自动发送新闻摘要到您的邮箱。

如有任何问题，请随时联系系统管理员。

---
国际新闻摘要系统
测试时间：当前时间
"""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        print("📤 发送邮件...")
        server.send_message(msg)
        
        print("🔚 断开连接...")
        server.quit()
        
        print("\n🎉 测试邮件发送成功！")
        print("📬 请检查您的QQ邮箱收件箱")
        print("💡 如果没看到邮件，请检查垃圾邮件文件夹")
        
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"\n❌ 邮箱认证失败: {e}")
        print("\n💡 可能的原因：")
        print("1. 授权码错误")
        print("2. SMTP服务未开启")
        print("3. 需要重新获取授权码")
        
    except Exception as e:
        print(f"\n❌ 发送失败: {type(e).__name__}: {e}")
    
    return False

def show_smtp_guide():
    """显示SMTP配置指南"""
    print("\n" + "=" * 50)
    print("🔧 SMTP服务配置指南")
    print("=" * 50)
    
    print("\n📋 配置步骤：")
    print("1. 登录QQ邮箱 (mail.qq.com)")
    print("2. 进入'设置' → '账户'")
    print("3. 找到'POP3/IMAP/SMTP服务'")
    print("4. 点击'开启'（如果已开启，先关闭再重新开启）")
    print("5. 按照提示获取新的16位授权码")
    print("6. 使用新授权码重新测试")
    
    print("\n⚠️ 重要提示：")
    print("- 授权码不同于登录密码")
    print("- 开启SMTP服务后需要重新获取授权码")
    print("- 授权码格式：16位字母组合")

if __name__ == "__main__":
    # 先显示配置指南
    show_smtp_guide()
    
    # 询问是否开始测试
    input("\n按回车键开始邮件测试...")
    
    # 执行测试
    success = test_email_with_input()
    
    if not success:
        print("\n" + "=" * 50)
        print("❌ 测试失败，请按指南重新配置SMTP服务")
        print("然后重新运行此脚本进行测试")
    else:
        print("\n" + "=" * 50)
        print("✅ 配置完成！新闻摘要系统已就绪")
        print("每天7:00会自动发送新闻摘要到您的邮箱")