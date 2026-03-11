#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
邮件发送诊断脚本
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
import ssl

def diagnose_smtp():
    """诊断SMTP连接问题"""
    print("🔍 开始SMTP连接诊断...")
    
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    sender_email = "289574795@qq.com"
    sender_password = "cboygbinfhtxcbbh"
    
    try:
        # 1. 测试网络连接
        print("1. 测试网络连接...")
        socket.create_connection(("smtp.qq.com", 587), timeout=10)
        print("   ✅ 网络连接正常")
        
        # 2. 测试SMTP连接
        print("2. 测试SMTP连接...")
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        print("   ✅ SMTP连接成功")
        
        # 3. 测试STARTTLS
        print("3. 测试STARTTLS加密...")
        server.starttls()
        print("   ✅ STARTTLS成功")
        
        # 4. 测试登录
        print("4. 测试邮箱登录...")
        server.login(sender_email, sender_password)
        print("   ✅ 邮箱登录成功")
        
        # 5. 测试发送简单邮件
        print("5. 测试邮件发送...")
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = "289574795@qq.com"
        msg['Subject'] = "诊断测试邮件"
        msg.attach(MIMEText("这是一封诊断测试邮件。", 'plain', 'utf-8'))
        
        server.send_message(msg)
        print("   ✅ 邮件发送成功")
        
        server.quit()
        print("\n🎉 所有诊断测试通过！邮件应该已发送成功。")
        return True
        
    except socket.timeout:
        print("   ❌ 网络连接超时，请检查网络")
    except socket.gaierror as e:
        print(f"   ❌ DNS解析失败: {e}")
    except smtplib.SMTPConnectError as e:
        print(f"   ❌ SMTP连接失败: {e}")
    except smtplib.SMTPAuthenticationError as e:
        print(f"   ❌ 邮箱认证失败: {e}")
        print("     可能原因：授权码错误或未开启SMTP服务")
    except smtplib.SMTPSenderRefused as e:
        print(f"   ❌ 发件人被拒绝: {e}")
    except smtplib.SMTPRecipientsRefused as e:
        print(f"   ❌ 收件人被拒绝: {e}")
    except ssl.SSLError as e:
        print(f"   ❌ SSL加密错误: {e}")
    except Exception as e:
        print(f"   ❌ 未知错误: {type(e).__name__}: {e}")
    
    return False

def check_authorization_code():
    """检查授权码配置"""
    print("\n🔑 检查授权码配置...")
    
    # 授权码特征检查
    auth_code = "cboygbinfhtxcbbh"
    
    if len(auth_code) != 16:
        print(f"   ❌ 授权码长度错误: {len(auth_code)}位 (应为16位)")
        return False
    
    if not auth_code.isalpha():
        print(f"   ❌ 授权码包含非字母字符")
        return False
    
    print(f"   ✅ 授权码格式正确: {len(auth_code)}位字母组合")
    return True

def verify_smtp_service():
    """验证SMTP服务是否开启"""
    print("\n📧 验证SMTP服务状态...")
    print("请确认以下步骤：")
    print("1. 登录QQ邮箱 (mail.qq.com)")
    print("2. 进入'设置' → '账户'")
    print("3. 找到'POP3/IMAP/SMTP服务'")
    print("4. 确认已开启'POP3/SMTP服务'")
    print("5. 如果未开启，请开启并获取新的授权码")
    print("\n💡 如果SMTP服务未开启，需要重新获取授权码")
    return True

if __name__ == "__main__":
    print("📧 邮件发送问题诊断")
    print("=" * 50)
    
    # 执行诊断
    auth_check = check_authorization_code()
    smtp_check = diagnose_smtp()
    
    if not smtp_check:
        verify_smtp_service()
        
    print("\n" + "=" * 50)
    print("📋 诊断结果：")
    
    if auth_check and smtp_check:
        print("✅ 所有诊断通过，邮件应该已发送成功")
        print("\n💡 如果仍未收到邮件，请检查：")
        print("1. 垃圾邮件文件夹")
        print("2. 邮箱容量是否已满")
        print("3. 网络连接状态")
    else:
        print("❌ 发现配置问题，请按提示修复")
        print("\n🔧 常见问题解决方法：")
        print("1. 确认SMTP服务已开启")
        print("2. 重新获取授权码")
        print("3. 检查网络连接")