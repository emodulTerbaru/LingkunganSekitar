import streamlit as st

st.set_page_config(
    page_title="Aplikasi Streamlit",
    page_icon="✨",
    layout="wide",  # Menggunakan lebar penuh layar
    initial_sidebar_state="expanded"  # Sidebar terbuka secara default
)
st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1733135017/fives_epdalm.png",width=200)
tab = st.tabs(["Lingkungan di Sekitarku","Menjaga Lingkungan Sekitar","Numerasi"])
with tab[0]:
    st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732279393/ayo_bacalah_ohjve1.png")
    with st.container(border=True):
        kol = st.columns(4,vertical_alignment="center")
        with kol[0]:
            st.image("https://img1.picmix.com/output/stamp/normal/7/8/6/4/934687_c939f.gif",width=200)
        with kol[1]:
            st.image("https://phoneky.co.uk/thumbs/screensavers/down/nature/flower_avuadpxp.gif",width=200)
        with kol[2]:
            st.image("https://phoneky.co.uk/thumbs/screensavers/down/new/places/woodhouseu_TvszJdtL.gif",width=200)
        with kol[3]:
            st.image("https://i0.wp.com/i285.photobucket.com/albums/ll73/lucky2_photo/hujan-1.gif",width=200)
    tulisan_html='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background: linear-gradient(45deg, #ff6b6b, #fddb3a, #3a86ff);
            background-size: 400% 400%;
            animation: gradientAnimation 10s ease infinite;
        }
        @keyframes gradientAnimation {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
        #judul{
            text-align:center;
            font-family:"bauhaus 93";
            font-size:40px;
            color:blue;
            text-shadow:2px 2px 2px red;
            display: flex;
            gap: 10px;
        }
        .isi{
            font-family:"comic sans ms";
            font-size:20px;
            margin:10px;
            border-radius:10px;
            background-color:lightcyan;
            padding:5px;
            text-align:justify;
        }
        .isi:hover{
            background-color:yellow;
            border:2px solid black;
        }
        #judul span {
            font-size: 4rem;
            font-weight: bold;
            position: relative;
            animation: bounce 1.5s ease-in-out infinite;
        }
        #judul span:nth-child(odd) {
            animation-delay: 0.2s;
}

    #judul span:nth-child(even) {
        animation-delay: 0.4s;
    }

        /* Keyframes */
        @keyframes bounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-20px);
            }
        }
    </style>
</head>
<body>
    <div id="judul">
        <span>L</span>
        <span>i</span>
        <span>n</span>
        <span>g</span>
        <span>k</span>
        <span>u</span>
        <span>n</span>
        <span>g</span>
        <span>a</span>
        <span>n</span><span>&nbsp;&nbsp;</span>  <span>d</span>
        <span>i</span><span>&nbsp;&nbsp;</span><span>S</span>
        <span>e</span>
        <span>k</span>
        <span>i</span>
        <span>t</span>
        <span>a</span>
        <span>r</span>
        <span>k</span>
        <span>u</span>
    </div>
    <div class="isi">Di sekitar kita, ada banyak hal yang bisa kita 
        temui setiap hari. Lingkungan adalah tempat 
        kita tinggal, bermain, dan belajar. 
        Lingkungan terdiri dari rumah, sekolah, 
        pepohonan, sungai, dan hewan-hewan yang hidup 
        bersama kita. Semua ini adalah bagian 
        penting dari kehidupan kita. Kita perlu 
        menjaga lingkungan agar tetap bersih dan 
        sehat, karena lingkungan yang baik akan 
        membuat hidup kita lebih nyaman.</div>
    <div class="isi">Di lingkungan sekolah, kita bisa melihat berbagai 
        macam tumbuhan di taman. Di sana, ada bunga, 
        pohon, dan rumput yang tumbuh subur. Setiap 
        pagi, Bapak penjaga sekolah menyiram tanaman 
        agar tetap hijau. Jika kita menghitung, ada 
        sekitar 15 jenis tanaman yang ditanam di 
        halaman sekolah. Selain itu, ada juga 
        binatang kecil seperti burung, kupu-kupu, dan
         semut yang hidup di sana. Tumbuhan dan 
         binatang-binatang itu adalah bagian dari 
         ekosistem yang saling membutuhkan.</div>
    <div class="isi">Menjaga kebersihan lingkungan juga termasuk 
        kegiatan yang harus kita lakukan setiap hari.
         Misalnya, kita harus membuang sampah pada 
         tempatnya. Jika ada 30 anak di kelas, dan 
         setiap anak membuang satu sampah sembarangan
          setiap hari, maka akan ada 30 sampah yang 
          menumpuk di sekolah. Bayangkan jika hal ini 
          terjadi setiap hari, lingkungan sekolah 
          kita akan kotor dan tidak sehat. Oleh 
          karena itu, kita harus mulai peduli dan 
          bersama-sama 
          menjaga kebersihan lingkungan.</div>
        <div class="isi">Dengan menjaga lingkungan, kita juga 
            melindungi diri sendiri dan makhluk hidup 
            lainnya. Lingkungan yang bersih akan 
            membantu kita terhindar dari penyakit. 
            Selain itu, udara yang segar dan bersih akan 
            membuat kita lebih bersemangat dalam belajar
             dan bermain. Jadi, mari kita jaga lingkungan 
             di sekitar kita, mulai dari hal-hal kecil 
             seperti tidak membuang sampah sembarangan, 
             menanam pohon, dan merawat tanaman di sekitar
              rumah dan sekolah.</div>
