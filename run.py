def modify(n):
    s = ''
    n = str(n)
    index = 0
    max_index = len(n) - 2
    if len(n) % 2 == 1:
        max_index -= 1
    while index <= max_index:
        num = (int(n[index:index+2])*int(n[index])) % 126
        while num < 48:
            num = num + 48
        temp = chr(num)
        if temp == '\n':
            temp = chr((num + index + 1) % 126)
        s += temp
        index += 1
    return s

def sum_ord(s):
    n = 0
    l = len(s)
    for i in range(l):
        n += ord(s[i])
    return n

def insert_pwd(s, pwd):
    new = ''
    index = 0
    while len(s) > 0 and index < len(pwd):
        if index % 2 == 0:
            new += modify(sum_ord(s[0]))
            s = s[1:]
        new += pwd[index]
        index += 1
    return new

def process(pwd, platform):
    n = len(pwd)
    for i in range(n):
        char = pwd[i]
        no = (ord(char) ** (2*ord(char)))
        modify_s = modify(no)

    s = insert_pwd(platform, modify_s)
    n = len(s)
    for i in range(n):
        char = s[i]
        no = (ord(char) ** (2*ord(char)))
        modify_s1 = modify(no)
    return modify_s1

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
	return render_template('index.html')

@app.route('/run',methods=["POST"])
def run():            
    pwd = request.form['pwd']
    platform = request.form['platform']
    n1 = len(pwd) % 4
    s = process(pwd, platform)
    for i in range(n1):
        s = process(s, platform)
    return render_template('result.html', p = s)
        
app.run()
