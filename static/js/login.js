grecaptcha.ready(function () {
    $('#form1').submit(function (e) {
        var form = this;
        e.preventDefault()
        grecaptcha.execute('6LdE360ZAAAAAMYLHV5BEZwNfrq4_KyGIL9QIb-h', { action: 'submit' }).then(function (token) {
            $('#recaptcha').val(token)
            form.submit()
        });
    })
});