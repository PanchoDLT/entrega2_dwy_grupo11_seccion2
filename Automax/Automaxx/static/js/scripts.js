function validarRut() {
    var rut=document.getElementById("txtRut").value;
    alert("El Rut:" + rut)
    if(rut.length != 10){
           alert("Largo de rut incorrecto, debe tener 10 caracteres."); 
           return false;
    }
    var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var car= rut.slice(index,index+1);
        suma= suma + (num * car);
        num = num - 1 ;
        if(num == 1){
            num=7;
        }

        
    }
    var resto= suma % 11;
    var dv= 11 - resto;
    if(dv>9){
        if(dv==10){
            dv="K"

        }
        else{
            dv=0;
        }
    } 
    var dv_usuario= rut.slice(-1).toUpperCase();
    if(dv!=dv_usuario){
        alert("rut incorrecto");
        return false;
    }
    else{
        alert("rut correcto")
        return true;
    }
}

function validarContrasena(){
    var contrasena=document.getElementById("txtContrasena").value;
    var repetirContrasena=document.getElementById("txtRepetirContrasena").value;

    if(contrasena==repetirContrasena){
        
        alert("contraseña validada");
        return true;

    }

    else{
        
        alert("las contraseñas no conciden")
        return false;
    }
}
function validarFecha() {
    var fechaControl=document.getElementById("fecha").value;
    var fechaSistema = new Date();
    if (fechaControl>fechaSistema){
        alert("fecha de nacimiento incorrecta");
        return false;
    }
    else{
        alert("fecha de nacimiento correcta");
        return true;

    }
}

function validarTodo(){
    var respContra = validarContrasena();
    var respRut= validarRut();
    var respFecha=validarFecha();
if(respRut == false){
    return false;

}

if(respContra == false){
    return false;


}
if(respFecha == false){
    return false;
}
    
}