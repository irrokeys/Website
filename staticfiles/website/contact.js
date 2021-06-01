const check_consent = document.getElementById('consent');

const name_c = document.getElementById('name_c');

name_c.innerText = "Contact";

function checkform() {
    if(check_consent.checked)
    return true

    else {
        alert('please consent first');
        return false
    }

}