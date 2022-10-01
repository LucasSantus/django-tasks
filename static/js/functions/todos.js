const build_html = ( item ) => `
    <div class="d-flex bg__primary rounded__custom container mt-2 p-3">
        <div class="form-check">
            <input class="form-check-input" type="checkbox" id="checkbox_task">
            <label class="form-check-label" for="checkbox_task"></label>
        </div>
        <div class="ps-3 w-100 d-flex align-items-center justify-content-between">
            <div>
                <a href="${item.redirect}" class="text-decoration-none text-white"> ${ item.title } </a>
            </div>
            <div class="d-flex gap-2">
                <a href="${item.redirect}" class="d-flex align-items-center text-decoration-none hover">
                    <span class="material-icons text-white border rounded-3 fs-5 p-1">edit</span>
                </a>
                <a href="${item.redirect}" class="d-flex align-items-center text-decoration-none hover">
                    <span class="material-icons text-white border rounded-3 fs-5 p-1">add</span>
                </a>
            </div>
        </div>
    </div>
`;

const build_todo = ( item, id ) => $( build_html(item) ).appendTo("#" + id);

const remove_class = ( element, items ) => {
    for( let item of items ) $(element).removeClass(item);
}

const get_all_todos = ( method, response, id ) => {
    let values = method === "GET" ? 
        JSON.parse(response) : JSON.parse(response["data"])[0]["fields"];

    if( values.length > 1 ){
        for( let item of values ) build_todo(item, id);
    } else {
        if( values.length != 0 ) build_todo(values, id);
    }

    $('.modal').modal('hide');

    remove_class( ".form-control", [ 'is-valid', 'is-invalid' ] );
}