/**
 * function constructor button elements.
 * @param string url 
 * @param string color 
 * @param string icon 
 * @param string id 
 * @returns string
 */
const build_button = ( url, color, icon, id ) => `
    <a href="${ url }" data-bs-toggle="modal" data-bs-target="#modal-${id}" class="d-flex align-items-center text-decoration-none border border-${ color } rounded-3 hover">
        <span class="material-icons text-${ color } fs-5 p-1">${ icon }</span>
    </a>
`;

/**
 * function constructor html elements.
 * @param {*} item 
 * @returns 
 */
const build_html = ( item ) => {
    const buttons = [
        { id: `change-${item.id}`, url: "#", color: "info", icon: "edit" },
        { id: `delete-${item.id}`, url: "#", color: "danger", icon: "delete" }
    ]

    return `
        <div id="id_task_${ item.id }" class="d-flex align-items-center bg__primary rounded__custom container mt-2 p-3">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="checkbox_task_${ item.id }">
                <label class="form-check-label" for="checkbox_task_${ item.id }"></label>
            </div>
            <div class="ps-3 w-100 d-flex justify-content-between">
                <div>
                    <a id="title_${item.id}" href="${item.redirect}" class="text-decoration-none text-white"> ${ item.title } </a>
                </div>
                <div class="d-flex gap-2">
                    ${buttons.map((option) => build_button(option.url, option.color, option.icon, item.id))}
                </div>
            </div>
            
            <div class="modal fade" id="modal-${ item.id }" tabindex="-1" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-body">
                            <div class="d-flex flex-column justify-content-center text-center gap-4">
                                <section>
                                    <span class="material-icons text-info border-info rounded-pill p-3" style="font-size: 80px; border-width: 10px; border-style: solid">edit</span>
                                </section>                                
                                <span>Deseja realmente deletar?</span>
                                <button type="button" class="btn btn__primary hover">Confirmar</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `
};

/**
 *  function prepare validation 
 * @param string element 
 * @param string[] items 
 */
const prepare_validation = ( element, items ) => {
    for( let item of items ) $(element).removeClass(item);
}

const check_item = ( item ) => {
    $(`#checkbox_task_${ item.id }`).click(function () {
        if($(this).is(':checked')){
            $.ajax({
                type: "POST",
                url: item.get_url_change_status,
                data: item,
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                beforeSend: ( ) => {
                    hold_start("Aguarde um momento, estamos finalizando sua task");
                },
                success: function( response ){
                    hold_close();

                    // $(`#id_task_${item.id}`).remove();
                },
                error: ( ) => {
                    hold_close();
                }
            });
        } 
        else {
            $(`#title_${item.id}`).removeClass("text-decoration-line-through");
        }
    })
}

const build_tasks = ( method, response, id ) => {
    let items = method === "GET" ? 
        JSON.parse(response) : JSON.parse(response["data"])[0]["fields"];

    if( items.length > 0 ) {
        items.forEach((item) => {
            $( build_html(item) ).appendTo("#" + id);
            check_item( item );
        });
    } else {
        $( build_html(items) ).appendTo("#" + id);
        check_item(items);
    }

    $('.modal').modal('hide');

    prepare_validation( ".form-control", [ 'is-valid', 'is-invalid' ] );
}
