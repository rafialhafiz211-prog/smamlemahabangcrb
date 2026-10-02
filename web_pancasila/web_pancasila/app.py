from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="id">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Hari Kesaktian Pancasila | SMA Muhammadiyah Lemahabang</title>

<style>

/* =========================
   RESET
========================= */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background: #f4f6f9;
    color: #202020;
    line-height: 1.7;
}


/* =========================
   NAVBAR
========================= */

.navbar {
    position: sticky;
    top: 0;
    z-index: 9999;

    background: rgba(120, 0, 0, 0.97);

    box-shadow: 0 4px 20px rgba(0,0,0,0.20);

    padding: 10px 5%;
}

.nav-container {
    max-width: 1250px;
    margin: auto;

    display: flex;
    align-items: center;
    justify-content: space-between;

    gap: 20px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;

    color: white;
}

.brand img {
    width: 50px;
    height: 50px;

    object-fit: contain;

    background: white;
    border-radius: 50%;

    padding: 4px;
}

.brand h2 {
    font-size: 17px;
}

.brand small {
    display: block;
    color: #ffdede;
    font-size: 11px;
}

.menu {
    display: flex;
    align-items: center;
    gap: 5px;

    flex-wrap: wrap;
    justify-content: center;
}

.menu a {
    color: white;
    text-decoration: none;

    padding: 9px 12px;

    border-radius: 8px;

    font-size: 13px;
    font-weight: bold;

    transition: 0.3s;
}

.menu a:hover {
    background: white;
    color: #850000;
}


/* =========================
   HERO
========================= */

.hero {

    min-height: 680px;

    display: flex;
    justify-content: center;
    align-items: center;

    text-align: center;

    padding: 70px 20px;

    background:
        linear-gradient(
            rgba(90,0,0,0.73),
            rgba(0,0,0,0.70)
        ),
        url("/static/hatake.jpg.jpeg");

    background-size: cover;
    background-position: center;
}

.hero-content {
    max-width: 950px;
    color: white;
}

.hero-logo {

    width: 125px;
    height: 125px;

    object-fit: contain;

    background: white;

    border-radius: 50%;

    padding: 9px;

    margin-bottom: 25px;

    box-shadow:
        0 10px 40px rgba(0,0,0,0.4);
}

.hero h1 {

    font-size: clamp(36px, 6vw, 70px);

    line-height: 1.15;

    margin-bottom: 15px;

    text-shadow:
        3px 4px 10px rgba(0,0,0,0.7);
}

.hero h2 {

    font-size: clamp(18px, 3vw, 30px);

    margin-bottom: 20px;
}

.hero p {

    max-width: 800px;

    margin: auto;

    font-size: 17px;

    line-height: 1.8;
}

.date {

    display: inline-block;

    margin-top: 25px;

    padding: 12px 27px;

    background: #c90000;

    border: 1px solid rgba(255,255,255,0.5);

    border-radius: 30px;

    font-weight: bold;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.3);
}

.hero-buttons {

    margin-top: 25px;

    display: flex;

    justify-content: center;

    gap: 12px;

    flex-wrap: wrap;
}

.btn {

    display: inline-block;

    padding: 12px 23px;

    border-radius: 30px;

    text-decoration: none;

    font-weight: bold;

    transition: 0.3s;
}

.btn-red {

    background: #d00000;
    color: white;
}

.btn-white {

    background: white;
    color: #850000;
}

.btn:hover {

    transform: translateY(-4px);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.25);
}


/* =========================
   GENERAL SECTION
========================= */

section {
    padding: 80px 6%;
}

.container {

    max-width: 1150px;

    margin: auto;
}

.section-title {

    text-align: center;

    margin-bottom: 45px;
}

.section-title h2 {

    color: #8b0000;

    font-size: 35px;

    margin-bottom: 8px;
}

.section-title p {

    color: #777;

    font-size: 15px;
}


/* =========================
   SAMBUTAN
========================= */

.sambutan {

    background: white;
}

.sambutan-box {

    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 25px;
}

.info-card {

    background: #ffffff;

    padding: 30px;

    border-radius: 18px;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.08);

    border-top: 5px solid #9b0000;
}

.info-card h3 {

    color: #8b0000;

    margin-bottom: 12px;
}

.info-card p {

    color: #555;

    line-height: 1.8;
}


/* =========================
   SEJARAH
========================= */

.sejarah {

    background: #f4f6f9;
}

.timeline {

    max-width: 950px;

    margin: auto;
}

