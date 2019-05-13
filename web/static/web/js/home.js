function addItem() {
    var li = document.createElement("LI");
    var input = document.getElementById("add");
    li.innerHTML = input.value;
    input.value = "";

    document.getElementById("prod").appendChild(li);
}

// function create_post() {
//     console.log("create post is working!") // sanity check
//     $.ajax({
//         url: "create_post/", // the endpoint
//         type: "POST", // http method
//         data: {
//             csrfmiddlewaretoken: '{{ csrf_token }}',
//             the_post: $('#gramatica-1').val()
//         }, // data sent with the post request
//
//         // handle a successful response
//         success: function (json) {
//             $('#post-text').val(''); // remove the value from the input
//             console.log(json); // log the returned json to the console
//             console.log("success"); // another sanity check
//         },
//
//         // handle a non-successful response
//         error: function (xhr, errmsg, err) {
//             $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
//                 " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//             console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//         }
//     });
// };

function create_post() {
    // console.log($("form").serializeArray());
    $.ajax({
        type: 'POST',
        url: '/home/create_post/',
        data: {the_post: $('#gramatica-1').val()},
        dataType: 'json',
        encode: true,
        crossDomain: false,
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function (data) {
            console.log(data);
        },
        error: function () {
            // alert('Deu Erro');
            console.log('Deu Erro');
        }
    });
    event.preventDefault();

    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
};