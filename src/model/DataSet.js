var DataSet = function(jsonData) {
	this.xValues = jsonData.xValues;
	this.datas = jsonData.datas;
	return this;
}

DataSet.get = function(callback) {
	$.ajax({
		url: "/results/results.json"
	}).done(function(jsonData){
		var model = new DataSet(jsonData)
		callback(model);
	})
}