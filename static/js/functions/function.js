// Função para criar toast's
function generate_toast(type, title, message){
    let type_message = type
    if(type == 'error'){
        type_message = "danger"
    }

    $('#assembly').empty();
    
    $(`
        <div class="toast fade show">
            <div role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-header text-${type_message}">
                    <strong class="me-auto">
                        ${title}
                    </strong>
                    <small class="text-muted">Agora</small>
                </div>
                <div class="toast-body text-${type_message}">
                    ${message}
                </div>
            </div>
        </div>
    `).appendTo("#assembly");

    $(".toast").toast("show")
}