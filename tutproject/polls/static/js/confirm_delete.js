/**
 * Created by mouaad on 07/12/16.
 */
$(document).ready(function() {

  $('#btnDelete').click(function() {
    bootbox.confirm("Are you sure want to delete?", function(result) {
      alert("Confirm result: " + result);
    });
  });
});