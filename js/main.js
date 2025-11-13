console.log("Try On Makeup ready! 💄");

// Tombol kamera
const video = document.getElementById("video");
const toggleBtn = document.getElementById("toggleCameraBtn");

if (toggleBtn && video) {
  toggleBtn.addEventListener("click", async () => {
    if (video.srcObject) {
      video.srcObject.getTracks().forEach(t => t.stop());
      video.srcObject = null;
      toggleBtn.textContent = "Start Camera";
    } else {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
        toggleBtn.textContent = "Stop Camera";
      } catch (err) {
        alert("Gagal mengakses kamera 😢");
        console.error(err);
      }
    }
  });
}

let slideIndex = 0;
showSlides();

function showSlides() {
  const slides = document.querySelectorAll(".slide");
  const dots = document.querySelectorAll(".dot");
  slides.forEach((s) => s.style.opacity = "0");
  dots.forEach((d) => d.classList.remove("active-dot"));

  slideIndex++;
  if (slideIndex > slides.length) { slideIndex = 1; }

  slides[slideIndex - 1].style.opacity = "1";
  dots[slideIndex - 1].classList.add("active-dot");

  setTimeout(showSlides, 3000); // Ganti slide setiap 3 detik
}

function currentSlide(n) {
  slideIndex = n - 1;
  showSlides();
}
