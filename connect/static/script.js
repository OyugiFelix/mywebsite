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