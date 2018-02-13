


function f1(callback){
  console.log('Running f1');
  setTimeout(callback,2000);
};

var a = function f2(){
  console.log("Running f2");
  return 2;
};

function f3(){
  console.log('Running f3');
};



// f1(f2);
f3();
// a;
console.log(typeof(a));
console.log(a());
