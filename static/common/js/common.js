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

