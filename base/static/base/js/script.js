
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

