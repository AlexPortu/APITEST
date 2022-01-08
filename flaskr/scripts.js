const date = new Date();


const months = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
];

document.querySelector(".date h1").innerHTML = months[date.getMonth()];


fetch("try_json_1D.json")
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        const myjson = JSON.stringify(data);
        localStorage.setItem('fs1', myjson);
        let text = localStorage.getItem('fs1');
        let obj = JSON.parse(text);
        document.getElementById('CONCEPTO').innerHTML = obj[Object.keys(obj)[0]]['CONCEPTO']
    });
;
