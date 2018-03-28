function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
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

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$("#save").click(function() {
    var myObject = new Object();
    myObject.con_001 = $("input[name='bg_color']:checked").val();
    console.log($("input[name='bg_color']:checked").val());
    var my_url = window.location.href;
    my_key = my_url.split("index")[1].split('/')[1];
    var myString = JSON.stringify(myObject);
    $.ajax({
        type: "POST",
        url: '/ajax/save/' + my_key + '/',
        success: console.log('sent json'),
        dataType: 'json',
        data: myString,
    });
});

$("#make").click(function() {
    var my_url = window.location.href;
    my_key = (my_url.split("index")[1]).split('/')[1]
    $.ajax({
        type: "POST",
        url: '/ajax/make/' + my_key + '/',
        success: console.log('sent command'),
        dataType: 'text',
        data: 'make',
    });
});

$("#run").click(function() {
    var my_url = window.location.href;
    my_key = (my_url.split("index")[1]).split('/')[1]
    $.ajax({
        type: "POST",
        url: "/ajax/run/" + my_key + '/',
        success: console.log('sent run'),
        dataType: 'text',
        data: 'run',
    });
});

$("#view").click(function() {
    var my_url = window.location.href;
    my_key = (my_url.split("index")[1]).split('/')[1]
    $.ajax({
        type: "GET",
        url: '/ajax/view/' + my_key + '/',
        success: console.log('sent command'),
        dataType: 'text',
        data: 'view',
    });
});


$("#kill").click(function() {
    var my_url = window.location.href;
    my_key = (my_url.split("index")[1]).split('/')[1]
    $.ajax({
        type: "POST",
        url: '/ajax/kill/' + my_key + '/',
        success: console.log('sent command'),
        dataType: 'text',
        data: 'kill',
    });
});

























