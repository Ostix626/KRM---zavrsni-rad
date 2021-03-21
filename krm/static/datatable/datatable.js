$(document).ready(function() {

    var table = $('#table_id').DataTable({

        responsive: true,
        pageLength: 25,
        lengthChange: false,

        buttons: [ 
            'copy',
            {
                extend: 'csvHtml5', 
                bom: true,
                fieldBoundary: '',
                fieldSeparator: '@',
                exportOptions: {
                    columns: [ 3, 4, 5, 6 ]
                }
            }, 
            {
                extend: 'excelHtml5', 
                autoFilter: true,
                messageTop: 'Poduzeće: ime poduzeća, adresa, grad',
                exportOptions: {
                    columns: ':visible'
                }
            }, 
            {
                extend: 'pdf',
                pageSize: 'A4',
                messageTop: 'Poduzeće: ime poduzeća, adresa, grad',
                exportOptions: {
                    columns: ':visible'
                }
            }, 
            {
                extend: 'print',
                pageSize: 'A4',
                messageTop: 'Poduzeće: ime poduzeća, adresa, grad',
                exportOptions: {
                    columns: ':visible'
                }
            },
            'colvis' 
        ],
        responsive    : true,
        paging        : true,
    });

    table.buttons().container()
    .appendTo( '#table_id_wrapper .col-md-6:eq(0)' );
});