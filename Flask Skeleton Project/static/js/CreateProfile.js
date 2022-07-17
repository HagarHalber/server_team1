
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0 so need to add 1 to make it 1!
var yyyy = today.getFullYear();
if(dd<10){
  dd='0'+dd
} 
if(mm<10){
  mm='0'+mm
} 

today = yyyy+'-'+mm+'-'+dd;
document.getElementById("startDates").setAttribute("min", today);

function DateCheck()
{
  var StartDate= document.getElementById('startDates').value;
  var EndDate= document.getElementById('endDates').value;
  var eDate = new Date(EndDate);
  var sDate = new Date(StartDate);
  if(StartDate!= '' && EndDate!= '' && sDate> eDate)
    {
    alert("Please ensure that the End Date is greater than or equal to the Start Date.");
<%session.setAttribute("id","Imsession");%>
    return false;
    }
}
document.getElementById('submit').onclick = function() {
  var selected = [];
  for (var option of document.getElementById('hobbies').options) {
    if (option.selected) {
      selected.push(option.value);
    }
  }
hobbies_String(selected);
}


function hobbies_String(selected){
  var opt = "";
  for (var i=0, iLen=selected.length; i<iLen; i++) {
    if(i == selected.length){
      opt+= selected[i];
    }
    else{
      opt+= selected[i] + " ,";
    }
  }
  const input= document.getElementById('string_hobbies');
  input.innerHTML= opt
}