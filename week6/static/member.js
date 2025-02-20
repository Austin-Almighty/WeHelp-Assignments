const comment_form = document.getElementById("comment_form");
const comment_box = document.getElementById("comment_box");
const comment_button = document.getElementById("comment_button");
const comment = document.getElementById("comment");

comment_button.addEventListener("click", () => {
    if (comment_box.value.trim().length === 0) {
        alert("請先輸入留言")
    } else {
        comment_form.submit();
    }
})

const deleteButtons = document.querySelectorAll(".delete_button");

deleteButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      const userConfirmed = confirm("確定要刪除訊息嗎？");
      
      if (!userConfirmed) {
        event.preventDefault(); 
      }
    });
  });
