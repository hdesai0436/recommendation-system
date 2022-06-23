$(document).ready(function(){
    $(".content").slice(0, 8).show();
    $("#loadMore").on("click", function(e){
      e.preventDefault();
      $(".content:hidden").slice(0, 8).slideDown();
      if($(".content:hidden").length == 0) {
        $("#loadMore").text("No Content").addClass("noContent");
      }
    });
    
})

function loadmore(){
	var status = $('#status');
    status.show();
	
}
function hide(){
    $(window).on('load', function() {
        
    })
}

$('#autoComplete').keypress(function(e){
    var title = $('#autoComplete').val()
    
    if (e.which == 13){
        
       window.location.href='/movie/'+title
    }
})


// $(document).on('click', '#reco_title', function(event) {
//     event.preventDefault();
//     event.preventDefault();
//     var actor_name = $(this).text().trim()
//     alert(actor_name)
//     window.location.href = '/actor/'+ actor_name
// });


$(document).on('click', '#actor_name', function(event) {
    event.preventDefault();
    event.preventDefault();
    var actor_name = $(this).text().trim()
   
    window.location.href = '/actor/'+ actor_name
});





    






$(document).ready(function() {
    // Configure/customize these variables.
    var showChar = 100;  // How many characters are shown by default
    var ellipsestext = "...";
    var moretext = "Show more >";
    var lesstext = "Show less";
    var readsummary = 'read summary'

    $('.more').each(function() {
        var content = $(this).html();
 
        if(content.length > showChar) {
 
            var c = content.substr(0, showChar);
            var h = content.substr(showChar, content.length - showChar);
 
            var html = c + '<span class="moreellipses">' + ellipsestext+ '&nbsp;</span><span class="morecontent"><span>' + h + '</span>&nbsp;&nbsp;<a href="" class="morelink">' + moretext + '</a>&nbsp;&nbsp;</span>';
 
            $(this).html(html);
        }
 
    });
 
    $(".morelink").click(function(){
        if($(this).hasClass("less")) {
            $(this).removeClass("less");
            $(this).html(moretext);
        } else {
            $(this).addClass("less");
            $(this).html(lesstext);
        }
        $(this).parent().prev().toggle();
        $(this).prev().toggle();
        return false;
    });
});













function AddReadMore() {

    $(document).on("click", ".readsumm", function(e) {
       
        var data = {
            review :$(this).parents('td').text() ,
        }
            $.ajax({
                type:'POST',
                url:'/summary',
                dataType:'json',
                data :data,
                success:function(res){
                
                    
                },
                error:function(r){
                    alert(r.responseJSON.error)
                }
            })
                e.preventDefault()
    });
   
}
