$(function() {
    $("#btn").click(function() {
        userPrompt = $("#input").val()
        $("#output").val("")
        if (userPrompt) {
            $.ajax({
                type : "POST",
                url : '/',
                dataType: "json", // expect json
                data: {
                    "input" : userPrompt
                },
                contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                success: function (data) {
                    $("#output").val(data.text)
                    }
                });
        }
        else {
            alert("Empty prompt")
        }
      });
});