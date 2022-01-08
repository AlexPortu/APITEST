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
var fs = {
    "2022-04-01": {
        "CUPO": 180,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-02": {
        "CUPO": 485,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-03": {
        "CUPO": 500,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-04": {
        "CUPO": 500,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-05": {
        "CUPO": 0,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 77.6,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-06": {
        "CUPO": 0,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 77.6,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-07": {
        "CUPO": 0,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 77.6,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-08": {
        "CUPO": 500,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-09": {
        "CUPO": 500,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-10": {
        "CUPO": 500,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-11": {
        "CUPO": 500,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-12": {
        "CUPO": 500,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-13": {
        "CUPO": 500,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    },
    "2022-04-14": {
        "CUPO": 500,
        "CONCEPTO": "2 DIAS ADULTO",
        "PRECIO": 73.81312,
        "PRECIO INICIAL": 77.6,
        "COD PRODUCTO": "2OA"
    }
}
"use strict";

fetch("./try_json_2D.json")
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        console.log(data);
    });
document.getElementById("12345").innerHTML = alert(data["2022-04-01"]["CONCEPTO"]);
