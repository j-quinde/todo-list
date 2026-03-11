
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


document.querySelectorAll('.form-tarea').forEach(form => {
    form.addEventListener('change', function(e) {
        e.preventDefault();

        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                "X-CSRFToken": formData.get('csrfmiddlewaretoken')
            }
        }).then(res => res.json()).then(data => {
            if(data.success){
                const label = form.querySelector('.titulo-tarea');
                if (data.completo){
                    label.classList.add('tarea-completada');
                }else{
                    label.classList.remove('tarea-completada');
                }
            }else{
                alert("Error al actualizar tarea");
            }
        });
    });
});
