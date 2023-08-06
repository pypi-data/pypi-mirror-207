function setCookie(name, value, daysToExpire) {
    let expireDate = new Date();
    expireDate.setDate(expireDate.getDate() + daysToExpire);
    let cookieValue = encodeURIComponent(value) + ((daysToExpire == null) ? '' : '; expires=' + expireDate.toUTCString());
    document.cookie = name + '=' + cookieValue + '; path=/';
}

const resaze_bg_login = () => {
    if (window.matchMedia('screen and (max-width: 1230px)').matches) {
        element_bg_login.removeClass('width')
    }
    else if (
        (window.matchMedia('screen and (min-width: 1169px)').matches) ||
        (window.matchMedia('screen and (max-height: 700px)').matches)) {
        element_bg_login.addClass('width')
    } else {
        element_bg_login.removeClass('width')
    }
}
const get_submit_login = ({ url, next, email, senha, remember }) => {
    let submit_login = e => {
        e.preventDefault()
        let user = $(email).val()
        let pass = $(senha).val()
        let has_remember = $(remember).is(':checked')
        payload = {
            'email': user,
            'senha': pass,
        }
        generic_post({
            url: url,
            payload: payload,
            success: data => {
                $.ajaxSetup({
                    headers: {
                        "Authorization": "Bearer " + data.access_token,
                    }
                })
                if (has_remember) {
                    localStorage.setItem('email', user)
                }
                setCookie('access_token_cookie', data.access_token, 1)
                location.href = next
            },
            error: error => {
                console.log(error)
            }
        })
    }
    return submit_login
}
const generic_post = ({ url, payload, success, error }) => {
    $.ajax({
        url: url,
        method: 'POST',
        data: payload,
        success: success,
        error: error
    })
}
const remember_email = () => {
    let email = localStorage.getItem('email')
    if (email) {
        $('#email').val(email)
        $('#remember').prop('checked', true)
        $('#senha').focus()
    }
}