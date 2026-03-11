
function confirm_delete(tarea_id) {
    Swal.fire({
        title: "¿Seguro que desea eliminar la tarea?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Si, eliminar!",
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if(result.isConfirmed){
            Swal.fire({
                text: "Tarea Eliminada!.",
                icon: "success",
                showConfirmButton: false,
                timer: 1500
            }).then(() => {
                window.location.href = `/eliminar-tarea/${tarea_id}`
            });
        }
    });
}

function confirm_save(event) {
    event.preventDefault();
    Swal.fire({
      position: "center",
      icon: "success",
      title: "Tarea Guadada!",
      showConfirmButton: false,
      timer: 1500
    }).then(()=>{
       //al cerrar la alerta, se envia el formulario
       document.querySelector('form').submit();
    });
}