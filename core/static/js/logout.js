function checkLogin() {
  const token = localStorage.getItem("access_token");
  if (token) {
    // کاربر لاگین هست → عکس پروفایل نشون بده
    document.getElementById("user-avatar").style.display = "block";
    document.getElementById("auth-links").style.display = "none";
  } else {
    // کاربر لاگین نیست → لینک login/register نشون بده
    document.getElementById("user-avatar").style.display = "none";
    document.getElementById("auth-links").style.display = "block";
  }
}

function logout() {
  // پاک کردن توکن‌ها
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");

  // برو صفحه لاگین و منو رو به‌روزرسانی کن
  document.getElementById("user-avatar").style.display = "none";
  document.getElementById("auth-links").style.display = "block";
  window.location.href = "/account/login/";
}

// هنگام لود صفحه بررسی کن وضعیت لاگین
checkLogin();