from flask import Flask
import random


app = Flask(__name__)

bilgiler = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.", "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor."]

@app.route("/")
def hello_world():
    return "<h1>Siteme hoş geldiniz!<h1>"

@app.route("/ikincisayfa")
def second():
    karekterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sifre = ""
    for i in range(8):
        sifre += random.choice(karekterler)
    return f'<h2>Sızın ıçın oluşturudgumuz 8 hanelı şıfre : {sifre}</h2>'

@app.route("/rastgelebilgi")
def rasgele():
    bilgi = random.choice(bilgiler)

    return f'<p>{bilgi}</p>'
app.run(debug=True)
