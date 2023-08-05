from email.header import Header
from email.mime.text import MIMEText
import logging
import smtplib
from jinja2 import Environment, FileSystemLoader
import os


class LspNotify:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def mail(self, config, content):
        root = os.path.dirname(__file__)
        path = os.path.join(root, 'resource')
        env = Environment(loader=FileSystemLoader(path))
        template = env.get_template('mail.html')
        html_content = template.render(content=content)

        message = MIMEText(str(html_content), 'html', 'utf-8')
        message['From'] = '%s <%s>' % (
            Header(config['name'], 'utf-8').encode(), config['usn'])
        message['To'] = config['recv']
        message['Subject'] = Header(
            '发现LSPSP.ME新库存%d个' % (len(content)), 'utf-8').encode()

        smtp = None
        if config['ssl']:
            smtp = smtplib.SMTP_SSL(config['host'], config['port'])
        else:
            smtp = smtplib.SMTP(config['host'], config['port'])
        smtp.login(config['usn'], config['pwd'])
        smtp.sendmail(config['usn'], config['recv'], message.as_string())
        self._logger.info("Email sended to: %s", config['recv'])
