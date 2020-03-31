var BASE_URL = "http://127.0.0.1:5000";

async function getData() {
  var response = await (await fetch(`${BASE_URL}/users`)).json();
  return response;
}

async function postData(data) {
  const response = await fetch(`${BASE_URL}/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });
  if (await response.ok) {
    alert("User successfully registered !");
  } else {
    alert("Incorrect data !");
  }
}

function register() {
  let name = document.getElementById("name").value;
  let email = document.getElementById("email").value;
  let pwd = document.getElementById("pwd").value;
  let data = { name: name, email: email, pwd: pwd };
  postData(data);
}

document.getElementById("register").addEventListener("click", register);
