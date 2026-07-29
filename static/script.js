async function sendMessage(){

    let question=document.getElementById("question").value;

    if(question=="") return;

    let chat=document.getElementById("chat-box");

    chat.innerHTML+=`
    <div class="user">
        <span>${question}</span>
    </div>`;

    let response=await fetch("/ask",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({question:question})
    });

    let data=await response.json();

    chat.innerHTML+=`
    <div class="bot">
        <span>${data.answer}</span>
    </div>`;

    document.getElementById("question").value="";

    chat.scrollTop=chat.scrollHeight;
}