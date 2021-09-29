const delay_by_in_ms = 500
let scheduled_function = false
const endpoint = '/ajax'

function get_ajax(campo, input, list) {

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    const request_parameters = {
        c: campo,
        n: $(input).val()
    }
    let datalist = $(list)
    
    scheduled_function = setTimeout(function (endpoint, request_parameters) {
        $.getJSON(endpoint, request_parameters).done(response => {
            datalist.html(response['html_componentes'])
        })
    }, delay_by_in_ms, endpoint, request_parameters)
}