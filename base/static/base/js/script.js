
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

const tabs = document.querySelectorAll('.tabs a');
const tab_contents = document.querySelectorAll('.tab-content');

tabs.forEach(tab => {
   tab.onclick = (e) => {
       e.preventDefault();
       const target = tab.getAttribute('href');

       //quitar active
       tabs.forEach(t => t.classList.remove('active'));
       tab_contents.forEach(tc => tc.classList.remove('active'));

       //agregar active
       tab.classList.add('active');
       document.querySelector(target).classList.add('active');
   }
});

