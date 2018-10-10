# coding:utf-8

#发送邮件
import smtplib
#信息头
from email.header import Header
#正文文本
from email.mime.text import MIMEText
#添加带附件功能
from email.mime.multipart import MIMEMultipart
#图片
from email.mime.image import MIMEImage
#附件
from email.mime.application import MIMEApplication


mailto_list = ['lubaobao_v@didichuxing.com','751500349@qq.com']
mail_host = "mail.didichuxing.com"
mail_user = "lubaobao_v@didichuxing.com"
mail_pass = "!Ni8zhidao!"
mail_port = '587'


def send_mail(to_list):
    # 创建一个带附件的实例,注意！！multipart类型为related，无这个类型会出现两张图片在邮件中
    msg = MIMEMultipart('related')
    # html格式构造
    html = """
    <html> 
      <head></head> 
      <body> 
          <p>
          Hi，all:
          </p>
          <p style="text-indent:2em;">以下是自动化测试报告：
          </p>
          <p>
           <br><img src="cid:image1"></br> 
          </p>
          <br>
          请查看附件附件
          </br>
      </body> 
    </html> 
    """
    htm = MIMEText(html, 'html', 'utf-8')
    msg.attach(htm)

    # 添加excel附件
    with open('../Report/report.xlsx', 'rb') as f:
        att1 = MIMEApplication(f.read())
        att1.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', 'Report.xlsx'))
        msg.attach(att1)

    #添加正文图片
    with open('/Users/didi/Downloads/222111.png','rb') as f1:
        image = MIMEImage(f1.read())
        image.add_header('Content-ID', '<image1>')
        msg.attach(image)

    #邮件主题
    msg['Subject'] = Header('测试TEST')
    #发件人
    msg['From'] = mail_user
    #收件人
    msg['To'] = ";".join(to_list)

    #发送邮件
    try:
        server = smtplib.SMTP()
        server.connect(mail_host,mail_port)
        server.starttls()
        server.login(mail_user, mail_pass)
        print("登录成功")
        server.sendmail(mail_user, to_list, msg.as_string())
        server.close()
        print('发送成功')
    except:
        print('链接失败')

send_mail(mailto_list)