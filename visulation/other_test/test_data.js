var jsondata;

function printData(){
  console.log(jsondata[0]["participantIdentities"]);
}

d3.json("lol_test.json",function(error,data){
  jsondata=data;
  printData();
});
