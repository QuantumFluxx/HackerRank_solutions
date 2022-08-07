JS:

var resultScreen=document.getElementById("res");
var result=0;
var operatorsSeq="";
function clickZero()
{
    
    resultScreen.innerHTML+="0";
}
function clickOne()
{
    
    resultScreen.innerHTML+="1";
}
function clickSum()
{
    operatorSeq="+";
    result=parseInt(resultScreen.innerHTML,2);
    resultScreen.innerHTML+="+";
}
function clickSub()
{
     operatorSeq="-";
    resultScreen.innerHTML+="-";
}
function clickMul()
{
    operatorSeq="*";
     result=parseInt(resultScreen.innerHTML,2);
    resultScreen.innerHTML+="*";
}
function clickDiv()
{
     operatorSeq="/";
    resultScreen.innerHTML+="/";
}
function clickEql()
{
    var ans=0;
   
  if(operatorSeq=='+')
      {
           var i =(resultScreen.innerHTML).indexOf("+");
   
         var operand2=parseInt((resultScreen.innerHTML).substr(i+1),2);
          ans =result+operand2;
      }
    else if(operatorSeq=='-')
    
    {
          var i =(resultScreen.innerHTML).indexOf("-");
         var operand2=parseInt((resultScreen.innerHTML).substr(i+1),2);
        ans =result-operand2;
    }
     
      else if(operatorSeq=='*')
    
    {
           var i =(resultScreen.innerHTML).indexOf("*");
         var operand2=parseInt((resultScreen.innerHTML).substr(i+1),2);
        ans =result*operand2;
    }
      else if(operatorSeq=='/')
    
    {
           var i =(resultScreen.innerHTML).indexOf("/");
         var operand2=parseInt((resultScreen.innerHTML).substr(i+1),2);
        ans =result/operand2;
    }
    
   
    resultScreen.innerHTML=ans.toString(2);
}
function clickClear()
{
    resultScreen.innerHTML="";
    
}

CSS:

body{
    width:33%;
}
#res{
    background-color:lightgray;
    border:solid;
    height:48px;
    font-size:20px;
}
#btn0,#btn1{
    background-color:lightgreen; 
    color:brown;
}

#btnClr,#btnEql{
       background-color:darkgreen; 
    color:white;
}
#btnSum,#btnSub,#btnMul,#btnDiv{
     background-color:black; 
    color:red;
}
button{
    
    width:25%;
    height:36px;
    font-size:18px;
    margin:0px;
    float:left;
    
}

HTML:

<!-- Enter your HTML code here -->
<!DOCTYPE html>
<html>
    <head>
          <link rel="stylesheet" href="css/binaryCalculator.css" type="text/css">
        <meta charset="utf-8">
        <title>Binary Calculator</title>
    </head>
    <body>
        
        <div id="res"></div>
        <div id="btns">
            <button id="btn0" onclick="clickZero()">0</button>
            <button id="btn1" onclick="clickOne()">1</button>
            <button id="btnClr" onclick="clickClear()">C</button>
            <button id="btnEql" onclick="clickEql()">=</button>
            <button id="btnSum" onclick="clickSum()">+</button>
            <button id="btnSub" onclick="clickSub()">-</button>
            <button id="btnMul" onclick="clickMul()">*</button>
            <button id="btnDiv" onclick="clickDiv()">/</button>
        
        </div>
        
        <script src="js/binaryCalculator.js" type="text/javascript"></script>
    </body>
</html>