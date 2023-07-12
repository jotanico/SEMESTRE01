//NUMBERS (EN JS SOLO EXISTE EL TIPO DE DATO NUMBERS PARA LOS NUMEROS EN GENERAL)

let edad = 29;
let sueldo = 12000000;
const PI = 3.14;

//Con notacion Cientifica
const n_grande = 1e6 //ESTO ES == 1MILLON
const n_pequeño = 1e-6//ESTOO ES == 0.0000001

//como podemos ver, uno aumenta haciendo el numero mas grande, y otro lo hace mas pequeño

console.log(n_grande);
console.log(n_pequeño);

//Big Int
const BigInt = 213123131313131413412n;
console.log(BigInt);

//Infinity
console.log(edad / 2);

//¿ES POSIBLE ESTO?

console.log("6" / 2); //SI, solo en JS

//NaN (error de calculo)

alert("Hola" * 2); //TAl DIVISION ES ERRONEA

//STRINGS
console.log("######### STRINGSSS ############");
let string1 = "Hola, Buen dia!"
let string2 = "Adios, Buenas noches!"
let frase = "Este es un saludo : " + string1
console.log(frase);

//BOOLEANOS (T- RUE OR F- ALSE)

//Asignando variables
console.log("############# BOOLEANOSS #################");

let V = true
let F = false

//Ciclo :

if (V) {
    //Se ejecuta si el valor es True
    console.log("El resultado es Verdadeero");
}   else {
    //Se ejecuta si el valor es false
    console.log("El resultado es falso");
}

//NULL

console.log("########### NULL ############");

let numeroNuevo = null
console.log(numeroNuevo);

//UNDEFINED
console.log("########### UNDEFINED ###########");
let instituciuon;
console.log(instituciuon) //arroja un valor indefinido, porque no tiene valor

//OBJECT  Y SYMBOL (AMBOS COLECCIONAN DATOS DENTRO)
 
console.log("############ Objetos ##############");
//hay 2 formas de crear un objeto

let user = new Object(); //sintaxis de "constructor de objetos"
let user1 = {}; //sintaxis de "Objeto literal"

//Objeto literal

let usuario = {
    name: "Mateo",   //En la clave name, se akmacena "Mateo"
    age: 26,         //En la clave age, se almacena 26
    city: "Osorno",  //En la clave city, se almacena "Osorno"
    "correo electronico": "holamellamomateo@gmail.com" //Usando comillas en la variable podemos usar espacios sin problemas

};

console.log(usuario);

//Agregando algo nuevo al objeto literal (usuario)

usuario.Verdadero = true; //solo llamamos la variable + punto, y denominamos otra variable

//Accediendo a una propiedad de mas de 2 palabras dentro de console.log

console.log(usuario["correo electronico"]);

//ELiminando una propiedad del objeto (usuario)

delete usuario.Verdadero;

console.log("################### SABER TIPO DE DATO ######################");
console.log(typeof edad);
console.log(typeof string1);

console.log("################# TRANSFORMANDO DE STRING A NUMBER ####################");
console.log(typeof edad);
edad = String(edad);
console.log(typeof edad); 

console.log("################# TRANSFORMANDO DE NUMBER A STRING ####################");
let stock = "1000"

console.log(typeof stock);
stock = Number(stock);
console.log(typeof stock);