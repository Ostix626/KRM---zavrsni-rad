var newone=[];
var newtwo=[];
var newthree=[];
var newfour=[];


function clear(){
    document.getElementById('one').value = '';
    document.getElementById('two').value = '';
    document.getElementById('three').value = '1';
    document.getElementById('four').value = '';
    document.getElementById("one").focus();
}


function empty(one, two, three, four) 
{
    var a = one.length;
    var b = two.length;
    var c = parseFloat(three);
    var d = parseFloat(four);
    var e = three.length;
    var f = four.length;

    if (a*b*e*f == 0 || c <= 0 || d <= 0) {  	
        alert("Niste sve ispunili");
        return false; 
    }  	
    return true;
}

function duplicate(one){
    for(let k = 0; k < newone.length; k++) {
        if(one.localeCompare(newone[k]) == 0) {
            alert("Materijal je već unesen u račun");
            return false;
        }
    }
    return true;
}

function add(){
    var one=document.getElementById('one').value;
    var two=document.getElementById('two').value;
    var three=document.getElementById('three').value;
    var four=document.getElementById('four').value;
    if(empty(one, two, three, four)){
        if(duplicate(one)){
            clear();
            newone.push(one);
            newtwo.push(two);
            newthree.push(three);
            newfour.push(four);
            listshow();
        }
    }
}

function listshow(){
    var list="";
    var ukupno=0;

    if(newone.length) document.getElementById('submit').disabled=false;
    else document.getElementById('submit').disabled=true;

    for(var i=0; i<newone.length; i++){
        var five = 0;
        five = newthree[i] * newfour[i];
        five = parseFloat(five);
        five = five.toFixed(2);

        ukupno = Number(ukupno) + Number(five);
        ukupno = ukupno.toFixed(2);

        list+= 
        "<tr><td>"+(i+1)+"</td>"
        +"<td><input name='sif"+i+"' value='" +newone[i]+ "'class='ro' readonly/></td>"
        +"<td><input name='naz"+i+"' value='" +newtwo[i]+ "'class='ro' readonly/></td>"
        +"<td><input name='kol"+i+"' value='" +newthree[i]+ "'class='ro' readonly/></td>"
        +"<td><input name='cij"+i+"' value='" +newfour[i]+ "'class='ro' readonly/></td>"
        +"<td>" +five+ "</td>"
        +"<td style='width:64px'>"
        +"<button type='button' class='btn material-icons btn-outline' style='padding:0' onclick='edt("+i
        +")'></button><button type='button' class='btn material-icons btn-outline' style='padding:0' onclick='del("+i+")'> </button>"
        +"</td></tr>"

    }
    document.getElementById('data').innerHTML=list;
    document.getElementById("ukupno").innerHTML = ukupno;
    document.getElementById("stavke").value = newone.length;
}

var load=""
function edt(edit){
    document.getElementById('dodaj').disabled=true;
    document.getElementById('izmijeni').disabled=false;
    load=edit;
    document.getElementById('one').value=newone[edit];
    document.getElementById('two').value=newtwo[edit];
    document.getElementById('three').value=newthree[edit];
    document.getElementById('four').value=newfour[edit];
}

function update(){
    var one=document.getElementById('one').value;
    var two=document.getElementById('two').value;
    var three=document.getElementById('three').value;
    var four=document.getElementById('four').value;
    if(empty(one, two, three, four)){
        document.getElementById('dodaj').disabled=false;
        document.getElementById('izmijeni').disabled=true;
        newone[load]=one;
        newtwo[load]=two;
        newthree[load]=three;
        newfour[load]=four;
        clear();
        listshow();
    }
}

function del(dok){
    if(document.getElementById('izmijeni').disabled==true) {
        newone.splice(dok,1);
        newtwo.splice(dok,1);
        newthree.splice(dok,1);
        newfour.splice(dok,1);
        listshow();
    }
}

$( document ).ready(function() {

    $('#viewfile').click(function () {
        var rdr = new FileReader();
        rdr.onload = function (e) {

          var therows = e.target.result.split("\n");

          for (var row = 1; row < therows.length; row++) {
                var columns = therows[row].split("@");
                newone.push(columns[0]);
                newtwo.push(columns[1]);
                newthree.push(columns[2]);
                newfour.push(parseFloat(columns[3]).toFixed(2));
          }
          listshow();
        }
        rdr.readAsText($("#inputfile")[0].files[0]);
    });
});


document.getElementById('submit').addEventListener('keypress', function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
    }
});

document.getElementById('inputDobavljac').addEventListener('keypress', function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
    }
});

document.getElementById('inputRacun').addEventListener('keypress', function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
    }
});

document.getElementById('inputDatum').addEventListener('keypress', function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
    }
});

document.getElementById('one').addEventListener('keypress', function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
    }
});

document.getElementById('two').addEventListener('keypress', function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
    }
});

document.getElementById('three').addEventListener('keypress', function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
    }
});

document.getElementById('four').addEventListener('keypress', function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
    }
});