</body>
</html>
    '''
    st.components.v1.html(tulisan_html,width=1100,height=700)
    tulisan_css1='''
<style>
    #tombol{
        width:200px;
        height:100px;
        transform:rotate(0deg)
    }
    #tombol:hover{
        animation:gerak 4s ease-in-out infinite;
    }
    @keyframes gerak{
        0%,100%{transform:rotate(60deg);}
        25%,75%{transform:rotate(0deg);}
        50%{transform:rotate(-60deg);}
    }
</style>
'''
    st.markdown(tulisan_css1,unsafe_allow_html=True)
    st.markdown('''
<img id="tombol" src="https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732179623/soal_test_p9lghr.png">
</img>
''',unsafe_allow_html=True)
    
with tab[1]:
    css_code = """
    <style>
    .color-changing-text {
    font-size: 40px;
    font-weight: bold;
    background: linear-gradient(90deg, red, yellow, green, cyan, blue, magenta, red);
    -webkit-background-clip: text;
    color: transparent;
    animation: colorchange 5s infinite;
    background-size: 400%;
    }

    @keyframes colorchange {
    0% { background-position: 0% 50%; }
    100% { background-position: 100% 50%; }
    }
</style>
"""
    kolom2 = st.columns(2)
    st.markdown(css_code,unsafe_allow_html=True)
    with kolom2[0]:
        st.markdown('<div class="color-changing-text">Menjaga Lingkungan Sekitar</div>',unsafe_allow_html=True)
    with kolom2[1]:
        st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732279393/ayo_bacalah_ohjve1.png")
    kolom1 = st.columns(3,vertical_alignment="center")
    with kolom1[0]:
        st.image("https://media4.giphy.com/media/dvaxTCHKca8PelPPUY/200w.gif?cid=6c09b952y41awv3hpceb19dijqj2aszl699xo9j3z0rtb8no&ep=v1_gifs_search&rid=200w.gif&ct=g")
    with kolom1[1]:
        st.image("https://cdn.pixabay.com/animation/2023/03/02/15/49/15-49-31-467_512.gif",width=200)
    with kolom1[2]:
        st.image("https://i.pinimg.com/474x/77/ec/72/77ec72fa49c7c6785fedb58465d75c36.jpg",width=250)
    # Membuat paragraf dengan HTML dan CSS
    tulisan_css='''
        <style>
            .gaya-teks{
                font-family:"comic sans ms";
                font-size:20px;
                border-radius:10px;
                padding:5px;
                text-indent:60px;
                line-eight:1.6;
                text-align:justify
            }
            .gaya-teks:hover{
                border:2px solid black;
                background-color:yellow;
                color:blue;
                box-shadow:2px 2px 2px 2px green;
            }
        </style>
    '''
    st.markdown(tulisan_css,unsafe_allow_html=True)
    st.markdown("""
    <p class="gaya-teks">
    Lingkungan adalah tempat kita tinggal, belajar, dan bermain setiap hari. Di sekitar kita, ada banyak hal yang
    perlu kita jaga agar tetap bersih dan nyaman. Misalnya, kita bisa menjaga kebersihan dengan tidak membuang sampah sembarangan.
    Jika kita semua membuang sampah pada tempatnya, lingkungan akan tetap bersih dan indah. Selain itu, menjaga lingkungan juga
    berarti merawat tumbuhan dan hewan yang hidup di sekitar kita. Dengan begitu, kita ikut menjaga keseimbangan alam.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <p class="gaya-teks">
    Di sekolah, kita juga harus menjaga kebersihan. Setiap kelas biasanya memiliki tempat sampah yang digunakan untuk membuang kertas,
    plastik, dan sisa makanan. Coba bayangkan jika setiap siswa membuang satu sampah sembarangan setiap hari. Jika ada 30 siswa di kelas,
    maka dalam satu minggu bisa ada lebih dari 150 sampah yang menumpuk di sekolah! Oleh karena itu, mari kita biasakan membuang sampah pada
    tempatnya agar lingkungan sekolah tetap bersih dan nyaman.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <p class="gaya-teks">
    Selain di sekolah, lingkungan rumah juga perlu kita jaga. Di sekitar rumah, kita bisa melihat pohon-pohon yang tumbuh dan burung-burung
    yang terbang di langit. Jika kita rajin merawat tanaman dan membersihkan halaman rumah, udara di sekitar kita akan lebih segar. Udara
    segar ini penting untuk kesehatan, terutama saat kita bernapas. Jadi, menjaga lingkungan rumah juga membantu kita hidup lebih sehat.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <p class="gaya-teks">
    Menanam pohon adalah salah satu cara terbaik untuk menjaga lingkungan. Pohon-pohon memberikan banyak manfaat, seperti memberikan oksigen
    yang kita hirup dan menurunkan suhu udara. Jika setiap keluarga menanam satu pohon di halaman rumahnya, bayangkan berapa banyak pohon yang akan
    tumbuh di lingkungan kita. Semakin banyak pohon yang kita tanam, semakin bersih udara yang kita hirup.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <p class="gaya-teks">
    Terakhir, menjaga lingkungan juga membantu mengurangi polusi. Polusi bisa terjadi di udara, air, atau tanah. Misalnya, asap kendaraan bermotor
    bisa mencemari udara. Untuk mengurangi polusi, kita bisa berjalan kaki atau bersepeda ke tempat yang dekat daripada naik kendaraan bermotor. Dengan
    begitu, kita ikut menjaga bumi agar tetap sehat dan bersih untuk masa depan.
    </p>
    """, unsafe_allow_html=True)
buka = st.button("Tampilkan Soal")
tulisan_html1='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <title>Document</title>
    <style>
        #identitas{
            font-family:"comic sans ms";
            font-size:20px;
            margin:10px;
            border:2px solid red;
            border-radius:10px;
            padding:10px;
            width:500px;
        }
        #logo{
            width:200px;
            height:100px;
        }
        .masukan{
            width:200px;
            height:30px;
            border:2px solid black;
            border-radius:10px;
            padding:5px;
            box-shadow:2px 2px 2px 2px black;
            margin:5px;
            padding:10px;
            font-size:15px;
        }
        .masukan:hover{
            background-color:orange;
        }
        .masukan:focus{
            background-color:lightgray;
        }
        .pertanyaan{
            font-size:20px;
            font-weight:normal;
        }
        .masukan1, .masukan2{
            border:2px solid black;
            border-radius:3px;
            box-shadow:2px 2px 2px 2px blue;
            margin:5px;
            padding:10px;
            font-size:15px;
        }
        .masukan1:hover, .masukan2:hover{
            background-color:cyan;
        }
        .masukan1:focus, .masukan2:focus{
            background-color:lightgray;
        }
        #kirim{
            width:100px;
            height:40px;
            border:2px solid black;
            border-radius:10px;
            background-color:green;
            color:white;
            margin:5px;
            margin-left:100px;
        }
    </style>
</head>
<body>
    <div style="display:flex;justify-content: center; align-items:center;">
        <div><img id="logo" src="https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732179623/soal_test_p9lghr.png"></div>
        <div id="identitas">
            <div>Nama: <input class="masukan" type="text"></div>
            <div>Kelas: <input class="masukan" type="text"></div>
            <div>Sekolah: <input class="masukan" type="text"></div>
        </div>
    </div>
    <div style="font-weight:bold;font-size:30px;font-family:elephant">Pertanyaan</div>
    <div>
        <ol>
            <li style="font-family:'comic sans ms';font-size:25px;font-weight:bold">Pertanyaan Eksplisit:
                <ol type="a">
                    <li class="pertanyaan">Apa yang bisa kita lakukan untuk menjaga kebersihan 
                        di lingkungan sekolah?</li>
                        <div><textarea class="masukan1" cols="100" rows="10"></textarea></div>
                    <li class="pertanyaan">Mengapa menanam pohon penting untuk menjaga lingkungan?</li>
                    <div><textarea class="masukan1" cols="100" rows="10"></textarea></div>
                    <li class="pertanyaan">Berapa banyak sampah yang bisa menumpuk dalam seminggu jika ada 30 
                        siswa membuang sampah sembarangan setiap hari?</li>
                        <div><textarea class="masukan1" cols="100" rows="10"></textarea></div>
                </ol>
            </li>
            <li style="font-family:'comic sans ms';font-size:25px;font-weight:bold">Pertanyaan Implisit:
                <ol type="a">
                    <li class="pertanyaan">Bagaimana menjaga kebersihan di rumah dapat membantu kesehatan kita?</li>
                    <div><textarea class="masukan2" cols="100" rows="10"></textarea></div>
                    <li class="pertanyaan">Apa dampaknya jika kita tidak peduli dengan kebersihan lingkungan?</li>
                    <div><textarea class="masukan2" cols="100" rows="10"></textarea></div>
                    <li class="pertanyaan">Mengapa berjalan kaki atau bersepeda bisa membantu mengurangi polusi?</li>
                    <div><textarea class="masukan2" cols="100" rows="10"></textarea></div>
                </ol>
            </li>
        </ol>
    </div>
    <div><input type="button" value="Kirim" id="kirim"></div>
    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
        import { getDatabase, ref, set, get, update, remove, onValue } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";
        const firebaseConfig = {
            apiKey: "AIzaSyCkgVmk75UTkos2y1Mrc7d3-sxShMfbeJQ",
            authDomain: "natural-ethos-423713-e0.firebaseapp.com",
            databaseURL: "https://natural-ethos-423713-e0-default-rtdb.firebaseio.com",
            projectId: "natural-ethos-423713-e0",
            storageBucket: "natural-ethos-423713-e0.firebasestorage.app",
            messagingSenderId: "41833960811",
            appId: "1:41833960811:web:6218d6ac2f3538c704e82e"
        };
        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);
        var kirim = document.getElementById("kirim")
        kirim.addEventListener("click",()=>{
            var nama = document.querySelectorAll(".masukan")[0].value
            var kelas= document.querySelectorAll(".masukan")[1].value
            var sekolah = document.querySelectorAll(".masukan")[2].value 
            var soal1a = document.querySelectorAll(".masukan1")[0].value
            var soal1b = document.querySelectorAll(".masukan1")[1].value
            var soal1c = document.querySelectorAll(".masukan1")[2].value
            var soal2a = document.querySelectorAll(".masukan2")[0].value
            var soal2b = document.querySelectorAll(".masukan2")[1].value
            var soal2c = document.querySelectorAll(".masukan2")[2].value
            if(nama && kelas && sekolah){
                set(ref(db,"lingkungan/"+nama),{
                    nama:nama,
                    kelas:kelas,
                    sekolah:sekolah,
                    soal1a:soal1a,
                    soal1b:soal1b,
                    soal1c:soal1c,
                    soal2a:soal2a,
                    soal2b:soal2b,
                    soal2c:soal2c
                })
                .then(()=>{
                    alert("Data sudah ditambahkan")
                })
                .catch(()=>{
                    alert("Data belum bisa ditambahkan")
                })
            }
        })
    </script>
</body>
</html>
'''
if buka:
    st.components.v1.html(tulisan_html1,width=1000,height=2000)


