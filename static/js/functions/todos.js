const build_html = ( item ) => `<div class="bg-danger w-100"> ${ item.title } </div>`;

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
