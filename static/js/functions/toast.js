/**
 * function for building the list of container for toasts.
 */
const build_toast_container = () => {
    $(`
        <div id='assembly'>
            <div id='toast_container' class='toast-container position-fixed' style='top: 20px; right: 40px'></div>
        </div>
    `).appendTo('body')
}

/**
 *  function for delete toast with time to 10 seconds after the building toast.
 * @param { string } id 
 */
const delete_toast = ( id ) => { 
    setTimeout( function(){
        $('#' + id).remove()
    }, 10000);
}

/**
 *  function for building the assembly message toast with user.
 * @param { string } type
 * @param { string } title
 * @param { string } message
 */
const toast = ( type = 'dark', title, message ) => {
    const is_valid_type = [ 'primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', ]

    if( !is_valid_type.includes(type) ) throw new Error('type not found!')

    const id = 'toast-' + Math.floor(Math.random() * 100)

    delete_toast( id )

    $(`
        <div id=${ id } class='toast' role='alert' aria-live='assertive' aria-atomic='true'>
            <div class='toast-header text-${ type }'>
                <strong class='me-auto'>
                    ${ title }
                </strong>
                <small class='text-muted'>Agora</small>
            </div>
            <div class='toast-body text-${ type }'>
                ${ message }
            </div>
        </div>
    `).appendTo('#toast_container');

    $('.toast').toast('show')
}
