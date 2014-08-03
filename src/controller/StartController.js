var StartController = function() {
	return this;
}

StartController.prototype.loadView = function() {
	DataSet.get(function(model){
		$.get('src/view/start.html', function(template) {
			var rendered = Mustache.render(template, {model: model});
			$('#placeholder').html(rendered);
		});
	})
}