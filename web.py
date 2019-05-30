from flask import Flask, render_template, redirect, url_for
from record import *

app = Flask(__name__)
@app.route('/')
def index():
    return redirect(url_for('cmd_index'))

@app.route('/cmd')
def cmd_index():
    return render_template('index.html', mesaj="Öncelikle init()'e bas!")

@app.route('/cmd/<cmd>')
def cmd(cmd):
    if(cmd=="init"):
        engineStart();engineStart()
        mesaj = "Ayarlandı!"
    elif(cmd=="duz"):
        goForward()
        sleep(1.5)
        engineWait()
        kaydet("duz",float(100))
        mesaj = "Düz gidiliyor"
    elif(cmd=="sag"):
        turnRight()
        engineWait()
        kaydet("sag",float(100))
        mesaj = "Dönüş sağlandı!"
    elif(cmd=="sol"):
        turnLeft()
        engineWait()
        kaydet("sol",float(100))
        mesaj = "Dönüş sağlandı!"
    elif(cmd=="geri"):
        goBackward()
        sleep(1.5)
        engineWait()
        kaydet("geri",float(100))
        mesaj = "Geri gidiliyor!"
    elif(cmd=="oynat"):
        oynat()
        mesaj = "Oynatıldı!"
    return render_template('index.html', mesaj=mesaj)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
