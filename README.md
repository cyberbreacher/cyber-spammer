# Cyber Spammer

Cyber Spammer is a python tool that continuously spams mail to the victim's mail inbox. Require at least five fake accounts to start. Works for both Termux and Linux.

## DISCLAIMER

our program is for EDUCATIONAL PURPOSES ONLY. Don't use this for illegal activities. You are the only responsable for your actions!

## Installation

```bash
git clone https://github.com/Cyberbreacher/cyber-spammer.git
cd cyber-spammer
nano assets/assets.txt
```
Now put the username and password like shown in the screenshot. Remember to allow a less safe app to access in account. [How to do?](https://devanswers.co/allow-less-secure-apps-access-gmail-account/)
 
![Script Screenshot](https://i.ibb.co/72KhBvz/demo.png)

```bash
pip3 install -r requirements.txt
python3 cyber_spammer.py

```
## Social Media

If you liked my script you can follow me for more.

Youtube:- [https://www.youtube.com/channel/UC7kQjyxl5rfMp27cpCQomGw](https://www.youtube.com/channel/UC7kQjyxl5rfMp27cpCQomGw)

Instagram:- [https://www.instagram.com/cyberbreacher/](https://www.instagram.com/cyberbreacher/)

Telegram:- [https://t.me/cyberbreacher](https://t.me/cyberbreacher)

Facebook:- [https://www.facebook.com/CyberBreacher/](https://www.facebook.com/CyberBreacher/)

## Usage
This script is designed to work for five accounts and if you like to add more. Edit the python script.

```python
user_5 = login.readline() # After This Add Same Two Lines
pass_5 = login.readline() # And Change the number (5 -> 6)

for sending in range(1):
 server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
 server.ehlo()
 server.login(user_5, pass_5) # Same Here (5 -> 6)
 message_format = MIMEMultipart() # And Add Them with Indent
 message_format['From'] = mail_data[0] # In The Same Loop
 message_format['To'] = mail_data[1]  
 message_format['Subject'] = mail_data[2]
 message = mail_data[3]
 message_format.attach(MIMEText(message, 'plain'))
 text = message_format.as_string()
 server.sendmail(user_1,mail_data[1],text) 
 print("Sent.                          :)")
 server.quit()

```
## Screenshot

![Script Screenshot](https://i.ibb.co/GV1ZqHb/01.png)
![Script Screenshot](https://i.ibb.co/x7wFFmS/02.png)
![Script Screenshot](https://i.ibb.co/R2zFvG7/03.png)
![Script Screenshot](https://i.ibb.co/B66P4X7/04.png)
![Script Screenshot](https://i.ibb.co/p1tnn06/05.png)
