import streamlit as st

st.set_page_config(
    page_title="Aplikasi Streamlit",
    page_icon="✨",
    layout="wide",  # Menggunakan lebar penuh layar
    initial_sidebar_state="expanded"  # Sidebar terbuka secara default
)


# HTML dan CSS untuk judul animasi
html_code = """
<style>
  @keyframes pulse {
    0%, 100% {
      transform: scale(1);
      color: #ff6ec7;
      text-shadow: 0 0 5px #ff6ec7, 0 0 15px #ff6ec7, 0 0 20px #ff6ec7, 0 0 40px #ff6ec7;
    }
    50% {
      transform: scale(1.2);
      color: #f3f169;
      text-shadow: 0 0 5px #f3f169, 0 0 15px #f3f169, 0 0 20px #f3f169, 0 0 40px #f3f169;
    }
  }

  .animated-title {
    font-size: 30px;
    font-weight: bold;
    text-align: center;
    animation: pulse 3s infinite;
  }
</style>
<div style="background-color:black;">
    <div class="animated-title">
      ✨ Perburuan Liar Ancam Macan Tutul di Ujung Kulon ✨
    </div>
</div>
"""
st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1733135017/fives_epdalm.png",width=200)
tab = st.tabs(["Perburuan Liar","Latihan"])
with tab[0]:
    # Tampilkan animasi di Streamlit
    st.markdown(html_code, unsafe_allow_html=True)
    tulisan_html='''
    <div style="text-align:center;margin-top:10px;border:3px solid purple;box-shadow:2px 2px 2px 2px red;padding:5px;background-color:gray"><img src="https://i.pinimg.com/originals/e4/23/33/e4233340e5e52282707c04f4d9b49ad6.gif"></div>
    '''
    st.markdown(tulisan_html,unsafe_allow_html=True)
    html_code2 = """
<style>
  .animated-border {
    font-size: 1.5rem;
    font-weight: bold;
    text-align: justify;
    color: black;
    text-indent:80px;
    padding: 20px;
    margin:10px;
    border: 4px solid transparent;
    background: linear-gradient(white, white) padding-box, 
                linear-gradient(90deg, #e74c3c, #f1c40f, #3498db, #9b59b6) border-box;
    border-radius: 15px;
    position: relative;
    animation: border-move 3s linear infinite;
  }
    .animated-border:hover{
        background-color:yellow;
        font-family:"comic sans ms";
    }
  @keyframes border-move {
    0% {
      background-position: 0%;
    }
    100% {
      background-position: 200%;
    }
  }
</style>
"""
    st.markdown(html_code2,unsafe_allow_html=True)
    tulisan1='''
<div class="animated-border">
  Pada pagi yang cerah, Pak Ardan yang bertempat tinggal tidak jauh dari Taman Nasional berjalan memasuki hutan lindung.
  Bersama seorang teman, Pak Ardan mengendap-endap di antara semak belukar sambil melirik ke kiri dan ke kanan. Tak lama
  kemudian, Pak Ardan dan temannya tersentak kaget. Seekor binatang yang berlari sangat cepat di hadapan mereka. “Sembunyi!”
  teriak Pak Ardan kepada temannya. Mereka mundur  beberapa langkah dan bersembunyi di balik pohon.
</div>
'''
    st.markdown(tulisan1,unsafe_allow_html=True)
    tulisan2='''
<div class="animated-border">
  “Dooor....” terdengar suara tembakan dari senjata api rakitan yang dibawa Pak Ardan. Tak lama kemudian,
  seekor macan tutul terkulai lemah tak berdaya. Macan tutul itu mati setelah dihantam peluru.
</div>
'''
    st.markdown(tulisan2,unsafe_allow_html=True)
    tulisan3='''
<div class="animated-border">
  Pak Ardan dan temannya menghampiri macan tutul tersebut. Mereka mengeluarkan sebilah pisau untuk mengambil
  kulit dan taring hewan tersebut. “Akhirnya dapat juga yang kita cari,” kata Pak Ardan kepada temannya.
  “Kita bisa segera menjualnya ke kota.”
</div>
'''
    st.markdown(tulisan3,unsafe_allow_html=True)
    tulisan4='''
<div class="animated-border">
  Setelah selesai menguliti macan tutul tersebut, Pak Ardan memasukkannya ke dalam karung yang telah
  disiapkan dari rumah. “Ayo, kita pulang!” kata Pak Ardan kepada temannya. Mereka segera melangkah meninggalkan
  hutan. Namun, baru beberapa langkah, tiba-tiba Pak Ardan dikagetkan oleh suara teriakan. “Berhenti! Angkat
  tangan!” teriak petugas kepolisian Taman Nasional. Aparat kepolisian mengamankan kedua pelaku perburuan macan tutul
  tersebut beserta barang bukti, berupa hasil perburuan yaitu kulit dan taring macan tutul.
</div>
'''
    st.markdown(tulisan4,unsafe_allow_html=True)
    tulisan5='''
<div class="animated-border">
  Setelah membaca cerita tersebut, Dayu mencoba menggali informasi tentang Macan Tutul Jawa.
  Berikut informasi yang didapatkan Dayu dari sebuah surat kabar
</div>
'''
    st.markdown(tulisan5,unsafe_allow_html=True)
    tulisan6='''
<div class="animated-border">
  Macan Tutul adalah hewan yang terancam punah akibat perburuan yang dilakukan warga setempat.
  Saat ini jumlah macan tutul hanya 200 ekor.  Berkurangnya jumlah macan tutul itu akibat adanya
  perburuan yang dilakukan warga sekitar. Mereka menjual kulit atau taringnya.  Selain itu, mereka
  juga memburu satwa langka lainnya, seperti burung, banteng, badak, penyu, dan ikan.
</div>
'''
    st.markdown(tulisan6,unsafe_allow_html=True)
    tulisan7='''
<div class="animated-border">
  Untuk mencegah perburuan hewan langka yang dilindungi, maka pihak Taman Nasional
  Ujung Kulon sudah beberapa kali menjelaskan kepada warga sekitar. Akan tetapi, hingga saat ini warga
  tetap belum menyadari pentingnya melindungi satwa langka itu supaya jangan punah
</div>
'''
    st.markdown(tulisan7,unsafe_allow_html=True)

