$(function() 
      {
        $("#form-reg").validate({
            rules: {
                    numIden: "required",
                    foto: "required",
                    nom: "required",
                    phono: "required",
                    dire: "required",
                    mail: {
                        required: true,
                        email: true
                    },
                    pais: "required",
                    pass: "required",
                    mon: "required"  
                    
            }, //rules
            messages: {
                numIden: {
                    required: 'Ingresa número de identificación'
                },
                foto: {
                    required: 'Carga una foto'
                },
                nom: {
                    required: 'Ingresa tu nombre completo'
                },
                phono:{
                    required: 'Ingrese un número de contacto'
                },
                dire: {
                    required: 'Ingresa una dirección'
                },
                mail: {
                    required: 'Ingresa tu correo electrónico',
                    email: 'Formato de correo no válido'
                },
                pais: {
                    required: 'Ingresa un País'
                },
                pass: {
                    required: 'Ingresa una contraseña',
                    minlength: 'Caracteres insuficientes'
                },
                mon: {
                    required: 'Ingresa una moneda'
                }
            }//messages
        }); //$('formulario').validate
    }); //function