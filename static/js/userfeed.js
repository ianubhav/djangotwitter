var tar = $('body').data('target_id');
$( ".follow-but" ).click(function() {
	if ($('.follow-but').text()=="Follow"){
		$('.follow-but').text("Following");
	}
	else {
		$('.follow-but').text("Follow");
	}
	$.ajax({
		type: "POST",
		url: '/userfollow/',
		data: {'target_id':tar},
	});
});