# Tampilkan animasi di Streamlit
    st.markdown(html_code2, unsafe_allow_html=True)
with tab[1]:
    # HTML dan CSS untuk animasi teks
    html_code1 = """
<style>
  .animated-text {
    font-size: 3rem;
    font-weight: bold;
    color: black;
    text-align: justify;
    indent-text:40px;
    animation: glow 2s ease-in-out infinite, move 4s linear infinite;
  }

  /* Efek cahaya */
  @keyframes glow {
    0%, 100% {
      text-shadow: 0 0 10px #3498db, 0 0 20px #2980b9, 0 0 30px #8e44ad, 0 0 40px #9b59b6;
    }
    50% {
      text-shadow: 0 0 20px #e74c3c, 0 0 30px #c0392b, 0 0 40px #e67e22, 0 0 50px #f1c40f;
    }
  }

  /* Animasi gerakan */
  @keyframes move {
    0% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-20px);
    }
    100% {
      transform: translateY(0);
    }
  }
</style>

<div class="animated-text">Latihan</div>
"""

    # Menampilkan animasi di Streamlit
    st.markdown(html_code1, unsafe_allow_html=True)
    with st.container(border=True):
            # Elemen input di dalam container
            nama = st.text_input("Nama:",key='urut4')
            kelas = st.text_input("Kelas:",key='urut5')
            sekolah = st.text_input("Nama Sekolah:",key='urut6')
    st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732179623/soal_test_p9lghr.png")
    st.markdown('''
                <div><b>Petunjuk</b>
                <ol type="a">
                    <li>Selesaikan tugas menyenangkan berikut!</li>
                    <li>Tulis jawaban dengan benar dan jelas!</li>
                    <li>Soal-soal berikut berdasarkan teks bacaan yang berjudul “Hemat Air, Cara Mudah Menyelamatkan Bumi”.</li>
                </ol>
                </div>
                ''', unsafe_allow_html=True)
    tulisan_html3=f'''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .pertanyaan{{
            font-family:"comic sans ms";
            font-size:20px;
            margin:10px;
            color:blue;
        }}
        .pertanyaan1, .pertanyaan2{{
            font-size:18px;
            color:black;
            font-weight:bold;
            margin:5px;
        }}
        .pertanyaan3{{
            border:2px solid brown;
            width:300px;
            height:30px;
            background-color:white;
            border-radius:10px;
            font-size:15px;
            padding:3px;
        }}
        .pertanyaan3:hover{{
            background-color:yellow;
            border-radius:5px;
        }}
        .pertanyaan4, .pertanyaan5{{
            border-radius:10px;
            border:2px solid black;
            box-shadow:2px 2px 2px 2px green;
            background-color:white;
            font-size:15px;
            padding:3px;
        }}
        .pertanyaan4:hover, .pertanyaan5:hover{{
            background-color:cyan;
        }}
        .pertanyaan4:focus, .pertanyaan5:focus{{
            background-color:lightgoldenrodyellow;
            font-size:15px;
            padding:3px;
        }}
        #kirim1{{
            font-family:nroadway;
            font-size:20px;
            background-color:green;
            color:yellow;
        }}
    </style>
</head>
<body>
    <div>
        <div><input type="text" id="nama" value={nama}></div>
        <div><input type="text" id="kelas" value={kelas}></div>
        <div><input type="text" id="ns" value={sekolah}></div>
    </div>
    <div>
        <ol>
            <li class="pertanyaan"><b>Artikan kata-kata/kelompok kata berikutnya</b>
                <ol type="a">
                    <li class="pertanyaan1">a.	Hutan Lindung (baris 2)  =  <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Mengendap-endap (baris 3)  = = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Dihantam (baris 9)  = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Menguliti (baris 14)  =  <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Perburuan (baris 23) = <input class="pertanyaan3" type="text"></li>
                </ol>
            </li>
            <li class="pertanyaan"><b>Jawablah pertenyaan di bahwah ini</b>
                <ol type="a">
                    <li class="pertanyaan2"><div>Di mana kejadian yang ada dalam cerita tadi?</div>
                        <div><textarea class="pertanyaan5" cols="40" rows="5"></textarea></div>
                     </li>
                    <li class="pertanyaan2"><div>Kapan waktunya?</div>
                        <div><textarea class="pertanyaan5" cols="40" rows="5"></textarea></div>
                     </li>
                    <li class="pertanyaan2"><div>Bagaimana situasi dalam teks bacaan tersebut? </div>
                        <div><textarea class="pertanyaan5" cols="40" rows="5"></textarea></div>
                    </li>
                </ol>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan informasi-informasi penting dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Uraikan ide pokok dan ide penjelas dalam teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tentukan kalimat utama dalam teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Urutkan kejadian-kejadian dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan simpulan yang mengakibatkan Macan Tutul di Ujung Kulon terancam punah!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Ceritakan kembali dengan bahasamu sendiri isi cerita dalam teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Pernahkah kamu mengetahui cerita yang hampir sama seperti dalam teks tadi?
                Jika pernah, tuliskan informasi-informasi yang kamu temui dalam kehidupan
                sehari-hari yang hampir sama dengan teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Cerita dalam teks bacaan tadi banyak mengandung makna/nilai-nilai yang bisa
                kita tiru. Tuliskan nilai-nilai yang kamu pahami dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, apakah teks bacaan tadi jelas dan lengkap? Apa alasanmu?</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, jalan cerita yang dituliskan penulis sudah benar? Apa alasanmu?</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Berdasarkan cerita dalam teks tadi, apakah ada watak tokoh, tempat,
                kejadian dalam kehidupan sehari-hari? Jika ada, coba tuliskan!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, apakah isi cerita dalam teks tadi sesuai dengan kehidupan
                sehari-hari? Mengapa?</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Setelah membaca cerita tadi, apakah ada nilai/sifat yang perlu ditiru
                dan tidak boleh ditiru olehmu? Tuliskan nilai-nilai yang perlu ditiru dan
                tidak perlu ditiru olehmu, yang akan kamu  terapkan dalam kehidupan
                sehari-hari!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
        </ol>
    </div>
    <div><input id="kirim1" type="button" value="Kirim Jawaban" ></div>
    <script type="module">
            // Konfigurasi Firebase SDK
            import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
            const firebaseConfig = {{
                    apiKey: "AIzaSyCkgVmk75UTkos2y1Mrc7d3-sxShMfbeJQ",
                    authDomain: "natural-ethos-423713-e0.firebaseapp.com",
                    databaseURL: "https://natural-ethos-423713-e0-default-rtdb.firebaseio.com",
                    projectId: "natural-ethos-423713-e0",
                    storageBucket: "natural-ethos-423713-e0.firebasestorage.app",
                    messagingSenderId: "41833960811",
                    appId: "1:41833960811:web:6218d6ac2f3538c704e82e",
            }};

            // Inisialisasi Firebase
            const app = initializeApp(firebaseConfig);
            import {{getDatabase, set, get, update, remove, ref, child}}
                from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";
            const db=getDatabase()
            var kirim1 = document.getElementById("kirim1")
            kirim1.addEventListener("click",()=>{{
                var nama = document.getElementById("nama").value
                var kelas = document.getElementById("kelas").value
                var ns = document.getElementById("ns").value
                var soal1 = document.getElementsByClassName("pertanyaan3")
                var soal2 = document.getElementsByClassName("pertanyaan5")
                var soal3 = document.getElementsByClassName("pertanyaan4")
                set(ref(db, 'pemburuan_hewan/' + nama), {{ 
                    nama:nama,
                    kelas:kelas,
                    ns:ns,
                }})
                    .then(() => {{
                        alert('Data added successfully');
                    }})
                    .catch((error) => {{
                    console.error("Error adding data:", error);
                }});
                set(ref(db, 'pemburuan/' + nama+'/soal'), {{ 
                    soal1a:soal1[0].value,
                    soal1b:soal1[1].value,
                    soal1c:soal1[2].value,
                    soal1d:soal1[3].value,
                    soal1e:soal1[4].value,
                    soal2a:soal2[0].value,
                    soal2b:soal2[1].value,
                    soal2c:soal2[2].value,
                    soal3:soal3[0].value,
                    soal4:soal3[1].value,
                    soal5:soal3[2].value,
                    soal6:soal3[3].value,
                    soal7:soal3[4].value,
                    soal8:soal3[5].value,
                    soal9:soal3[6].value,
                    soal10:soal3[7].value,
                    soal11:soal3[8].value,
                    soal12:soal3[9].value,
                    soal13:soal3[10].value,
                    soal14:soal3[11].value,
                    soal15:soal3[12].value
                }})
                    .then(() => {{
                        alert('Data added successfully');
                    }})
                    .catch((error) => {{
                    console.error("Error adding data:", error);
                }});
            }});

    </script>
</body>
</html>
'''
    st.components.v1.html(tulisan_html3,width=1000,height=13000)
    
    



