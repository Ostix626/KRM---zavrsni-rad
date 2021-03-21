$(function () {
    $( '#table' ).searchable({
        striped: false,
        oddRow: { 'background-color': '#f5f5f5' },
        evenRow: { 'background-color': '#fff' },
        searchType: 'default'
    });
    
    $( '#searchable-container' ).searchable({
        searchField: '#container-search',
        selector: '.row',
        childSelector: '.col-xs-4',
        show: function( elem ) {
            elem.slideDown(100);
        },
        hide: function( elem ) {
            elem.slideUp( 100 );
        }
    })
});