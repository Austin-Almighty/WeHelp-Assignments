const searchForm = document.getElementById("searchForm");
const searchBox = document.getElementById("searchBox");
const searchButton = document.getElementById("searchButton");
const memberName = document.getElementById("memberName");

async function searchMember(event) {
  event.preventDefault();
  let username = searchBox.value.trim();
  let response = await fetch(`/api/member?username=${username}`, {
    method: "GET",
    credentials: "include",
  });

  if (response.redirected) {
    memberName.textContent = "You are not logged in";
    return;
  }

  if (response.ok) {
    let data = await response.json();
    if (data.data === null) {
      memberName.textContent = "No Data";
    } else {
      memberName.textContent = `${data.data.name} (${data.data.username})`;
    }
  } else {
    console.error("Server Error");
  }
}

const updateForm = document.getElementById("updateForm");
const updateBox = document.getElementById("updateBox");
const updateButton = document.getElementById("updateButton");
const updateStatus = document.getElementById("updateStatus");

async function updateName(event) {
    event.preventDefault();
    
    let newName = updateBox.value.trim();
    if (!newName) {
        updateStatus.textContent = "Please enter a new name"
        return;
    }
    let response = await fetch(
        '/api/member',
        {
            method: "PATCH",
            credentials: "include",
            body: JSON.stringify({"name":newName}),
            headers: {
                'Content-Type': 'application/json'
            }
        }
    );
    if (response.redirected) {
        updateStatus.textContent = "You are not logged in";
        return;
      }

    if (response.ok) {
        let data = await response.json();
        if (data.ok) {
            updateStatus.textContent = "Updated";
        } else {
            updateStatus.textContent = "Failed to Update";
        }
    }
}