.timeline-item {

    position: relative;

    background: white;

    padding: 28px;

    margin-bottom: 22px;

    border-radius: 15px;

    border-left: 6px solid #a00000;

    box-shadow:
        0 6px 22px rgba(0,0,0,0.07);
}

.timeline-item h3 {

    color: #900000;

    margin-bottom: 10px;
}

.timeline-item p {

    color: #555;

    line-height: 1.8;
}


/* =========================
   NILAI PANCASILA
========================= */

.pancasila {

    background: white;
}

.sila-grid {

    display: grid;

    grid-template-columns:
        repeat(5, 1fr);

    gap: 18px;
}

.sila-card {

    background: #fff;

    padding: 25px 18px;

    border-radius: 18px;

    text-align: center;

    box-shadow:
        0 7px 25px rgba(0,0,0,0.09);

    border-top: 5px solid #a40000;

    transition: 0.3s;
}

.sila-card:hover {

    transform: translateY(-8px);
}

.sila-number {

    width: 52px;
    height: 52px;

    display: flex;

    justify-content: center;
    align-items: center;

    margin: 0 auto 15px;

    border-radius: 50%;

    background: #a40000;

    color: white;

    font-size: 20px;

    font-weight: bold;
}

.sila-card h3 {

    font-size: 17px;

    color: #8b0000;

    margin-bottom: 12px;
}

.sila-card p {

    color: #666;

    font-size: 14px;

    line-height: 1.6;
}


/* =========================
   POSTER
========================= */

.poster-section {

    background: #f4f6f9;
}

.poster-card {

    background: white;

    padding: 20px;

    border-radius: 22px;

    max-width: 850px;

    margin: auto;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.10);

    text-align: center;
}

.poster-card img {

    width: 100%;

    max-height: 700px;

    object-fit: contain;

    border-radius: 15px;

    display: block;
}

.fullscreen {

    margin-top: 18px;

    border: none;

    background: #8b0000;

    color: white;

    padding: 12px 23px;

    border-radius: 30px;

    font-weight: bold;

    cursor: pointer;
}

.fullscreen:hover {

    background: #bd0000;
}


/* =========================
   KEPALA SEKOLAH
========================= */

.kepala {

    background: white;
}

.kepala-box {

    max-width: 950px;

    margin: auto;

    display: grid;

    grid-template-columns:
        300px 1fr;

    gap: 40px;

    align-items: center;

    background: #fafafa;

    padding: 30px;

    border-radius: 22px;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.08);
}

.kepala-box img {

    width: 100%;

    height: 360px;

    object-fit: cover;

    border-radius: 18px;

    border: 5px solid #a00000;
}

.kepala-info h2 {

    color: #8b0000;

    margin-bottom: 7px;
}

.jabatan {

    color: #bd0000;

    font-weight: bold;

    margin-bottom: 20px;
}

.kepala-info p {

    color: #555;

    line-height: 1.8;
}


/* =========================
   GALERI
========================= */

.galeri {

    background: #f4f6f9;
}

.gallery-grid {

    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 18px;
}

.gallery-card {

    background: white;

    padding: 8px;

    border-radius: 15px;

    overflow: hidden;

    box-shadow:
        0 6px 22px rgba(0,0,0,0.10);

    transition: 0.3s;
}

.gallery-card:hover {

    transform: translateY(-7px);
}

.gallery-card img {

    width: 100%;

    height: 230px;

    object-fit: cover;

    border-radius: 10px;

    display: block;

    cursor: pointer;
}


/* =========================
   MAKNA
========================= */

.makna {

    background: white;
}

.makna-grid {

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 20px;
}

.makna-card {

    padding: 28px;

    border-radius: 18px;

    background: #fafafa;

    text-align: center;

    box-shadow:
        0 5px 20px rgba(0,0,0,0.07);
}

.makna-card .icon {

    font-size: 42px;

    margin-bottom: 10px;
}

.makna-card h3 {

    color: #8b0000;

    margin-bottom: 10px;
}

.makna-card p {

    color: #666;
}


/* =========================
   QUOTE
========================= */

.quote {

    background:
        linear-gradient(
            rgba(100,0,0,0.9),
            rgba(100,0,0,0.9)
        );

    color: white;

    text-align: center;
}

.quote h2 {

    font-size: 30px;

    margin-bottom: 15px;
}

.quote p {

    max-width: 800px;

    margin: auto;

    font-size: 18px;

    line-height: 1.8;
}


/* =========================
   FOOTER
========================= */

footer {

    background: #520000;

    color: white;

    text-align: center;

    padding: 40px 20px;
}

footer h3 {

    margin-bottom: 10px;
}

footer p {

    color: #e5caca;

    font-size: 14px;
}


