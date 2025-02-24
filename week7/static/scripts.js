const register_form = document.getElementById("register");
const register_name = document.getElementById('register_name');
const register_username = document.getElementById("register_username");
const register_password = document.getElementById('register_password');
const register_button = document.getElementById('register_button');


const login_form = document.getElementById("login");
const login_username = document.getElementById('login_username');
const login_password = document.getElementById('login_password');
const login_button = document.getElementById('login_button');


register_button.addEventListener("click", () => {
    if (!register_name.value.trim() || !register_password.value.trim() || !register_username.value.trim()) {
        alert("註冊前，請確實輸入姓名、帳號、密碼")
    } else {
        register_form.submit();
    }
})

login_button.addEventListener("click", () => {
    if (!login_username.value.trim() || !login_password.value.trim()) {
        alert("請輸入帳號和密碼")
    } else {
        login_form.submit();
    }
})


