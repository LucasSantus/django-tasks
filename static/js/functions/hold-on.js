const hold_start = ( text = 'Por favor, Aguarde...' ) => {
    var options = {
        theme: "sk-falding-circle",
        message: text,
        backgroundColor: "bg-dark",
        textColor: "white"
    };
    HoldOn.open(options);
}

const hold_close = ( ) => HoldOn.close();
