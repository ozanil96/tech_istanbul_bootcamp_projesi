from flask import Flask, render_template, request, redirect, url_for
from models import db, Gorev

app = Flask(__name__)

# Veritabanı Ayarları (SQLite kullanılacak)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Veritabanını uygulamaya bağlıyoruz
db.init_app(app)

# Uygulama ilk çalıştığında veritabanı tablolarını oluştur
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Tüm görevleri listeleme sayfası"""
    gorevler = Gorev.query.order_by(Gorev.id.desc()).all()
    return render_template('index.html', gorevler=gorevler)

@app.route('/ekle', methods=['POST'])
def ekle():
    """Yeni görev ekleme işlemi (Create)"""
    baslik = request.form.get('baslik')
    aciklama = request.form.get('aciklama')

    if baslik:
        yeni_gorev = Gorev(baslik=baslik, aciklama=aciklama)
        db.session.add(yeni_gorev)
        db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/guncelle/<int:id>')
def guncelle(id):
    """Görevin durumunu (Tamamlandı/Beklemede) değiştirme (Update)"""
    gorev = Gorev.query.get_or_404(id)
    gorev.tamamlandi = not gorev.tamamlandi # Durumu tersine çevir
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/sil/<int:id>')
def sil(id):
    """Görevi veritabanından silme (Delete)"""
    gorev = Gorev.query.get_or_404(id)
    db.session.delete(gorev)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)