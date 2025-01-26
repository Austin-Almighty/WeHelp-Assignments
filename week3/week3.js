const burger = document.getElementById("burger");
const popupMenu = document.getElementById("popupMenu");
const closeMenu = document.getElementById("closeMenu");

burger.addEventListener("click", () => {
  popupMenu.style.right = "0";
});

closeMenu.addEventListener("click", () => {
  popupMenu.style.right = "-100%";
});

const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";


function fetchData(url) {
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        const results = data.data.results;
  
        // Extract the first 13 `stitle` values
        const stitles = [];
        for (let i = 0; i < 13; i++) {
          stitles.push(results[i].stitle);
        }
  
        const img = [];
        for (let i = 0; i < 13; i++) {
          // Split the filelist string into an array of URLs
          const urls = results[i].filelist
            .split(/https?:\/\//)
            .map((url) => `https://${url.trim()}`);
  
          // Find the first URL that ends with .jpg
          const firstJpgUrl = urls.find((url) => url.endsWith(".jpg"));
  
          // Push the first valid .jpg URL to the img array
          if (firstJpgUrl) {
            img.push(firstJpgUrl);
          }
        }
  
        // Add `stitle` values to the correct positions in the DOM
        const smallFirstDivs = document.querySelectorAll(".top"); // First 3 positions
        const titleDivs = document.querySelectorAll(".title"); // Next 10 positions
        
        for (let i = 0; i < smallFirstDivs.length && i < 3; i++) {
            const newIMG = document.createElement("img");
            newIMG.src = img[i];
            smallFirstDivs[i].appendChild(newIMG);
          }

        for (let i = 0; i < smallFirstDivs.length && i < 3; i++) {
          const newDiv = document.createElement("div");
          newDiv.textContent = stitles[i];
          smallFirstDivs[i].appendChild(newDiv);
        }
  
        // Populate the next 10 positions under `.title`
        for (let i = 0; i < titleDivs.length && i < 10; i++) {
          const newDiv = document.createElement("div");
          newDiv.textContent = stitles[i + 3];
          newDiv.className = "text-box";
          titleDivs[i].appendChild(newDiv);
        }
  
        
  
        // Select all `.title` elements
        const titleElements = document.querySelectorAll(".title");
  
        // Replace the background-image of each `.title` element with the next 10 images from the `img` array
        for (let i = 0; i < titleElements.length && i < 10; i++) {
          if (img[i + 3]) {
            // Start from the 4th image since the first 3 are used elsewhere
            titleElements[i].style.backgroundImage = `url('${img[i + 3]}')`;
          }
        }
      });
  }

  fetchData(url);