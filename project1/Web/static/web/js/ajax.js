const queryString = window.location.search;
let scheduled_function = false
const delay_by_in_ms = 500

function get_abstract(path, dict, list) {
    if (scheduled_function) {clearTimeout(scheduled_function)}
    
    scheduled_function = setTimeout(function (endpoint, request_parameters) {
        $.getJSON(endpoint, request_parameters).done(response => {
            $(list).html(response['html_response'])
        })
    }, delay_by_in_ms, path, dict)
}

let last_comp = ""

function get_comps(comps, input, list) {
    if ($(input).val() == last_comp)
        return
    dict = {
        c: comps,
        n: $(input).val()
    }
    get_abstract('/ajax/comps', dict, list)
}

function get_details(comps, name, list) {
    dict = {
        c: comps,
        n: name,
        m: true
    }
    show_overlay()
    get_abstract('/ajax/comps', dict, list)
}

function get_build(page, list) {
    dict = {
        p: page
    }
    get_abstract('/ajax/build', dict, list)
}

function get_user(page, list) {
    dict = {
        u: true,
        p: page
    }
    get_abstract('/ajax/build', dict, list)
}

function build_search(page, list) {
    form = document.forms['search']
    dict = {
        gpu: form['tarjetavideo'].value,
        pro: form['procesador'].value,
        pla: form['placamadre'].value,
        n: form['name'].value,
        u: form['user'].value,
        p: page
    }
    get_abstract('/ajax/search', dict, list)
}