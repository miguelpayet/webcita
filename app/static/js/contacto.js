enviar_contacto = function (codigo) {
    if (jQuery) {
        let jqobj = jQuery('form#form_contacto');
        if (jqobj.length) {
            let form = jqobj.get(0);
            form.submit();
            console.log('envió form');
        } else {
            console.log("no existe form en página");
        }
    } else {
        console.log('no existe jQuery en página');
    }
    return false;
}