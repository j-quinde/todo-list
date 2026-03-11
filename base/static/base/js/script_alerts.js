
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
                icon: "success"
            });
            window.location.href = `/eliminar-tarea/${tarea_id}`
        }
    });
}