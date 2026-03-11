#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
发送所有邮件：测试邮件 + 新闻摘要邮件
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
import os

def send_email(subject, body, attachment_path=None):
    """通用邮件发送函数"""
    recipient_email = "289574795@qq.com"
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    sender_email = "289574795@qq.com"
    sender_password = "cboygbinfhtxcbbh"
    
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, 'rb') as file:
                attachment = MIMEApplication(file.read(), _subtype="md")
                filename = os.path.basename(attachment_path)
                attachment.add_header('Content-Disposition', 'attachment', filename=filename)
                msg.attach(attachment)
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        return True
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        return False

def send_test_email():
    """发送测试邮件"""
    subject = f"📧 测试邮件 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
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
    
    print("📧 正在发送测试邮件...")
    if send_email(subject, body):
        print("✅ 测试邮件发送成功！")
        return True
    else:
        print("❌ 测试邮件发送失败")
        return False

def send_news_summary():
    """发送新闻摘要邮件"""
    # 查找最新的新闻摘要文件
    reports_dir = "reports"
    if os.path.exists(reports_dir):
        files = [f for f in os.listdir(reports_dir) if f.endswith('.md') and '新闻摘要' in f]
        if files:
            files.sort(key=lambda x: os.path.getmtime(os.path.join(reports_dir, x)), reverse=True)
            latest_report = os.path.join(reports_dir, files[0])
            
            # 读取报告内容
            with open(latest_report, 'r', encoding='utf-8') as file:
                report_content = file.read()
            
            # 提取标题和摘要
            lines = report_content.split('\n')
            title = ""
            summary = ""
            for line in lines:
                if line.startswith('# ') and not title:
                    title = line.replace('# ', '').strip()
                elif line.startswith('**生成时间**') and not summary:
                    summary = line.replace('**生成时间**: ', '').strip()
                    break
            
            subject = f"📰 {title} - {datetime.now().strftime('%Y-%m-%d')}"
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

📎 附件包含完整的Markdown格式报告。

---
国际新闻摘要系统
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
            
            print(f"📰 正在发送新闻摘要: {latest_report}")
            if send_email(subject, body, latest_report):
                print("✅ 新闻摘要邮件发送成功！")
                return True
            else:
                print("❌ 新闻摘要邮件发送失败")
                return False
        else:
            print("❌ 未找到新闻摘要文件")
            return False
    else:
        print("❌ 报告目录不存在")
        return False

if __name__ == "__main__":
    print("📧 邮件发送系统启动")
    print("=" * 50)
    
    # 发送测试邮件
    print("\n1. 发送测试邮件...")
    test_success = send_test_email()
    
    # 发送新闻摘要邮件
    print("\n2. 发送新闻摘要邮件...")
    news_success = send_news_summary()
    
    print("\n" + "=" * 50)
    print("📋 发送结果汇总：")
    print(f"测试邮件: {'✅ 成功' if test_success else '❌ 失败'}")
    print(f"新闻摘要: {'✅ 成功' if news_success else '❌ 失败'}")
    
    if test_success and news_success:
        print("\n🎉 所有邮件发送完成！请检查您的邮箱。")
    else:
        print("\n⚠️ 部分邮件发送失败，请检查配置。")