function signup_validation() {
    return true;

    var user_name = document.getElementById('user_name').value;                     //value in the input field username is assigned to a variable 'user_name'
    var user_email = document.getElementById('user_email').value;                   //value in the input field email is assigned to a variable 'user_email'
    var user_password = document.getElementById('user_password').value;                  //value in the input field password is assigned to a variable 'user_password'
    var user_confirm_pwd = document.getElementById('user_confirm_pwd').value;       //value in the input field password is assigned to a variable 'user_confirm_password'
    // var regularExpression = /^[a-zA-Z0-9!@#$%^&*]$/;

    let digit = /[0-9]/g;
    var lowercase = /[a-z]/g;
    var uppercase = /[A-Z]/g;
    console.log(user_name, user_email, user_password, user_confirm_pwd)

    if (user_name == "") {                                                          //if nothing is entered in the email field

        document.getElementById('user_name_error_msg_id').innerHTML = "Username must be filled out"; //required error message is inserted to the particular input text
        document.getElementById('user_name').style.border = '1px solid red'                      //to make the input field's border in to reddish colour
        return false;

    } else {

        document.getElementById('user_name_error_msg_id').innerHTML = "";                           //since the condition is false the form gets submitted

    }

    if (user_name.length < 8) {                                      //if nothing is entered in the email field

        document.getElementById('user_name_error_msg_id').innerHTML = "must be atleast 8 characters"; //required error message is inserted to the particular input text
        document.getElementById('user_name').style.border = '1px solid red'                      //to make the input field's border in to reddish colour
        return false;

    } else {

        document.getElementById('user_name_error_msg_id').innerHTML = "";                           //since the condition is false the form gets submitted
        document.getElementById('user_name').style.border = ""

    }

    if (user_email == "") {                                                                         //if nothing is entered in the email field

        document.getElementById('user_email_error_msg_id').innerHTML = "User email must be filled out"; //required error message is inserted to the particular input text
        document.getElementById('user_email').style.border = '1px solid red'                       //to make the input field's border in to reddish colour
        return false;                                                                              //to prevent the form from getting submitted

    } else {

        document.getElementById('user_email_error_msg_id').innerHTML = "";                           //since the condition is false the form gets submitted
        document.getElementById('user_email').style.border = ""

    }

    if (user_password == "") {

        document.getElementById('user_pwd_error_msg_id').innerHTML = "Password must be filled out";
        document.getElementById('user_password').style.border = '1px solid red'
        return false;

    } else {

        document.getElementById('user_pwd_error_msg_id').innerHTML = "";

    }

    if (user_password.length < 8) {

        document.getElementById('user_pwd_error_msg_id').innerHTML = "Password must be atleast 8 characters";
        document.getElementById('user_password').style.border = '1px solid red'
        return false;

    } else {

        document.getElementById('user_pwd_error_msg_id').innerHTML = ""

    }

    if (user_password.match(lowercase) && user_password.match(uppercase) && user_password.match(digit)) {

        document.getElementById('user_pwd_error_msg_id').innerHTML = ""
        document.getElementById('user_password').style.border = ""

    } else {

        document.getElementById('user_pwd_error_msg_id').innerHTML = "Password should contain A-Z,a-z and 0-9";
        document.getElementById('user_password').style.border = '1px solid red'
        return false;

    }


    if (user_confirm_pwd == "") {

        document.getElementById('user_confirm_pwd_error_msg_id').innerHTML = "Repeat your password";
        document.getElementById('user_confirm_pwd').style.border = '1px solid red'
        return false;

    } else {

        document.getElementById('user_confirm_pwd_error_msg_id').innerHTML = ""
        document.getElementById('user_confirm_pwd').style.border = ""


    }

    if (user_confirm_pwd != user_password) {

        document.getElementById('user_confirm_pwd_error_msg_id').innerHTML = "Passwords does not match";
        document.getElementById('user_confirm_pwd').style.border = '1px solid red'
        return false;

    } else {

        document.getElementById('user_confirm_pwd_error_msg_id').innerHTML = ""
        document.getElementById('user_confirm_pwd').style.border = ""

    }

}

// document.getElementById('show_pwd_check').onclick = function show_pwd() {
//     if (this.checked) {
//         document.getElementById('user_pwd').type = "text";
//     } else {
//         document.getElementById('user_pwd').type = "password";
//     }
// };