with tab[2]:
    tuliskan_html5='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            padding:10px;
            background-color:lightgray
        }
        .judul{
            font-family:"bauhaus 93";
            font-size:20px;
            font-weight:bold;
        }
        .bagian{
            font-size:30px;
            color:blue;
            text-shadow:2px 2px 2px red;
        }
        .bagian1{
            margin:3px;
            color:green;
            font-weight:bold;
        }
        .ident{
            border: 2px solid black;
            border-radius:5px;
            width:300px;
            height:30px;
            box-shadow:2px 2px 2px 2px orange;
        }
        #identitas{
            padding:5px;
            border:2px solid black;
            border-radius:3px;
            box-shadow:2px 2px 2px 2px yellow;
            margin:5px;
            background-color:mistyrose
        }
        #petunjuk{
            border: 2px solid black;
            border-radius:5px;
            background-color:cyan;
            padding:5px;
            font-size:18px;
            text-align:justify;
        }
        .bagian2{
            color:brown;
            font-weight:bold;
            font-size:20px;
            margin:5px;
        }
        ul li{
            margin:3px;
            font-size:20px;
        }
        .bagian3{
            border:3px solid black;
            border-radius:10px;
            box-shadow:2px 2px 2px 2px green;
        }
        #kirim1{
            font-family:nroadway;
            font-size:20px;
            background-color:green;
            color:yellow;
        }
    </style>
