const nav_bar = document.getElementById("navbar");
const menuBtn = document.querySelector(".menu-btn");
const closeBtn = document.querySelector(".close-btn");
let prevScrollpos = window.pageYOffset;

menuBtn.addEventListener("click", () => {
  nav_bar.classList.add("active2");
});

closeBtn.addEventListener("click", () => {
  nav_bar.classList.remove("active2");
});

window.onscroll = function () {
  let currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("nav").style.top = "0";
  } else {
    document.getElementById("nav").style.top = "-120px";
  }
  prevScrollpos = currentScrollPos;
};
