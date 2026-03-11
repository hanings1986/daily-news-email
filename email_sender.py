import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from datetime import datetime
import config

def send_news_summary_email(recipient_email, report_file_path):
    """
    发送新闻摘要邮件到指定邮箱
    
    Args:
        recipient_email: 收件人邮箱
        report_file_path: 新闻摘要文件路径
    """
    try:
        # 读取新闻摘要内容
        with open(report_file_path, 'r', encoding='utf-8') as file:
            report_content = file.read()
        
        # 邮件配置
        smtp_server = "smtp.qq.com"
        smtp_port = 587
        sender_email = "289574795@qq.com"  # 发送邮箱
        sender_password = "your_password_here"  # 需要替换为实际授权码
        
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"📰 今日国际新闻摘要 - {datetime.now().strftime('%Y-%m-%d')}"
        
        # 邮件正文
        body = f"""
亲爱的用户：

这是您订阅的今日国际新闻摘要报告，请查收附件。

报告包含：
- 今日新闻概览和分类分布
- 重点新闻详细分析
- 新闻趋势和风险评估

如有任何问题，请随时联系我们。

---
自动发送系统
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 添加附件
        with open(report_file_path, 'rb') as file:
            attachment = MIMEApplication(file.read(), _subtype="md")
            attachment.add_header('Content-Disposition', 'attachment', 
                                filename=f"今日新闻摘要_{datetime.now().strftime('%Y%m%d')}.md")
            msg.attach(attachment)
        
        # 发送邮件
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ 新闻摘要已成功发送到 {recipient_email}")
        return True
        
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        return False

def send_email_with_text_only(recipient_email, subject, content):
    """
    发送纯文本邮件
    
    Args:
        recipient_email: 收件人邮箱
        subject: 邮件主题
        content: 邮件内容
    """
    try:
        # 邮件配置
        smtp_server = "smtp.qq.com"
        smtp_port = 587
        sender_email = "289574795@qq.com"  # 发送邮箱
        sender_password = "your_password_here"  # 需要替换为实际授权码
        
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        
        # 发送邮件
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ 邮件已成功发送到 {recipient_email}")
        return True
        
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        return False

def send_todays_news_summary():
    """发送今日新闻摘要邮件"""
    # 查找最新的新闻摘要文件
    reports_dir = "reports"
    if os.path.exists(reports_dir):
        files = [f for f in os.listdir(reports_dir) if f.endswith('.md') and '新闻摘要' in f]
        if files:
            # 按修改时间排序，获取最新的文件
            files.sort(key=lambda x: os.path.getmtime(os.path.join(reports_dir, x)), reverse=True)
            latest_report = os.path.join(reports_dir, files[0])
            
            print(f"📧 正在发送新闻摘要: {latest_report}")
            return send_news_summary_email("289574795@qq.com", latest_report)
        else:
            print("❌ 未找到新闻摘要文件")
            return False
    else:
        print("❌ 报告目录不存在")
        return False

if __name__ == "__main__":
    # 直接发送今日新闻摘要
    send_todays_news_summary()