document.addEventListener("DOMContentLoaded", function() {
  const categorySelect = document.getElementById("category");
  const subredditSelect = document.getElementById("subreddits");

  categorySelect.addEventListener("change", async function() {
    const category = categorySelect.value;

    // Clear out old subreddit options
    subredditSelect.innerHTML = '<option value="">-- Select a Subreddit --</option>';

    if (!category) return; // If no category selected, do nothing

    const url = "https://hook.us1.make.com/1cjtct7hjz7qyqi0pb3es26onuoqowe1?category=" + encodeURIComponent(category);

    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const apiResponse = await response;
      const data = apiResponse.split(',');
      // const data = await response.json(); // expecting array like ["r/example1","r/example2"]
console.log(data);
      // Populate subreddit dropdown
      data.forEach(subreddit => {
        const option = document.createElement("option");
        option.value = subreddit;
        option.textContent = subreddit;
        subredditSelect.appendChild(option);
      });
    } catch (error) {
      console.error("Error fetching subreddits:", error);
    }
  });
});

var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
