import smtplib
from typing import Any
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from followee_notifier.types import FollowerIncrements


def render(current_time: datetime, platform: str, increments: FollowerIncrements) -> str:
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S UTC')
    cell_style = 'style="text-align: left; border: 1px solid #c0c0c0; padding: 4px 12px"'
    span_style = 'style="text-align: center; padding: 4px 12px; border: 1px solid #c0c0c0; padding: 4px 12px"'
    html = f"""
    <h1 style="font-weight: 400">Follower Notification</h1>
    <table border="1" cellspacing="0" cellpadding="0">
        <tr>
            <td width="120px" {cell_style}">Platform</td>
            <td width="180px" {cell_style}"><code>{platform}</code></td>
            <td width="120px" {cell_style}">Time</td>
            <td width="180px" {cell_style}"><code>{formatted_time}</code></td>
        </tr>
        <tr>
            <td colspan="4" {span_style}>Followers</td>
        </tr>
        <tr>
            <td {cell_style}">Old</td>
            <td {cell_style}">{len(increments["old"])}</td>
            <td {cell_style}">New</td>
            <td {cell_style}">{len(increments["new"])}</td>
        </tr>
        <tr>
            <td {cell_style}">New Followers</td>
            <td {cell_style}">{len(increments["add"])}</td>
            <td {cell_style}">Lost Followers</td>
            <td {cell_style}">{len(increments["del"])}</td>
        </tr>
    </table>
    """
    if len(increments["add"]) > 0:
        html += f"""
        <h2>New Followers</h2>
        <ul>
            {"".join([
                f'''<li>
                    {i["display_name"]}
                    (<a href="{i["url"]}">{i["name"]}</a>) - 
                    <code>{i["id"]}</code>
                </li>'''
                for i in increments["add"]
            ])}
        </ul>
        """
    if len(increments["del"]) > 0:
        html += f"""
        <h2>Lost Followers</h2>
        <ul>
            {"".join([
                f'''<li>
                    {i["display_name"]}
                    (<a href="{i["url"]}">{i["name"]}</a>) - 
                    <code>{i["id"]}</code>
                </li>'''
                for i in increments["del"]
            ])}
        </ul>
        """
    return html


def notify(config: dict[str, Any], platform: str, fetched_at: datetime, increments: FollowerIncrements):
    body = render(fetched_at, platform, increments)
    subject = f'Follower Notification ({platform}) as of {fetched_at.strftime("%Y-%m-%d")}'
    subject += f' [{len(increments["old"])} -> {len(increments["new"])}, +{len(increments["add"])}, -{len(increments["del"])}]'
    exceptions = []
    for dest_address in config['to']:
        try:
            print(f'[SMTP] Send email from <{config["from"]}> to <{dest_address}>')
            message = MIMEMultipart()
            message['From'] = f"Follower Notifier <{config['from']}>"
            message['To'] = dest_address
            message['Subject'] = subject
            message.attach(MIMEText(body, 'html'))
            print(f'[SMTP] > Connecting smtp+tls://{config["host"]}:{config["port"]}...')
            with smtplib.SMTP_SSL(config['host'], config['port']) as server:
                result = server.login(config['username'], config['password'])
                print(f'[SMTP] < {result}')
                result = server.sendmail(message['From'], message['To'], message.as_string())
                print(f'[SMTP] < {result}')
        except Exception as e:
            exceptions.append(e)
            continue
    if len(exceptions) > 0:
        raise Exception(exceptions)
