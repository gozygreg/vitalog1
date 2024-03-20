function toggleText(id) {
    var elem = document.getElementById(id);
    var paragraphs = elem.getElementsByTagName("p");
    var moreLink = elem.getElementsByClassName("more")[0];

    // Check if the additional paragraphs are currently hidden
    if (paragraphs[1].style.display === "none") {
        // Show additional paragraphs
        for (var i = 1; i < paragraphs.length; i++) {
            paragraphs[i].style.display = 'block';
        }
        // Update the link text
        moreLink.textContent = "Read less";
    } else {
        // Hide additional paragraphs
        for (var i = 1; i < paragraphs.length; i++) {
            paragraphs[i].style.display = 'none';
        }
        // Update the link text
        moreLink.textContent = "Read more";
    }
}

