const build_html = ( item ) => {
    return `
        <div class="bg-danger w-100">
            ${item.title}
        </div>
    `
}

const build_todo = ( values, id_class ) => $( build_html(values) ).appendTo("#" + id_class);

function get_all_todos(values, id_class){
    if( values.length > 1 ) {
        for( let item of values ){
            build_todo(item, id_class);
        }
    } else {
        build_todo(values, id_class);
    }
}