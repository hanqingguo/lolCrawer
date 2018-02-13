var fs = require("fs");
var jsondata;
var contain;
var ChampionData={};
var parsedJSON = require('./lol_test.json');


jsondata=parsedJSON;

function loadChampionData(callback){
  for(var i=0;i<jsondata.length;i++)
  {
    for(var j=0;j<jsondata[i]["participants"].length;j++)
      {
         var ChampionID = jsondata[i]["participants"][j]["championId"];
         var game_result = jsondata[i]["participants"][j]["stats"]["win"];
         //console.log(jsondata[i]["participants"][j]["championId"]);
         //console.log(jsondata[i]["participants"][j]["stats"]["win"])
         if(ChampionData[ChampionID]==undefined)
         {
           ChampionData[ChampionID]={"appear":0,"win_count":0,"win_rate":0};
         }
         ChampionData[ChampionID]["appear"]+=1;
         if(game_result==true)
         {
           ChampionData[ChampionID]["win_count"]+=1;
           ChampionData[ChampionID]["win_rate"]=ChampionData[ChampionID]["win_count"]/ChampionData[ChampionID]["appear"];
         }
      }
  }

  callback(ChampionData);
}
function printData(Ddata){
  console.log(Ddata);
}

loadChampionData(printData);

fs.writeFile("./champions.json",JSON.stringify(ChampionData),(err)=>{
  if(err){
    console.console.error(err);
    return;
  };
  console.log("File has been created");
});
