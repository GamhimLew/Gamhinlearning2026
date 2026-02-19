"""
Knowledge Daily - 邮件发送脚本
用于 GitHub Actions 定时发送邮件
"""

import os
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from pathlib import Path


def load_config():
    """加载配置文件"""
    config_path = Path(__file__).parent.parent / "config" / "subjects.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_pending_email():
    """加载待发送的邮件内容"""
    content_path = Path(__file__).parent.parent / "content" / "pending_email.md"
    if not content_path.exists():
        raise FileNotFoundError("没有找到待发送的邮件内容，请先生成内容！")
    
    with open(content_path, "r", encoding="utf-8") as f:
        return f.read()


def markdown_to_html(md_content):
    """
    将 Markdown 转换为 HTML
    """
    try:
        import markdown
        html = markdown.markdown(
            md_content,
            extensions=['tables', 'fenced_code', 'nl2br']
        )
    except ImportError:
        # 如果没有安装 markdown 库，使用简单的替换
        html = md_content.replace('\n', '<br>')
    
    # 包装成完整的 HTML 文档
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.8;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background: #f5f5f5;
            }}
            .container {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            h1 {{ 
                color: #2c3e50; 
                border-bottom: 3px solid #3498db; 
                padding-bottom: 15px; 
                font-size: 28px;
            }}
            h2 {{ 
                color: #2980b9; 
                margin-top: 40px; 
                padding: 10px 0;
                border-left: 4px solid #3498db;
                padding-left: 15px;
            }}
            h3 {{ 
                color: #27ae60; 
                font-size: 20px;
            }}
            h4 {{ 
                color: #8e44ad; 
                font-size: 16px;
                margin-top: 25px;
            }}
            blockquote {{
                border-left: 4px solid #3498db;
                padding: 15px 20px;
                color: #555;
                margin: 20px 0;
                background: linear-gradient(to right, #e8f4f8, #fff);
                border-radius: 0 8px 8px 0;
            }}
            code {{
                background: #f0f0f0;
                padding: 3px 8px;
                border-radius: 4px;
                font-family: 'Fira Code', Consolas, monospace;
                font-size: 14px;
            }}
            pre {{
                background: #2d2d2d;
                color: #f8f8f2;
                padding: 20px;
                border-radius: 8px;
                overflow-x: auto;
                font-size: 14px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
                font-size: 14px;
            }}
            th, td {{
                border: 1px solid #e0e0e0;
                padding: 12px 15px;
                text-align: left;
            }}
            th {{
                background: linear-gradient(135deg, #3498db, #2980b9);
                color: white;
                font-weight: 600;
            }}
            tr:nth-child(even) {{
                background: #f9f9f9;
            }}
            tr:hover {{
                background: #f0f7ff;
            }}
            details {{
                background: #e8f4f8;
                padding: 20px;
                border-radius: 8px;
                margin: 25px 0;
                border: 1px solid #bee5eb;
            }}
            summary {{
                cursor: pointer;
                font-weight: bold;
                color: #2980b9;
                font-size: 16px;
            }}
            summary:hover {{
                color: #1a5276;
            }}
            hr {{
                border: none;
                border-top: 2px dashed #e0e0e0;
                margin: 35px 0;
            }}
            .emoji {{
                font-size: 20px;
            }}
            strong {{
                color: #2c3e50;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {html}
        </div>
    </body>
    </html>
    """
    return html_template


def send_email(subject, html_content, to_email):
    """发送邮件"""
    # 从环境变量获取邮箱配置（QQ邮箱）
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.qq.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "465"))
    smtp_user = os.environ.get("SMTP_USER")
    smtp_password = os.environ.get("SMTP_PASSWORD")  # QQ邮箱授权码
    
    if not smtp_user or not smtp_password:
        raise ValueError("请设置 SMTP_USER 和 SMTP_PASSWORD 环境变量！")
    
    # 创建邮件
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f"Knowledge Daily <{smtp_user}>"
    msg['To'] = to_email
    
    # 添加 HTML 内容
    html_part = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(html_part)
    
    # 发送邮件（使用SSL）
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())
            print(f"✅ 邮件发送成功！收件人: {to_email}")
            print(f"📧 发送时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")
        raise


def main():
    """主函数"""
    print("=" * 50)
    print("📧 Knowledge Daily - 邮件发送")
    print("=" * 50)
    
    # 加载配置
    config = load_config()
    to_email = os.environ.get("TO_EMAIL") or config["user_profile"]["email"]
    
    if not to_email:
        raise ValueError("请设置收件邮箱地址！")
    
    # 加载待发送内容
    print("📄 加载待发送内容...")
    md_content = load_pending_email()
    
    # 转换为 HTML
    print("🔄 转换为 HTML 格式...")
    html_content = markdown_to_html(md_content)
    
    # 生成邮件标题
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 从内容中提取期数
    import re
    episode_match = re.search(r'第(\d+)期', md_content)
    episode = episode_match.group(1) if episode_match else "?"
    
    subject = f"📚 每日知识推送 | 第{episode}期 | {today}"
    
    # 发送邮件
    print(f"📤 正在发送邮件到 {to_email}...")
    send_email(subject, html_content, to_email)
    
    print("=" * 50)
    print("✅ 完成！")


if __name__ == "__main__":
    main()
