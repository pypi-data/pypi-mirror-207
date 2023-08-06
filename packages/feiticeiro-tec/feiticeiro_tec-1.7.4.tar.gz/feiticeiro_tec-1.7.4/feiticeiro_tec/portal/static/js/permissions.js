const update_list = {}
new gridjs.Grid({
    columns: [
        {
            name: 'Endpoint',
        },
        {
            name: 'Rota',
        },
        {
            name: 'Method',
        },
        {
            name: 'Atualizado em',
            formatter: (cell) => {
                const date = new Date(cell).toLocaleString();
                return `${date}`;
            },
        },
        {
            name: 'Status',
            formatter: (cell) => {
                let icon = (cell.is_delete) ? '<i class="bi bi-x-circle text-danger ml" title="Rota Desativada Pelo Sistema"></i>' : '<i class="bi bi-check-circle text-secundary ml" title="Rota Disponivel"></i>';
                let is_active = (cell.is_active && !update_list[cell.id]) ? 'checked' : '';

                let $button = $(`<button class="toggle-permissions" data-id="${cell.id}">`)
                $button.addClass(is_active)
                $button.html(`
                        <i class="bi bi-toggle-on " title="Rota aberta para uso"></i>
                        <i class="bi bi-toggle-off text-white" title="Rota desativada para uso"></i>
                    `)

                init_element_toggle(cell.id)

                return gridjs.html(`
                    <div class="d-flex gap-2 m-auto justify-content-center">
                    ${$button[0].outerHTML}
                    ${icon}
                    </div>
                    `)
            }
        }
    ],
    server: {
        url: '/v1/permissions/',
        headers: {
            "X-Fields": "id,endpoint,rule,method,update_time,is_active,is_delete"
        },
        then: data => data.map(row => [
            row.endpoint, row.rule, row.method, row.update_time, row
        ])
    },
    search: true,
    pagination: {
        enabled: true,
        limit: 10,
        summary: true
    },
    width: '100%',
    height: '100%',
    sort: true,
    resizable: true,
    language: {
        search: {
            placeholder: 'Pesquisar...'
        },
        pagination: {
            next: 'Próximo',
            previous: 'Anterior',
            showing: 'Exibindo',
            results: 'resultados',
            to: 'a'
        },
        noRecordsFound: 'Nenhum registro encontrado',
    }
}).render(document.getElementById("permissions"));

function init_element_toggle(id) {
    setTimeout(function () {
        let button = $(`button[data-id="${id}"]`)
        console.log(button)
        togglePermissions(button)
    }, 100
    )
}
const toogle_action = element => {
    let is_active = element.hasClass('checked')
    let id = element.attr('data-id')
    let url = `/v1/permissions/${id}`
    let method = 'PUT'
    let data = {
        is_active: !is_active
    }
    $.ajax({
        url: url,
        method: method,
        data: data,
        success: function (data) {
            element.toggleClass('checked')
            if (update_list[id]) {
                delete update_list[id]
            } else {
                update_list[id] = true
            }

        }
    })
}
function call_func(element, call) {
    return call(element)
}
function togglePermissions(element) {
    element.off()
    element.click(() => { call_func(element, toogle_action) })
}