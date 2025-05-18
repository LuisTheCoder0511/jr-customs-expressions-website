replacement()

document.getElementById('imageInput').addEventListener('change', function(event) {
    const fileInput = event.target;
    const files = fileInput.files;

    if (!files || files.length === 0) {
        // No file selected, so do nothing (and keep the previous one, if needed)
        return;
    }

    const file = files[0];

    if (file.type.startsWith('image/')) {
        const reader = new FileReader();

        reader.onload = function(e) {
            const preview = document.getElementById('preview');
            preview.src = e.target.result;
            preview.style.display = 'block';
        };

        reader.readAsDataURL(file);
    } else {
        alert("Please select a valid image file.");
    }
});