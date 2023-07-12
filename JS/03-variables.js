//VARIABLES QUE PUEDEN CAMBIAR CON EL TIEMPO ("VAR" AND "LET")

var estatura = 1.71;
let peso = 60;

//VARIABLE QUE NO PUEDE CAMBIAR CON EL TIEMPO (CONSTANTE)

const nombre = "Jorge";

//OTROS EJEMPLOS
//declarando variables

var edad ;
let ciudad;

//inicializando variables

edad = 18
ciudad = "Rio bueno";

//Declarando e inicializando en un mismo extracto de codigo

const apellido = "Abarzua";

//Concatenando variables de tipo String

const nombre_completo = nombre + "" +  apellido;
console.log("Hola mi nombre es", nombre_completo);

//declarando e inicializando variables en una linea

let docente= "Tomas", age= 25, asignaturas= ["IA", "Seguridad Cibernetica"];
console.log("Nombre del docente :", docente); console.log("Años del docente : ", age); console.log("Asignaturas que hace el docente : ", asignaturas);

//Entendiendo el concepto de Hosting (Solo con VAR, ya que LET no tiene hosting)

console.log(n);
var n=10
//podemos imprimir la variable pero saldra que no tiene definido nada
//Este codigo deberia emplearse

var n = 10;
console.log("valor de n :", n);
