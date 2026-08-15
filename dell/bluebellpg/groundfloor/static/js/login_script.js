const form=document.getElementById('loginForm');
const loginpage=document.getElementById('loginPage');
const sucessPage=document.getElementById('success');
form.addEventListener('submit',function(event){
    event.preventDefault();
    loginpage.style.display='none';
    sucessPage.style.display='block';
});
function goBack(){
    loginpage.style.display='block';
    sucessPage.style.display='none';
}
