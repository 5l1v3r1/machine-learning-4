/**
 * ajax_data.js: this script utilizes ajax to relay the form POST data, to a defined
 *               'action' script.
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // Local Variables
    var dataset      = $('input[name="svm_dataset[]"]');
    var pInput       = $('input[name="prediction_input[]"]');
    var flag_dataset = true;
    var flag_pInput  = true;

  // Check if data supplied
    dataset.each(function() {
      if ( typeof $(this).val() === 'undefined' ) {
        flag_dataset = false;
        return false;
      }
    });
    pInput.each(function() {
      if ( typeof $(this).val() === 'undefined' ) {
        flag_pInput = false;
        return false;
      }
    });

  // AJAX Process
    if ( flag_dataset || flag_pInput ) {
      $.ajax({
        url: $(this).attr('action'),
        type: 'POST',
        data: new FormData( this ),
        dataType: 'json',
        contentType: false,
        processData: false,
        beforeSend: function() {

        // AJAX Overlay
          ajaxLoader( $(event.currentTarget) );

        // Form Validation
          $("form").validate({
            submitHandler: function(form) {
              $(form).ajaxSubmit();
            }
          });
        }
      }).done(function(data) {

      // JSON Object from Server
        if (data.result) {
          var obj_result = '\
                <fieldset class="fieldset-prediction-result">\
                  <legend>Prediction Result</legend>\
                  <p class="result"></p>\
                </fieldset>\
              ';

          if (data.result.error) {
            $('.fieldset-prediction-result').remove();
            $('.fieldset-session-predict').append(obj_result);
            $('.result').append(data.result.error);
          }

          else if (data.result.result) {
            $('.fieldset-prediction-result').remove();
            $('.fieldset-session-predict').append(obj_result);
            $('.result').append(data.result.result);
          }
        }
        else {
          json_server = ( !$.isEmptyObject( data ) ) ? JSON.stringify(data, undefined, 2) : 'none';
          console.log( 'JSON object from Server: ' + json_server );
        }

      // Remove AJAX Overlay
        $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove(); });

      }).fail(function(jqXHR, textStatus, errorThrown) {
        console.log('Error Thrown: '+errorThrown);
        console.log('Error Status: '+textStatus);

      // Remove AJAX Overlay
        $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove(); });
      });
    }

  });
});
