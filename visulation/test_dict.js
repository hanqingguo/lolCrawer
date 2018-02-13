var fs = require("fs");
var parsedJSON = require('./lol_test.json');

var dict={"name":"damage","children":[]};
// dict["children"].push({"name":"ADC","Size":123});
// dict["children"].push({"name":"TOP","Size":200});
//
// fs.writeFile("./object.json",JSON.stringify(dict),(err)=>{
//   if(err){
//     console.console.error(err);
//     return;
//   };
//   console.log("File has been created");
// });
//
// new_file=JSON.stringify(dict);
// dict["hanqing"+" "+"guo"]="nan";
//
// console.log(dict["hanqing"+" "+"guo"]);
// console.log(dict["hello"]["hei"]);
console.log(dict["heiehi"]==undefined);
dict["heihei"]="hello";
console.log(dict);