</head>
<body>
    <div class="judul bagian">Tugas Numerasi: Menjaga Lingkungan Sekitar Kita</div>
    <div id="identitas">
        <div class="bagian1" id="nama">Nama: <input class="ident" type="text"></div>
        <div class="bagian1" id="kelas">Kelas: <input class="ident" type="text"></div>
    </div>
    <div class="judul">Petunjuk</div>
    <div id="petunjuk">Bacalah teks <b><i>“Lingkungan di Sekitarku”</i></b> untuk memahami lebih baik cara menjaga 
        lingkungan. Jawablah setiap soal berikut dengan menghitung, memperkirakan, dan 
        mengaplikasikan konsep numerasi. Gunakan konsep penjumlahan, pengurangan, 
        perkalian, atau pembagian sesuai kebutuhan.</div>
    <div class="judul">Soal-soal:</div>
    <div>
        <ol>
            <li><div class="bagian2">Menghitung Sampah di Sekolah</div>
                <ul type="circle">
                    <li>Di kelas terdapat 30 siswa. Jika setiap siswa membuang satu sampah 
                        sembarangan setiap hari, berapa banyak sampah yang menumpuk di 
                        sekolah dalam satu minggu (7 hari)?</li>
                        <div><textarea class="bagian3" id="jawaban1a" rows="10" cols="80"></textarea></div>
                    <li>Jika setengah dari siswa membuang dua sampah sembarangan setiap hari, 
                        berapa total sampah di sekolah dalam seminggu?</li>
                        <div><textarea class="bagian3" id="jawaban1b" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Jumlah Pohon di Lingkungan Rumah</div>
                <ul type="circle">
                    <li>Di lingkungan rumah, ada sekitar 20 rumah, dan setiap rumah rata-rata 
                        memiliki 2 pohon. Berapa total pohon di lingkungan tersebut?</li>
                        <div><textarea class="bagian3" id="jawaban2a" rows="10" cols="80"></textarea></div>
                    <li>Jika 5 rumah menambah satu pohon lagi, berapa jumlah total pohon sekarang?</li>
                    <div><textarea class="bagian3" id="jawaban2b" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Estimasi Pengurangan Polusi</div>
                <ul type="circle">
                    <li>Teks menyebutkan bahwa kita bisa berjalan kaki atau bersepeda 
                        untuk mengurangi polusi. Jika setiap siswa di kelas bersepeda 
                        atau berjalan kaki 3 kali dalam seminggu daripada menggunakan 
                        kendaraan bermotor, berapa kali dalam sebulan (4 minggu) mereka 
                        mengurangi penggunaan kendaraan bermotor? (Anggap semua siswa 
                        melakukan ini.</li>
                        <div><textarea id="jawaban3" class="bagian3" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Memperkirakan Jumlah Tanaman di Sekolah</div>
                <ul type="circle">
                    <li>Bapak penjaga sekolah menyiram sekitar 15 jenis tanaman 
                        setiap hari. Jika ada rata-rata 4 tanaman per jenis, 
                        berapa total tanaman di sekolah yang perlu disiram setiap hari?</li>
                        <div><textarea class="bagian3" id="jawaban4" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Menanam Pohon untuk Mengurangi Polusi</div>
                <ul type="circle">
                    <li>Menanam pohon adalah cara baik untuk menjaga lingkungan. 
                        Jika setiap keluarga di lingkungan kita menanam satu pohon 
                        di halaman rumahnya, dan ada 20 rumah di lingkungan tersebut, 
                        berapa banyak pohon baru yang ditanam?</li>
                        <div><textarea class="bagian3" id="jawaban5a" rows="10" cols="80"></textarea></div>
                    <li>Bayangkan jika setiap keluarga menanam 2 pohon baru setiap tahun, 
                        berapa banyak pohon yang akan tumbuh setelah 3 tahun?</li>
                        <div><textarea class="bagian3" id="jawaban5b" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Pengurangan Sampah dengan Kebiasaan Baik</div>
                <ul type="circle">
                    <li>Jika setiap siswa di kelas mulai membawa tempat makan sendiri 
                        sehingga mengurangi satu sampah plastik setiap hari, berapa 
                        banyak sampah yang dihemat oleh seluruh kelas dalam satu bulan 
                        (anggap ada 20 hari belajar dalam sebulan)?</li>
                        <div><textarea class="bagian3" id="jawaban6" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Rata-rata Tanaman di Rumah</div>
                <ul type="circle">
                    <li>Di sepanjang jalan rumah Aini terdapat 20 rumah. Jika dari 
                        20 rumah tersebut terdapat 80 tanaman, berapa rata-rata jumlah 
                        tanaman per rumah?</li>
                        <div><textarea id="jawaban7" class="bagian3" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
            <li><div class="bagian2">Menjaga Keseimbangan Ekosistem</div>
                <ul type="circle">
                    <li>Di lingkungan sekolah, terdapat banyak jenis hewan kecil seperti burung, 
                        kupu-kupu, dan semut. Jika jumlah burung ada 10 ekor, kupu-kupu 12 ekor, 
                        dan semut 50 ekor, berapa total hewan kecil tersebut?</li>
                        <div><textarea id="jawaban8a" class="bagian3" rows="10" cols="80"></textarea></div>
                    <li>Jika dalam sehari jumlah kupu-kupu bertambah 4 ekor dan semut bertambah 
                        10 ekor, berapa total hewan kecil yang ada keesokan harinya?</li>
                        <div><textarea id="jawaban8b" class="bagian3" rows="10" cols="80"></textarea></div>
                </ul>
            </li>
        </ol>
    </div>
    <div><input type="button" value="Kirim" id="kirim1"></div>
    <script type="module">
        // Konfigurasi Firebase SDK
        import {initializeApp} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
        const firebaseConfig = {
                apiKey: "AIzaSyCkgVmk75UTkos2y1Mrc7d3-sxShMfbeJQ",
                authDomain: "natural-ethos-423713-e0.firebaseapp.com",
                databaseURL: "https://natural-ethos-423713-e0-default-rtdb.firebaseio.com",
                projectId: "natural-ethos-423713-e0",
                storageBucket: "natural-ethos-423713-e0.firebasestorage.app",
                messagingSenderId: "41833960811",
                appId: "1:41833960811:web:6218d6ac2f3538c704e82e",
        };

        // Inisialisasi Firebase
        const app = initializeApp(firebaseConfig);
        import {getDatabase, set, get, update, remove, ref, child}
            from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";
        const db=getDatabase()
        var kirim1 = document.getElementById("kirim1")
        kirim1.addEventListener("click",()=>{
            var nama = document.getElementById("nama").value
            var kelas = document.getElementById("kelas").value
            var soal1a = document.getElementsByClassName("pertanyaan1a")
            var soal1b = document.getElementsByClassName("pertanyaan1b")
            var soal2a = document.getElementsByClassName("pertanyaan2a")
            var soal2b = document.getElementsByClassName("pertanyaan2b")
            var soal3 = document.getElementsByClassName("pertanyaan3")
            var soal4 = document.getElementsByClassName("pertanyaan4")
            var soal5a = document.getElementsByClassName("pertanyaan5a")
            var soal5b = document.getElementsByClassName("pertanyaan5b")
            var soal6 = document.getElementsByClassName("pertanyaan6")
            var soal7 = document.getElementsByClassName("pertanyaan7")
            var soal8a = document.getElementsByClassName("pertanyaan8a")
            var soal8b = document.getElementsByClassName("pertanyaan8b")
            set(ref(db, 'lingkunganNumerasi/' + nama), { 
                nama:nama,
                kelas:kelas,
            })
                .then(() => {
                    alert('Data added successfully');
                })
                .catch((error) => {
                console.error("Error adding data:", error);
            });
            set(ref(db, 'lingkungan1/' + nama+'/soal'), {
                soal1a:soal1a.value,
                soal1b:soal1b.value,
                soal2a:soal2a.value,
                soal2b:soal2b.value,
                soal3:soal3.value,
                soal4:soal4.value,
                soal5a:soal5a.value,
                soal5b:soal5b.value,
                soal6:soal6.value,
                soal7:soal7.value,
                soal8a:soal8a.value,
                soal8b:soal8b.value,
            })
                .then(() => {
                    alert('Data added successfully');
                })
                .catch((error) => {
                console.error("Error adding data:", error);
            });
        });
</script>
</body>
</html>
    '''
    st.components.v1.html(tuliskan_html5,width=1000,height=3400)
