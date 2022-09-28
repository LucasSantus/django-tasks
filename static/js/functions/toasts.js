// Função para criar toast's
function generate_toast(type, title, message){
    let type_message = type
    if(type == 'error'){
        type_message = "danger"
    }

    $('#assembly').empty();
    
    $(`
        <div class="position-fixed bottom-0 end-0 p-3" style="z-index: 11">
        <div id="liveToast" class="toast hide" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
            <img src="..." class="rounded me-2" alt="...">
            <strong class="me-auto">Bootstrap</strong>
            <small>11 mins ago</small>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            Hello, world! This is a toast message.
        </div>
        </div>
    </div>
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