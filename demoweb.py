#!/usr/bin/python

import subprocess

from flask import Flask, render_template_string, request
app = Flask(__name__)

home = """
<!doctype html>
<html>
<head>
<title>Comitup Demo</title>
</head>
<body>
Learn more about <a href="http://davesteele.github.io/comitup/">Comitup</a>.
<br>
<br>
{% if confirm %}
Your name has been submitted.
{% endif %}
{% if winner %}
Congratulations!
<br><br>
You were the person who successfully connected the wifi.
Enter your name to register your accomplishment.
<form action="/" method="post">
<br><br>
<input type="text" name="name">
<br><br>
<input type="submit" value="Submit">
</form>
{% endif %}
</body>
</html>
"""


wincmd = "grep comitup-web /var/log/syslog | grep POST | grep connect | head -1 | awk '{print $6 }'"

def is_winner():
    win_ip = subprocess.check_output(wincmd, shell=True).decode().strip()

    req_ip = request.remote_addr

    print(win_ip, req_ip)

    return win_ip and win_ip == req_ip


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template_string(home, winner=is_winner(), confirm=False)
    else:
        name = request.form['name']

        with open("/tmp/comitup-demo.txt", 'w') as fp:
            fp.write("We have a winner ... ")
            fp.write("%s ... " % name)
            fp.write("Repeat ... %s" % name)

        return render_template_string(home, winner=False, confirm=True)
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
