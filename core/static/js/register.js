document.addEventListener('DOMContentLoaded', function () {
  const registerForm = document.getElementById('register-form');
  if (registerForm) {
    registerForm.addEventListener('submit', async function (event) {
      event.preventDefault();

      const username = document.getElementById('user_name').value;
      const email = document.getElementById('email').value;
      const password1 = document.getElementById('password1').value;
      const password2 = document.getElementById('password2').value;

      try {
        const response = await fetch('/account/api/v1/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            user_name:username,
            email: email,
            password: password1,
            password_confirm: password2
          })
        });

        const data = await response.json();

        if (response.ok) {
          alert('✅ ثبت‌نام موفق! لطفاً ایمیل خود را برای فعال‌سازی بررسی کنید.');
          window.location.href = '/account/login'; 
        } else {
          alert('❌ خطا: ' + JSON.stringify(data));
        }
      } catch (error) {
        console.error(error);
        alert('⚠️ خطای شبکه! لطفاً دوباره تلاش کنید.');
      }
    });
  }
});