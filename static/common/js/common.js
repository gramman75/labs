$(document).ready(function(){
	var $navList = $('#nav li a');
	$navList.click(function(){
		var $this = $(this);
		$this.parent().addClass('active');
		$navList.each(function(){
			var $eachThis = $(this);
			if ($eachThis.parent().text() != $this.parent().text()) {
				$eachThis.parent().removeClass('active');
			}
		})
	})
})

var testAjax = function(url){
	$.ajax({
		url : url,
		// data : 'applicationId='+me.value,
		async : true,
		success : function(html){			
			$('#contents').html(html);
		}
	});
}