/* =========================
   IMAGE MODAL
========================= */

.modal {

    display: none;

    position: fixed;

    z-index: 99999;

    left: 0;
    top: 0;

    width: 100%;
    height: 100%;

    background: rgba(0,0,0,0.92);

    justify-content: center;
    align-items: center;

    padding: 30px;
}

.modal img {

    max-width: 95%;

    max-height: 90%;

    object-fit: contain;

    border-radius: 10px;
}

.close {

    position: absolute;

    top: 20px;
    right: 35px;

    color: white;

    font-size: 45px;

    cursor: pointer;
}


/* =========================
   MOBILE
========================= */

@media(max-width: 1000px) {

    .sila-grid {

        grid-template-columns:
            repeat(2, 1fr);
    }

    .gallery-grid {

        grid-template-columns:
            repeat(3, 1fr);
    }

}

@media(max-width: 750px) {

    .nav-container {

        flex-direction: column;

    }

    .menu {

        width: 100%;

    }

    .menu a {

        font-size: 12px;

    }

    .sambutan-box {

        grid-template-columns: 1fr;

    }

    .kepala-box {

        grid-template-columns: 1fr;

        text-align: center;

    }

    .kepala-box img {

        max-width: 300px;

        margin: auto;

    }

    .gallery-grid {

        grid-template-columns:
            repeat(2, 1fr);

    }

    .makna-grid {

        grid-template-columns: 1fr;

    }

}

@media(max-width: 500px) {

    section {

        padding: 55px 5%;

    }

    .hero {

        min-height: 620px;

    }

    .sila-grid {

        grid-template-columns: 1fr;

    }

    .gallery-grid {

        grid-template-columns: 1fr;

    }

    .gallery-card img {

        height: 280px;

    }

    .brand h2 {

        font-size: 14px;

    }

}

</style>

</head>


<body>


<!-- ================= NAVBAR ================= -->

<nav class="navbar">

<div class="nav-container">


<div class="brand">

<img src="/static/logo.jpg.jpeg">
<div>

<h2>SMA Muhammadiyah Lemahabang</h2>

<small>Hari Kesaktian Pancasila</small>

</div>

</div>


<div class="menu">

<a href="#beranda">Beranda</a>

<a href="#tentang">Tentang</a>

<a href="#sejarah">Sejarah</a>

<a href="#pancasila">Nilai Pancasila</a>

<a href="#poster">Poster</a>

<a href="#kepala">Kepala Sekolah</a>

<a href="#galeri">Dokumentasi</a>

</div>


</div>

</nav>



<!-- ================= HERO ================= -->

<header class="hero" id="beranda">

<div class="hero-content">


<img
src="/static/poster.jpg.jpeg"
class="hero-logo"
>


<h1>
HARI KESAKTIAN PANCASILA
</h1>


<h2>
SMA MUHAMMADIYAH LEMAHABANG
</h2>


<p>

Memperingati Hari Kesaktian Pancasila sebagai momentum
untuk mengenang perjuangan para pendahulu bangsa,
memperkuat persatuan, serta mengamalkan nilai-nilai
Pancasila dalam kehidupan sehari-hari.

</p>


<div class="date">

🇮🇩 1 OKTOBER 2026 🇮🇩

</div>


<div class="hero-buttons">

<a
href="#sejarah"
class="btn btn-red"
>
Pelajari Sejarah
</a>


<a
href="#galeri"
class="btn btn-white"
>
Lihat Dokumentasi
</a>

</div>


</div>

</header>



<!-- ================= TENTANG ================= -->

<section
class="sambutan"
id="tentang"
>

<div class="container">


<div class="section-title">

<h2>
Tentang Hari Kesaktian Pancasila
</h2>

<p>
Mengenal makna dan tujuan peringatannya
</p>

</div>


<div class="sambutan-box">


<div class="info-card">

<h3>
🇮🇩 Apa Itu Hari Kesaktian Pancasila?
</h3>

<p>

Hari Kesaktian Pancasila diperingati setiap
tanggal 1 Oktober di Indonesia. Peringatan
ini menjadi momentum untuk meneguhkan kembali
Pancasila sebagai dasar negara dan ideologi bangsa.

</p>

</div>


<div class="info-card">

<h3>
🎓 Mengapa Diperingati?
</h3>

<p>

Peringatan ini mengajak seluruh masyarakat,
khususnya generasi muda, untuk menjaga persatuan,
menghargai perjuangan para pahlawan dan menerapkan
nilai-nilai Pancasila dalam kehidupan.

</p>

</div>


</div>

</div>

