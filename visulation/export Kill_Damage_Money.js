var fs = require("fs");
var jsondata;
var contain;
var damageData={"name":"Damage","children":[{"name":"team100","children":[]},{"name":"team200","children":[]}]};
var killData={"name":"Kills","children":[{"name":"team100","children":[]},{"name":"team200","children":[]}]};
var moneyData={"name":"MoneyEarn","children":[{"name":"team100","children":[]},{"name":"team200","children":[]}]};
var parsedJSON = require('./lol_test.json');


jsondata=parsedJSON;

function loadDamageData(callback){
  var totalDamage=0;
  var totalKill=0;
  var totalMoney=0;
  for(var i=0;i<jsondata.length;i++)
  {
    for(var j=0;j<jsondata[i]["participants"].length;j++)
    {
      totalDamage+=jsondata[i]["participants"][j]["stats"]["totalDamageDealtToChampions"];
      totalKill+=jsondata[i]["participants"][j]["stats"]["kills"];
      totalMoney+=jsondata[i]["participants"][j]["stats"]["goldEarned"];
    }
  }
  totalDamage=totalDamage/10000;
  totalKill=totalKill/10000;
  totalMoney=totalMoney/10000;
  for(var i=0;i<jsondata.length;i++)
  {
    console.log(jsondata.length);
    for(var j=0;j<jsondata[i]["participants"].length;j++){
      if(jsondata[i]["participants"][j]["teamId"]==100)
      {
        contain=0;
        var role=jsondata[i]["participants"][j]["timeline"]["role"];
        var lane=jsondata[i]["participants"][j]["timeline"]["lane"];
        for(var k=0;k<damageData["children"][0]["children"].length;k++)
        {

          if(role+" "+lane==damageData["children"][0]["children"][k]["name"])
          {
            damageData["children"][0]["children"][k]["children"][0]["size"]+=jsondata[i]["participants"][j]["stats"]["totalDamageDealtToChampions"]/totalDamage;
            damageData["children"][0]["children"][k]["children"][1]["size"]+=jsondata[i]["participants"][j]["stats"]["kills"]/totalKill;
            damageData["children"][0]["children"][k]["children"][2]["size"]+=jsondata[i]["participants"][j]["stats"]["goldEarned"]/totalMoney;
            contain=1;
          }
        }
        if(contain==0)
        {
            damageData["children"][0]["children"].push({"name":role+" "+lane,"children":[{"name":"DamageContribute","size":jsondata[i]["participants"][j]["stats"]["totalDamageDealtToChampions"]/totalDamage
          },{"name":"KillContribute","size":jsondata[i]["participants"][j]["stats"]["kills"]/totalKill},{"name":"MoneyContribute","size":jsondata[i]["participants"][j]["stats"]["goldEarned"]/totalMoney}]})
        }
      }
      else {
        contain=0;
        var role=jsondata[i]["participants"][j]["timeline"]["role"];
        var lane=jsondata[i]["participants"][j]["timeline"]["lane"];
        for(var k=0;k<damageData["children"][1]["children"].length;k++)
        {

          if(role+" "+lane==damageData["children"][1]["children"][k]["name"])
          {
            damageData["children"][1]["children"][k]["children"][0]["size"]+=jsondata[i]["participants"][j]["stats"]["totalDamageDealtToChampions"]/totalDamage;
            damageData["children"][1]["children"][k]["children"][1]["size"]+=jsondata[i]["participants"][j]["stats"]["kills"]/totalKill;
            damageData["children"][1]["children"][k]["children"][2]["size"]+=jsondata[i]["participants"][j]["stats"]["goldEarned"]/totalMoney;
            contain=1;
          }

        }
        if(contain==0)
        {
          damageData["children"][1]["children"].push({"name":role+" "+lane,"children":[{"name":"DamageContribute","size":jsondata[i]["participants"][j]["stats"]["totalDamageDealtToChampions"]/totalDamage
        },{"name":"KillContribute","size":jsondata[i]["participants"][j]["stats"]["kills"]/totalKill},{"name":"MoneyContribute","size":jsondata[i]["participants"][j]["stats"]["goldEarned"]/totalMoney}]})
        }
      }
      }
    }

  callback(damageData);
}
function printData(Ddata){
  console.log(Ddata);
}

