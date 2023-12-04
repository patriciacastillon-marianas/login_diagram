
function formvalid() {
    var validpass = document.getElementById("pwinput").value;

    if (validpass.length <= 8 || validpass.length >= 20) {
        document.getElementById("valid-pass").innerHTML = "Minimum 8 characters";
        return false;
    } else {
        document.getElementById("valid-pass").innerHTML = "";

    }
}


$(document).ready(function() {
    $('#loginForm').submit(function(e) {
        e.preventDefault();
        var username = $('#username').val();
        var password = $('#password').val();
        
        // Perform login validation
        if (username === 'firstname.lastname' && password === 'password') {
            alert('Login successful!');
        } else {
            alert('Invalid username or password. Please try again.');
        }
    });
});