</section>



<!-- ================= SEJARAH ================= -->

<section
class="sejarah"
id="sejarah"
>

<div class="container">


<div class="section-title">

<h2>
Sejarah Hari Kesaktian Pancasila
</h2>

<p>
Perjalanan sejarah dan makna peringatannya
</p>

</div>


<div class="timeline">


<div class="timeline-item">

<h3>
📅 1 Juni 1945
</h3>

<p>

Dalam sidang BPUPKI, gagasan mengenai dasar
negara Indonesia disampaikan dan berkembang
menjadi rumusan Pancasila.

</p>

</div>


<div class="timeline-item">

<h3>
🇮🇩 18 Agustus 1945
</h3>

<p>

Pancasila ditetapkan sebagai dasar negara
dalam Pembukaan Undang-Undang Dasar 1945.

</p>

</div>


<div class="timeline-item">

<h3>
📅 30 September – 1 Oktober 1965
</h3>

<p>

Indonesia mengalami peristiwa politik dan
keamanan yang dikenal sebagai Gerakan
30 September atau G30S.

</p>

</div>


<div class="timeline-item">

<h3>
🇮🇩 1 Oktober
</h3>

<p>

Tanggal 1 Oktober kemudian diperingati sebagai
Hari Kesaktian Pancasila sebagai momentum untuk
meneguhkan Pancasila sebagai dasar negara dan
memperkuat persatuan bangsa.

</p>

</div>


<div class="timeline-item">

<h3>
🎓 Makna Bagi Generasi Muda</h3>

<p>

Generasi muda memiliki peran penting dalam menjaga
persatuan, menghargai keberagaman, menjunjung
toleransi dan mengamalkan nilai Pancasila
dalam kehidupan sehari-hari.

</p>

</div>


</div>

</div>

</section>



<!-- ================= NILAI PANCASILA ================= -->

<section
class="pancasila"
id="pancasila"
>

<div class="container">


<div class="section-title">

<h2>
5 Nilai Dasar Pancasila
</h2>

<p>
Pedoman dalam kehidupan bermasyarakat dan bernegara
</p>

</div>


<div class="sila-grid">


<div class="sila-card">

<div class="sila-number">
1
</div>

<h3>
Ketuhanan Yang Maha Esa
</h3>

<p>

Menghormati agama dan kepercayaan,
menjalankan ibadah serta menghargai
kebebasan beragama.

</p>

</div>


<div class="sila-card">

<div class="sila-number">
2
</div>

<h3>
Kemanusiaan yang Adil dan Beradab
</h3>

<p>

Menghargai sesama manusia, menjunjung
persamaan derajat, serta bersikap adil
dan beradab.

</p>

</div>


<div class="sila-card">

<div class="sila-number">
3
</div>

<h3>
Persatuan Indonesia
</h3>

<p>

Menjaga persatuan, mencintai tanah air,
menghargai keberagaman dan mengutamakan
kepentingan bangsa.

</p>

</div>


<div class="sila-card">

<div class="sila-number">
4
</div>

<h3>
Kerakyatan
</h3>

<p>

Mengutamakan musyawarah, menghargai
pendapat dan mengambil keputusan
dengan bijaksana.

</p>

</div>


<div class="sila-card">

<div class="sila-number">
5
</div>

<h3>
Keadilan Sosial
</h3>

<p>

Bersikap adil, saling membantu dan
berusaha menciptakan kesejahteraan
bersama.

</p>

</div>


</div>

</div>

</section>



<!-- ================= POSTER ================= -->

<section
class="poster-section"
id="poster"
>

<div class="container">


<div class="section-title">

<h2>
Poster Hari Kesaktian Pancasila
</h2>

<p>
SMA Muhammadiyah Lemahabang
</p>

</div>


<div class="poster-card">


<img
src="/static/hatake.jpg.jpeg"
id="posterImage"
alt="Poster Hari Kesaktian Pancasila"
>


<button
class="fullscreen"
onclick="fullScreenPoster()"
>

⛶ Lihat Poster Fullscreen

</button>


</div>

</div>

</section>



<!-- ================= KEPALA SEKOLAH ================= -->

<section
class="kepala"
id="kepala"
>

<div class="container">


<div class="section-title">

<h2>
Kepala Sekolah SMA Muhammadiyah Lemahabang
</h2>

<p>
Pimpinan dan pembina warga sekolah
</p>

</div>


<div class="kepala-box">


<img
src="/static/kepsek.jpg.jpeg"
alt="Kepala Sekolah"
>


<div class="kepala-info">


<h2>
Gilang Bayu Purnama, S.Pd.
</h2>


