document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".rating").forEach(function (ratingElement) {
        let rating = parseFloat(ratingElement.getAttribute("data-rating"));  // Puanı al
        let maxStars = 5;
        let scaledRating = (rating / 10) * maxStars; // 10 üzerinden geleni 5'e çevir
        let starsHtml = "";

        for (let i = 1; i <= maxStars; i++) {
            if (scaledRating >= i) {
                starsHtml += `<i class="bx bxs-star"></i>`; // Tam yıldız
            } else if (scaledRating >= i - 0.5) {
                starsHtml += `<i class="bx bxs-star-half"></i>`; // Yarım yıldız
            } else {
                starsHtml += `<i class="bx bx-star"></i>`; // Boş yıldız
            }
        }

        ratingElement.innerHTML = starsHtml;
    });
});