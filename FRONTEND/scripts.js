async function getData() {
  var response = await (await fetch("http://127.0.0.1:5000/users")).json();
  console.log(response);
}

async function postData(data) {
  var response = await fetch("http://127.0.0.1:5000/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: data
  });
  console.log(await response.json());
}

function submit() {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var pwd = document.getElementById("pwd").value;
  data = { name: name, email: email, pwd: pwd };
  console.log(data);
  postData(data);
}

document.getElementById("submit").addEventListener("click", submit);