<div class="jabatan">
Kepala Sekolah SMA Muhammadiyah Lemahabang
</div>


<p>

Mari kita jadikan Hari Kesaktian Pancasila
sebagai momentum untuk memperkuat karakter,
persatuan dan semangat kebangsaan.

</p>


<br>


<p>

Sebagai generasi penerus bangsa, kita harus
mampu mengamalkan nilai-nilai Pancasila,
menghargai perbedaan dan menjaga persatuan
di lingkungan sekolah maupun masyarakat.

</p>


</div>

</div>

</div>

</section>



<!-- ================= GALERI ================= -->

<section
class="galeri"
id="galeri"
>

<div class="container">


<div class="section-title">

<h2>
Dokumentasi Kegiatan
</h2>

<p>
Dokumentasi kegiatan SMA Muhammadiyah Lemahabang
</p>

</div>


<div class="gallery-grid">


<div class="gallery-card">

<img
src="/static/foto1.jpg.jpeg"
onclick="showImage(this.src)"
>

</div>


<div class="gallery-card">

<img
src="/static/foto2.jpg.jpeg"
onclick="showImage(this.src)"
>

</div>


<div class="gallery-card">

<img
src="/static/foto3.jpg.jpeg"
onclick="showImage(this.src)"
>

</div>


<div class="gallery-card">

<img
src="/static/foto4.jpg.jpeg"
onclick="showImage(this.src)"
>

</div>


<div class="gallery-card">

<img
src="/static/foto5.jpg.jpeg"
onclick="showImage(this.src)"
>

</div>


<div class="gallery-card">

<img
src="/static/foto6.jpg.jpeg"
onclick="showImage(this.src)"
>

</div>


<div class="gallery-card">

<img
src="/static/foto7.jpg.jpeg"
onclick="showImage(this.src)"
>

</div>


</div>

</div>

</section>



<!-- ================= MAKNA ================= -->

<section
class="makna"
>

<div class="container">


<div class="section-title">

<h2>
Semangat Pancasila
</h2>

<p>
Nilai yang dapat diterapkan di lingkungan sekolah
</p>

</div>


<div class="makna-grid">


<div class="makna-card">

<div class="icon">
🤝
</div>

<h3>
Persatuan
</h3>

<p>

Menghargai perbedaan dan menjaga
kerukunan antarwarga sekolah.

</p>

</div>


<div class="makna-card">

<div class="icon">
🎓
</div>

<h3>
Pendidikan Karakter
</h3>

<p>

Membangun generasi yang berkarakter,
berilmu dan bertanggung jawab.

</p>

</div>


<div class="makna-card">

<div class="icon">
🇮🇩
</div>

<h3>
Cinta Tanah Air
</h3>

<p>

Menumbuhkan rasa cinta terhadap
Indonesia dan menjaga keutuhan bangsa.

</p>

</div>


</div>

</div>

</section>



<!-- ================= QUOTE ================= -->

<section class="quote">

<div class="container">

<h2>
🇮🇩 Pancasila Pemersatu Bangsa 🇮🇩
</h2>

<p>

"Jadikan Pancasila sebagai pedoman dalam
berpikir, bersikap dan bertindak untuk
membangun Indonesia yang lebih baik."

</p>

</div>

</section>



<!-- ================= FOOTER ================= -->

<footer>

<h3>
SMA MUHAMMADIYAH LEMAHABANG
</h3>

<p>
Hari Kesaktian Pancasila
</p>

<p>
1 Oktober 2026
</p>

<br>

<p>
© 2026 SMA Muhammadiyah Lemahabang
</p>

</footer>



<!-- ================= MODAL FOTO ================= -->

<div
class="modal"
id="imageModal"
onclick="closeImage()"
>

<span class="close">
&times;
</span>

<img
id="modalImage"
>

</div>



<script>


function showImage(src) {

    const modal =
        document.getElementById("imageModal");

    const image =
        document.getElementById("modalImage");

    image.src = src;

    modal.style.display = "flex";

}


function closeImage() {

    document.getElementById(
        "imageModal"
    ).style.display = "none";

}


function fullScreenPoster() {

    const image =
        document.getElementById("posterImage");

    if (image.requestFullscreen) {

        image.requestFullscreen();

    }

    else if (image.webkitRequestFullscreen) {

        image.webkitRequestFullscreen();

    }

}


</script>


</body>

</html>
"""


@app.route("/")
def home():

    return render_template_string(HTML)


if __name__ == "__main__":

    app.run(
        host="192.168.1.5",
        port=5000,
        debug=True
    )