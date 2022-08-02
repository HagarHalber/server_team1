
const editButton = document.getElementById('edit');
const saveButton = document.getElementById('save');

//dates validation
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
const FullName = document.getElementById("Full-Name");
const Email = document.getElementById("Email");
const PhoneNumber = document.getElementById("Phone-Number");
const Destnation = document.getElementById("Destnation");
const From = document.getElementById("From");
const To = document.getElementById("To");
const Hobbies = document.getElementById("Hobbies");
const Trip_Vibe = document.getElementById("Vibe");
const Languages = document.getElementById("Languages");
const about = document.getElementById("About");
const todayDate = Date.parse(today);


editButton.addEventListener('click', () => {
	    FullName.contentEditable = true;
    Email.contentEditable = true;
    PhoneNumber.contentEditable = true;
    Destnation.contentEditable = true;
    From.contentEditable = true;
    To.contentEditable = true;
    Hobbies.contentEditable = true;
    Trip_Vibe.contentEditable = true;
    Languages.contentEditable = true;
    about.contentEditable = true;

    FullName.style.backgroundColor = "#edf3f3b3";
    Email.style.backgroundColor = "#edf3f3b3";
    PhoneNumber.style.backgroundColor = "#edf3f3b3";
    Destnation.style.backgroundColor = "#edf3f3b3";
    From.style.backgroundColor = "#edf3f3b3";
    To.style.backgroundColor = "#edf3f3b3";
    Hobbies.style.backgroundColor = "#edf3f3b3";
    Trip_Vibe.style.backgroundColor = "#edf3f3b3";
    Languages.style.backgroundColor = "#edf3f3b3";
    about.style.backgroundColor = "#edf3f3b3";
});

//alerts when user doesn't fill in all fields
saveButton.addEventListener('click', () => {
  var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    var re = /^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$/;
    var isValidDateTo = Date.parse(To.textContent);
    var isValidDateFrom = Date.parse(From.textContent);

    if(FullName.textContent == '' || /^[a-zA-Z]+$/.test(FullName)){
        alert("Full name is required");
    }
    else if (!Email.textContent.match(pattern)) {
        alert("Enter a valid Email");
    }
    else if(!PhoneNumber.textContent.match(re)){
        alert("Phone Number must be digits only");
    }
    else if(Destnation.textContent == '' || /^[a-zA-Z]+$/.test(Destnation)){
        alert("Destnation a text is required");
    }
    else if(isNaN(isValidDateFrom) || isValidDateFrom < todayDate){
        alert("From must be a date dd/mm/yy after today date"+" "+ today);
    }
    else if(isNaN(isValidDateTo) || isValidDateTo<isValidDateFrom){
        alert("To must be a date dd/mm/yy after From date"+" "+ From.textContent);
    }
    else if((/\d/.test(Trip_Vibe.textContent)) || (/\d/.test(Hobbies.textContent)) || (/\d/.test(Languages.textContent))){
        alert("Hobbies, Trip_Vibe, Languages, About Me must be a text only filed");
    }
    else{
        FullName.contentEditable = false;
        Email.contentEditable = false;
        PhoneNumber.contentEditable = false;
        Destnation.contentEditable = false;
        From.contentEditable = false;
        To.contentEditable = false;
        Hobbies.contentEditable = false;
        Trip_Vibe.contentEditable = false;
        Languages.contentEditable = false;
        about.contentEditable = false;
        FullName.style.backgroundColor = "#cdf2f3b3";
        Email.style.backgroundColor = "#cdf2f3b3";
        PhoneNumber.style.backgroundColor = "#cdf2f3b3";
        Destnation.style.backgroundColor = "#cdf2f3b3";
        From.style.backgroundColor = "#cdf2f3b3";
        To.style.backgroundColor = "#cdf2f3b3";
        Hobbies.style.backgroundColor = "#cdf2f3b3";
        Trip_Vibe.style.backgroundColor = "#cdf2f3b3";
        Languages.style.backgroundColor = "#cdf2f3b3";
        about.style.backgroundColor = "#cdf2f3b3";
    }
});


