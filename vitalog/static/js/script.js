document.addEventListener("DOMContentLoaded", function () {
    if (window.innerWidth <= 768) { // Check if screen width is less than or equal to 768px (adjust as needed)
        const toggles = document.querySelectorAll('.toggleText');
        toggles.forEach(toggle => {
            const moreBtn = toggle.querySelector('.more');
            moreBtn.addEventListener('click', function () {
                const additionalContent = toggle.querySelector('.additional-content');
                if (additionalContent.style.display === "none" || additionalContent.style.display === "") {
                    additionalContent.style.display = 'block';
                    moreBtn.textContent = "Read less";
                } else {
                    additionalContent.style.display = 'none';
                    moreBtn.textContent = "Read more";
                }
            });
        });
    }
});