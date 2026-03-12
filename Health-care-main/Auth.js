/**
 * auth.js — Include at the bottom of <body> on EVERY page
 * Reads localStorage "hm_user" and updates the navbar login button
 */
(function () {
  var user = localStorage.getItem("hm_user");
  var loginDiv = document.getElementById("Login");
  if (!loginDiv) return;

  if (user) {
    loginDiv.innerHTML =
      '<span style="display:inline-flex;align-items:center;gap:6px;' +
      'background:#e0fff5;border:1.5px solid #00c98d;border-radius:50px;' +
      'padding:6px 14px;font-family:Nunito,sans-serif;font-weight:700;' +
      'font-size:13px;color:#00a374;cursor:pointer;white-space:nowrap;" ' +
      'onclick="logoutUser()">&#x1F464; ' + user + ' &nbsp;&middot;&nbsp; Logout</span>';
  } else {
    // Make sure the Login link is shown (it already is by default HTML, but just in case)
    if (!loginDiv.querySelector('a')) {
      loginDiv.innerHTML = '<a href="Login.html">Login</a>';
    }
  }
})();

function logoutUser() {
  localStorage.removeItem("hm_user");
  window.location.href = "Login.html";
}