function build__todos(items, id_class){
    $("#" + id_class).empty();

    for( let item of items ){
        $(`
            <div class="bg-danger w-100">
                ${item.title}
            </div>
        `).appendTo("#" + id_class);
    }
}