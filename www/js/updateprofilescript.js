<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
		<script type="text/javascript">
		var profileLink = "/cgi-bin/profile.py?user=" + localStorage['username']
			$(document).ready(function() {
			$("#logout").click(function() {
				localStorage.removeItem('username');
				console.log("You out dawg!");
			});

			$("#profileLink").click(function() {
				console.log("Hello?");
				$("#profileLink").attr("href", profileLink);
				console.log("Hello!");
			});

			$("#submit").click(function(){
				
				
			})
		})
		</script>