$(document).ready(function() {
	console.log("Hello?");
	var profileLink = "/cgi-bin/profile.py?user=" + localStorage['username']

	$("#logout").click(function() {
		localStorage.removeItem('username');
	});
	
	$("#profileLink").click(function() {
		$("#profileLink").attr("href", profileLink);
	});
})