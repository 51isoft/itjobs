jQuery(function($) {
  $(".navbar #index").addClass("active");
  var job_type=0;
  function update_table() {
    $("#jobs tbody tr").each(function() {
      $(this).show();
      if (job_type == 1 && $("td:first", this).text().match(/实习|intern/)) $(this).hide();
    })
  }
  $("#job_type button").click(function(){
    if ($(this).hasClass('active')) return;
    $(this).parent().children().removeClass('active')
    $(this).addClass('active')
    if ($(this).attr('id') == 'job_all') job_type=0;
    else job_type=1;
    update_table();
    return false;
  })
});
