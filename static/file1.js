$("button").on("click", function () {
    $.ajax({
        url: "http://localhost:5000/api/imageName",
        success: function (data) {
            console.log(data);
            $("div").append($("<img>", { src: "/static/images/" + data.image_name }));
        }
    });
});