const searchForm = document.getElementById("searchForm");
const searchBox = document.getElementById("searchBox");
const searchButton = document.getElementById("searchButton");
const memberName = document.getElementById("memberName");

async function searchMember() {
    let username = searchBox.value.trim();
    let response = await fetch(`/api/member?username=${username}`, {
        method: 'GET',
        headers: {
            "Content-Type": "application/json"
        }
    });
    let data = await response.json();
    if (data.data===null) {
        memberName.textContent = "No Data";
    } else {
        memberName.textContent = `${data.data.name} (${data.data.username})`;
    }
}

searchButton.addEventListener("click", () => {
    if (!searchBox.value.trim()) {
        alert("請輸入會員帳號")
    } else {
        searchMember();
    }
})