//loadKill
function loadKillData(callback){
  for(var i=0;i<jsondata.length;i++)
  {
    for(var j=0;j<jsondata[i]["participants"].length;j++){
      if(jsondata[i]["participants"][j]["teamId"]==100)
      {
        contain=0;
        var role=jsondata[i]["participants"][j]["timeline"]["role"];
        var lane=jsondata[i]["participants"][j]["timeline"]["lane"];
        for(var k=0;k<killData["children"][0]["children"].length;k++)
        {

          if(role+" "+lane==killData["children"][0]["children"][k]["name"])
          {
            killData["children"][0]["children"][k]["size"]+=jsondata[i]["participants"][j]["stats"]["kills"];
            contain=1;
          }
        }
        if(contain==0)
        {
            killData["children"][0]["children"].push({"name":role+" "+lane,"size":jsondata[i]["participants"][j]["stats"]["kills"]})
        }
      }
      else {
        contain=0;
        var role=jsondata[i]["participants"][j]["timeline"]["role"];
        var lane=jsondata[i]["participants"][j]["timeline"]["lane"];


        for(var k=0;k<killData["children"][1]["children"].length;k++)
        {

          if(role+" "+lane==killData["children"][1]["children"][k]["name"])
          {
            killData["children"][1]["children"][k]["size"]+=jsondata[i]["participants"][j]["stats"]["kills"];
            contain=1;
          }

        }
        if(contain==0)
        {
            killData["children"][1]["children"].push({"name":role+" "+lane,"size":jsondata[i]["participants"][j]["stats"]["kills"]})
        }
      }
      }
    }

  callback(killData);
}

//loadMoneyData
function loadMoneyData(callback){

  for(var i=0;i<jsondata.length;i++)
  {
    for(var j=0;j<jsondata[i]["participants"].length;j++){
      if(jsondata[i]["participants"][j]["teamId"]==100)
      {
        contain=0;
        var role=jsondata[i]["participants"][j]["timeline"]["role"];
        var lane=jsondata[i]["participants"][j]["timeline"]["lane"];
        for(var k=0;k<moneyData["children"][0]["children"].length;k++)
        {

          if(role+" "+lane==moneyData["children"][0]["children"][k]["name"])
          {
            moneyData["children"][0]["children"][k]["size"]+=jsondata[i]["participants"][j]["stats"]["goldEarned"];
            contain=1;
          }
        }
        if(contain==0)
        {
            moneyData["children"][0]["children"].push({"name":role+" "+lane,"size":jsondata[i]["participants"][j]["stats"]["goldEarned"]})
        }
      }
      else {
        contain=0;
        var role=jsondata[i]["participants"][j]["timeline"]["role"];
        var lane=jsondata[i]["participants"][j]["timeline"]["lane"];


        for(var k=0;k<moneyData["children"][1]["children"].length;k++)
        {

          if(role+" "+lane==moneyData["children"][1]["children"][k]["name"])
          {
            moneyData["children"][1]["children"][k]["size"]+=jsondata[i]["participants"][j]["stats"]["goldEarned"];
            contain=1;
          }

        }
        if(contain==0)
        {
            moneyData["children"][1]["children"].push({"name":role+" "+lane,"size":jsondata[i]["participants"][j]["stats"]["goldEarned"]})
        }
      }
      }
    }

  callback(moneyData);
}



loadDamageData(printData);
loadKillData(printData);
loadMoneyData(printData);

fs.writeFile("./damage1111.json",JSON.stringify(damageData),(err)=>{
  if(err){
    console.console.error(err);
    return;
  };
  console.log("File has been created");
});
