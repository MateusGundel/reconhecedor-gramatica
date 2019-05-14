function addItem() {
    var li = document.createElement("LI");
    var input = document.getElementById("add");
    li.innerHTML = input.value;
    input.value = "";

    document.getElementById("producao").appendChild(li);
    // console.log(document.querySelector("#producao").children);
}

function create_post() {
    // console.log($("form").serializeArray());
    let val = [];
    [...document.querySelector("#producao").children].forEach(function (item) {
        val.push(item.textContent);
    })
    console.log(val)
    $.ajax({
        type: 'POST',
        url: '/create_post/',
        data:{'gramatica-nao-terminal': $('#gramatica-1').val(),
            'gramatica-terminal': $('#gramatica-2').val(),
            'producoes': val,},
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