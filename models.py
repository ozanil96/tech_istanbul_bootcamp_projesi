from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy nesnesini oluşturuyoruz
db = SQLAlchemy()

class Gorev(db.Model):
    """
    Gorev sınıfı, yapılacaklar listesindeki her bir maddeyi temsil eder.
    OOP prensiplerine göre özellikleri (attributes) aşağıdadır.
    """
    __tablename__ = 'gorevler'

    id = db.Column(db.Integer, primary_key=True)
    baslik = db.Column(db.String(100), nullable=False)
    aciklama = db.Column(db.String(200), nullable=True)
    # Durum: False = Beklemede, True = Tamamlandı
    tamamlandi = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Gorev {self.baslik}>'