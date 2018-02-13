var width = 300;  //画布的宽度
var height = 300;   //画布的高度


var svg = d3.select("body")     //选择文档中的body元素
    .append("svg")          //添加一个svg元素
    .attr("width", width)       //设定宽度
    .attr("height", height);    //设定高度

    var dataset = [ 2.5 , 2.1 , 1.7 , 1.3 , 0.9 ];
    //定义比例尺
    var linear = d3.scale.linear()
          .domain([0, d3.max(dataset)])
          .range([0, 250]);

    var axis = d3.svg.axis()
         .scale(linear)      //指定比例尺
         .orient("bottom")   //指定刻度的方向
         .ticks(7);          //指定刻度的数量


var rectHeight = 25;   //每个矩形所占的像素高度(包括空白)

svg.selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect")
    .attr("x",20)
    .attr("y",function(d,i){
         return i * rectHeight;
    })
    .attr("width",function(d){
         return linear(d);
    })
    .attr("height",rectHeight-2)
    .attr("fill","steelblue");

svg.append("g")
    .attr("class","axis")
    .attr("transform","translate(20,130)")
    .call(axis);
