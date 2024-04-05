function toggleText(id) {
    var elem = document.getElementById(id);
    var moreLink = elem.querySelector(".more");
    var additionalContent = elem.querySelector(".additional-content");

    // Check if the additional content is currently hidden
    if (additionalContent.style.display === "none" || additionalContent.style.display === "") {
        // Show additional content
        additionalContent.style.display = 'block';
        // Update the link text
        moreLink.textContent = "Read less";
    } else {
        // Hide additional content
        additionalContent.style.display = 'none';
        // Update the link text
        moreLink.textContent = "Read more";
    }
}

// Function to limit the number of words displayed initially
function limitWords(element, limit) {
    var text = element.textContent.trim(); // Trim to remove leading/trailing whitespace
    var words = text.split(' ');
    if (words.length > limit) {
        var truncatedText = words.slice(0, limit).join(' ') + '...';
        element.innerHTML = truncatedText + ' <span class="more" onclick="toggleText(this.parentElement.parentElement.id)">Read more</span>';
    }
}

// Limit the words for each FAQ answer
var faqElements = document.querySelectorAll('.text-myBlack p');
faqElements.forEach(function (element) {
    limitWords(element, 25); // Change 25 to desired word limit
});
