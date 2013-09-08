jQuery(function($) {
  $(".navbar #index").addClass("active");
  var job_type=0;
  var job_source=0;
  function update_table() {
    $("#jobs tbody tr").each(function() {
      $(this).show();
      if (job_type == 1 && $("td:first", this).text().match(/实习|intern/i)) $(this).hide();
      if (job_source == 1 && $("td:nth-child(3)", this).text() != "水木清华BBS") $(this).hide();
      if (job_source == 2 && $("td:nth-child(3)", this).text() != "北师就业中心") $(this).hide();
      if (job_source == 3 && $("td:nth-child(3)", this).text() != "大街网") $(this).hide();
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
  });
  $("#job_source button").click(function(){
    if ($(this).hasClass('active')) return;
    $(this).parent().children().removeClass('active')
    $(this).addClass('active')
    if ($(this).attr('id') == 'job_smth') job_source=1;
    else if ($(this).attr('id') == 'job_bnu') job_source=2;
    else if ($(this).attr('id') == 'job_dajie') job_source=3;
    else job_source=0;
    update_table();
    return false;
  });
});
