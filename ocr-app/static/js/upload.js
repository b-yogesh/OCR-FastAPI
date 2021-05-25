function perform_OCR(){
    var file = document.getElementById("image_file").files
    var endpoint = "/perform_OCR"
    var formData = new FormData()
    formData.append('image', file[0])

    $.ajax({
        type:'POST',
        url: endpoint,
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        success: function(data){
            console.log(data.is_success)
            var x = document.getElementById("overlayed_image")
            if (x.style.display === "none") {
                x.style.display = "block"
                $(".image_1").attr('src', "static/temp/overlayed_image.png")
            } else {
                x.style.display = "none"
                $(".image_1").attr('src', "#")
            }
        }
    })
}

