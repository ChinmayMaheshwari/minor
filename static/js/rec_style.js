

$('#recordButton').removeClass("Rec");
$('#recordButton').addClass("notRec");

$('#recordButton').click(function(){
	if($('#recordButton').hasClass('notRec')){
		$('#recordButton').removeClass("notRec");
		$('#recordButton').addClass("Rec");
		$('#b1').addClass("btnable");
$('#b2').addClass("btnable");
	}
	else{
		$('#recordButton').removeClass("Rec");
		$('#recordButton').addClass("notRec");
		$('#b1').removeClass("btnable");
		$('#b2').removeClass("btnable");
	}
});