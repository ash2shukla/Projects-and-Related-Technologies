function useArgs(var1, var2, var3) {
  var a = arguments.length;       // array containing all the arguments
  var result = "";
  for (var i = 0; i < a; i++) {
    result += " " + arguments[i];
  }
  return result;
}
var b = useArgs("Déjà", "vu");    // b => " Déjà vu", var3 = undefined
console.log(b);
