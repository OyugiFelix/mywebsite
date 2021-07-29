function loadForm(){
    let enquiry = document.querySelector('.comment-form');
    let body = document.querySelector('.content');
    body.style.opacity = ".3";
    enquiry.style.zIndex = "1";
    enquiry.style.opacity = "1";
    
}
function home(){
    let commentForm = document.querySelector('.comment-form');
    commentForm.style.zIndex = "-7";
    let body = document.querySelector('.content');
    body.style.opacity = "1";
}
function skillOn(){
    let skill = document.querySelector('.prof');
    if(skill.style.zIndex =="2"){
        skill.style.zIndex = "-2";
    }
    else{
        skill.style.zIndex = "2";
    }
    
    let service = document.querySelector('.prof ul');
    body.style.opacity = "1";
}
function notice(){
    let skill = document.querySelector('.skills');
    alert("I'm sorry!! This page is still Under implementation")
}