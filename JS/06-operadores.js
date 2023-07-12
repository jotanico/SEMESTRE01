console.log("############### OPERADOR DE SUMA/CONCATENACION #####################");
//OPERADOR DE SUMA
//SUMA binaria 
let tomates = 30
let naranjas = 20
console.log("La suma entre tomates y naranjas es : ", tomates + naranjas);


//SUMA unaria
let caja = "2"
let estantes = "5"
console.log(caja);
console.log(+caja);

console.log("La suma entre cajas y estantes es : ", caja + estantes);

suma1 = "La suma entre cajas y estantes es :", +caja + +estantes;
console.log(suma1)

//OPERADOR RESTA
console.log("############### OPERADOR DE RESTA #######################");
console.log("La resta entre tomates y naranjas es :", tomates - naranjas);

//OPERADOR DE MULTIPLICACION
console.log("################### OPERADOR DE PRODUCTO ###################");
console.log("La multiplicacion entre tomates y naranjas es :", tomates * naranjas);

//OPERADOR DE DIVISION
console.log("################### OPERADOR DE DIVISION ###################");
console.log("La DIVISION entre tomates y naranjas es :", tomates / naranjas);

//RESTO DE UNA DIVISION (%)
console.log("################### OPERADOR DE RESTO ###################");
console.log(6 % 2); //0 ES EL RESTO DE 6 DIVIDIDO EN 2
console.log(8 % 3); // 2 ES EL RESTO DE 8 DIVIDIDO EN 3

//OPERADOR DE POTENCIA (**)
console.log("################### OPERADOR DE EXPONENCIACION ###################");
console.log(2**2); //2² = 4
console.log(2 ** 3); // 2³ = 8

//ASIGNACION ENCADENADAS
console.log("################### ASIGNACIONES ENCADENADAS ###################");

let a,b,c;
a = b = c = 5 + 5;
console.log(a); //10
console.log(b); //10
console.log(c); //10

//MODIFICACION EN EL LUGAR
console.log("################### MODIFICACION/ASIGNACION VARIABLES (OPERADOR) ###################");
let n = 1
n = n + 9; //al n ya establecido le sumamos 9

console.log(n);

n += 5; //ahora n = 15
console.log("Valor actualizado :", n);
n*= 2; //ahora n = 30 (15*2)
console.log("Valor actualizado n: ", n);

//INCREMENTO / DECREMENTO
console.log("################### INCREMENTO ###################");
let contador = 5;
contador ++;
console.log(contador);

console.log("################### DECREMENTO ###################");
contador--;
console.log(contador);