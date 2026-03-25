document.addEventListener('DOMContentLoaded', () => {
    MicroModal.init();
});

/* const tabs = document.querySelectorAll('.tabs a');
const tab_contents = document.querySelectorAll('.tab-content');
const buscador = document.querySelector('input[name="buscador"]');

tabs.forEach(tab =>{
    tab.addEventListener('click', (e) => {
        e.preventDefault();
        const target = tab.dataset.target;

        // quitar active
        tabs.forEach(t => t.classList.remove('active'));
        tab_contents.forEach(tc => tc.classList.remove('active'));

        // agregar active
        tab.classList.add('active');
        document.querySelector(target).classList.add('active');

        // limpiar el buscador al cambiar de tab
        buscador.value = '';
        document.querySelectorAll(`${target} .tarea-item`).forEach(t => t.style.display = '');
    });
});
 */


document.getElementById('btn-agregar').addEventListener('click', (e) => {
    e.preventDefault();
    const form = document.getElementById('form-crear-tarea');
    if (form) {
        // limpiar manualmente los campos
        form.querySelector('#id_titulo').value = '';
        form.querySelector('#id_descripcion').value = '';
        form.querySelector('#id_completo').checked = false;

        // forzar que el action sea crear
        form.action = form.dataset.crearUrl;
    }
    MicroModal.show('modal-1');
});

document.querySelectorAll('.form-tarea').forEach(form => {
    form.addEventListener('change', function (e) {
        e.preventDefault();

        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                "X-CSRFToken": formData.get('csrfmiddlewaretoken')
            }
        }).then(res => res.json()).then(data => {
            if (data.success) {
                const label = form.querySelector('.titulo-tarea');
                if (data.completo) {
                    label.classList.add('tarea-completada');
                } else {
                    label.classList.remove('tarea-completada');
                }
            } else {
                alert("Error al actualizar tarea");
            }
        });
    });
});

document.querySelectorAll('.icon-edit').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        const url = btn.getAttribute('href');

        fetch(url)
            .then(res => res.text())
            .then(html => {
                document.querySelector('#modal-1-content').innerHTML = html
            });
    });
});

document.querySelectorAll(".acordeon").forEach(acordeon =>{
    acordeon.addEventListener("click", () => {
        const tareaId = acordeon.dataset.id;
        const content = document.querySelector(`.acordeon-content[data-id="${tareaId}"]`);

        acordeon.classList.toggle('active');

        if (content.classList.contains('open')) {
            content.style.maxHeight = null;
            content.classList.remove('open');
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
            content.classList.add('open');
        }
    });
});