$(function() {

    // This code will attach `fileselect` event to all file inputs on the page
    $(document).on('change', ':file', function() {
      var input = $(this),
          numFiles = input.get(0).files ? input.get(0).files.length : 1,
          label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
      input.trigger('fileselect', [numFiles, label]);
    });
  
    
    $(document).ready( function() {
    //below code executes on file input change and append name in text control
        $(':file').on('fileselect', function(event, numFiles, label) {
  
            var input = $(this).parents('.input-group').find(':text'),
                log = numFiles > 1 ? numFiles + ' files selected' : label;
  
            if( input.length ) {
                input.val(log);
            } else {
                if( log ) alert(log);
            }
  
        });
    });
    
  });