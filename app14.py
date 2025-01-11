import streamlit as st
st.set_page_config(
    page_title="Aplikasi Streamlit",
    page_icon="✨",
    layout="wide",  # Menggunakan lebar penuh layar
    initial_sidebar_state="expanded"  # Sidebar terbuka secara default
)
st.title("Pemeriksaan Soal")

tulisan_html='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Firebase Select Box</title>
</head>
<body>
  <h1>Daftar Pengguna</h1>
  <div><input type="button" value="reset" id="reset"></div>
  <select id="userSelect"></select>
  <div><ol id="konsep"></ol></div>
  <script type="module">
    // Import Firebase Library
    
    import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
    import { getDatabase, ref, get } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";
    
    // Konfigurasi Firebase
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
    const db = getDatabase(app);

    // Referensi ke Realtime Database
    const usersRef = ref(db, 'hemat_air');

    // Mendapatkan data dan memasukkan ke dalam select box
    const userSelect = document.getElementById('userSelect');
    function jalankan(){
        get(usersRef).then((snapshot) => {
      if (snapshot.exists()) {
        const users = snapshot.val();
        // Iterasi melalui data
        userSelect.innerHTML = ""
        Object.keys(users).forEach((key) => {
          const option = document.createElement('option');
          option.value = key; // Menyimpan kunci
          option.textContent = users[key].nama; // Menampilkan nama
          userSelect.appendChild(option);
        });
      } else {
        console.log('Data tidak ditemukan!');
      }
    }).catch((error) => {
      console.error('Terjadi kesalahan:', error);
    });
}
jalankan();
document.getElementById("reset").addEventListener("click",()=>{
    jalankan();
})
const konsep = document.getElementById("konsep")
userSelect.addEventListener("change",()=>{
    const keluaran = userSelect.value
    const usersRef1 = ref(db, 'hemat_air/'+keluaran);
    get(usersRef1).then((snapshot) => {
      if (snapshot.exists()) {
        const users = snapshot.val();
        
        // Iterasi melalui data
        konsep.innerHTML = ""
        const kumpulan=["soal1a","soal1b","soal1c","soal1d","soal1e","soal2a","soal2b","soal2c","soal3","soal4","soal5","soal6","soal7","soal8","soal9","soal10","soal11","soal12","soal13","soal14","soal15"]
        kumpulan.forEach((e)=>{
            const li = document.createElement('li');
            li.innerHTML = "<span style='border:1px solid black;background-color:yellow;display:inline-block;width:30%;margin:10px;padding:5px'>"+e+"</span>:<span style='border:1px solid black;color:white;background-color:blue;display:inline-block;width:60%;margin:10px;padding:5px'>"+users.soal[e]+"</span>";
            konsep.appendChild(li);
        })
        
        
      } else {
        console.log('Data tidak ditemukan!');
      }
    }).catch((error) => {
      console.error('Terjadi kesalahan:', error);
    });
})
  </script>
</body>
</html>
'''
st.components.v1.html(tulisan_html,width=1200,height=1500)
