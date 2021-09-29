const delay_by_in_ms = 500
let scheduled_function = false
const endpoint = '/ajax/comps'

function get_ajax(campo, input, list) {

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    
    scheduled_function = setTimeout(function (endpoint, request_parameters) {
        $.getJSON(endpoint, request_parameters).done(response => {
            $(list).html(response['html_componentes'])
        })
    }, delay_by_in_ms, endpoint, {c: campo, n: $(input).val()})
}