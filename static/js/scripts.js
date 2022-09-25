function loadingInit(){
    $("body").append(`
        <div class="body__loading">
            <div class="sk-cube-grid"> <div class="sk-cube-child sk-cube-grid1"></div> <div class="sk-cube-child sk-cube-grid2"></div> <div class="sk-cube-child sk-cube-grid3"></div> <div class="sk-cube-child sk-cube-grid4"></div> <div class="sk-cube-child sk-cube-grid5"></div> <div class="sk-cube-child sk-cube-grid6"></div> <div class="sk-cube-child sk-cube-grid7"></div> <div class="sk-cube-child sk-cube-grid8"></div> <div class="sk-cube-child sk-cube-grid9"></div> </div>
        </div>
    `)
}

function loadingStop(){
    $(".body__loading").remove();
}

$(document).ready(function(){
    $(window).bind('beforeunload', function() {
        console.log("abriu")
        loadingInit();
    });

    $(window).on("load", async function() {
        await new Promise(function(resolve) {
            
            loadingStop();
            resolve();
        });
        console.log("fechou")
    }) 
});