$(document).ready(function() { 
    var options = {
        beforeSubmit: bs_func,
        success: success_func
    };
    $('#account_form').ajaxForm(options);
    $('.calendar_field').datepicker();
});

function bs_func(formdata, jqForm, options)
{
    $('#indicator').css("display","block");
    $('input').attr('disabled', 'true');
    $('textarea').attr('disabled', 'true')
    
}

function success_func(responseText, statusText, xhr, $form)
{
    $('#indicator').css("display","none");
    $('input').removeAttr('disabled');
    $('textarea').removeAttr('disabled');
}
