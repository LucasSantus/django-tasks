const build_button = ( url, color, icon, id ) => `
    <a href="${ url }" data-bs-toggle="modal" data-bs-target="#modal-delete-${id}" class="d-flex align-items-center text-decoration-none bg-${ color } border border-${ color } rounded-3 hover">
        <span class="material-icons text-white fs-5 p-1">${ icon }</span>
    </a>
`;

const build_html = ( item ) => {
    console.log(item)

    const buttons = [
        { id: `change-${item.id}`, url: "#", color: "info", icon: "edit" },
        { id: `delete-${item.id}`, url: "#", color: "danger", icon: "delete" }
    ]

    return `
        <div id="id_task_${ item.id }" class="d-flex align-items-center bg__primary rounded__custom container mt-2 p-3">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="checkbox_task">
                <label class="form-check-label" for="checkbox_task"></label>
            </div>
            <div class="ps-3 w-100 d-flex justify-content-between">
                <div>
                    <a href="${item.redirect}" class="text-decoration-none text-white"> ${ item.title } </a>
                </div>
                <div class="d-flex gap-2">
                    ${buttons.map((option) => build_button(option.url, option.color, option.icon, item.id))}
                </div>
            </div>
            
            <div class="modal fade" id="modal-delete-${ item.id }" tabindex="-1" aria-labelledby="modal-delete-${ item.id }-label" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="modal-delete-${ item.id }-label">Modal title</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            Deseja realmente deletar?
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary">Save changes</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `
};

const prepare_validation = ( element, items ) => {
    for( let item of items ) $(element).removeClass(item);
}

const build_tasks = ( method, response, id ) => {
    let values = method === "GET" ? 
        JSON.parse(response) : JSON.parse(response["data"])[0]["fields"];
    
    for( let item of values ) $( build_html(item) ).appendTo("#" + id);
    
    $('.modal').modal('hide');

    prepare_validation( ".form-control", [ 'is-valid', 'is-invalid' ] );
}