function uploadImage() {
    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    fetch("/upload/", {
        method: "POST",
        body: formData,
    })
    .then(res => res.json())
    .then(data => {
        const img = document.getElementById("resultImage");
        img.src = data.processed_url + "?t=" + new Date().getTime(); // prevent caching
        img.style.display = "block";
    });
}
